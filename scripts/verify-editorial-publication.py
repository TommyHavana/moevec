#!/usr/bin/env python3
"""Verify published plan entries and their three editorial assets over public HTTP."""
import concurrent.futures
import hashlib
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = []
        self.in_h1 = False
        self.canonicals = []
        self.robots = []
        self.images = []
        self.ids = set()
        self.links = []
        self.schemas = []
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'h1':
            self.in_h1 = True
            self.h1.append('')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href'))
        if tag == 'meta' and a.get('name') == 'robots':
            self.robots.append(a.get('content', ''))
        if tag == 'img':
            self.images.append(a)
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_schema = True
            self.schemas.append('')

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False
        if tag == 'script':
            self.in_schema = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1[-1] += data
        if self.in_schema:
            self.schemas[-1] += data


def get(url):
    return urllib.request.urlopen(url, timeout=30)


def verify(ident):
    directory = ROOT / 'editorial/articles' / ident
    manifest = json.loads((directory / 'article.json').read_text())
    publication = json.loads((directory / 'publication.json').read_text())
    url = publication['url']
    response = get(url)
    html = response.read().decode()
    page = Page()
    page.feed(html)
    issues = []
    # The existing MEE template appends a decorative .title-dot span.
    if page.h1 not in ([manifest['title']], [manifest['title'] + '.']):
        issues.append('H1 differs from plan')
    if page.canonicals != [url]:
        issues.append('Canonical differs from URL')
    robots = ' '.join(page.robots) + ' ' + response.headers.get('X-Robots-Tag', '')
    if re.search(r'\b(?:noindex|none)\b', robots, re.I):
        issues.append('Article is not indexable')
    schemas = [json.loads(s) for s in page.schemas]
    has_article_schema = any('Article' in json.dumps(s) for s in schemas)
    if not has_article_schema:
        issues.append('Article schema absent')
    body = (directory / 'article.html').read_text()
    expected_anchors = re.findall(r'<h2 id="([^"]+)"', body)
    for anchor in expected_anchors:
        if anchor not in page.ids or not any(link.endswith('#' + anchor) for link in page.links):
            issues.append('Missing heading or TOC link: ' + anchor)
    checked_images = []
    for role, expected in manifest['images'].items():
        matches = [a for a in page.images if expected['file'].removesuffix('.webp') in a.get('src', '')]
        if len(matches) != 1:
            issues.append('Expected one image for ' + role)
            continue
        actual = matches[0]
        if actual.get('alt') != expected['alt'] or not all(actual.get(k) for k in ('width', 'height')):
            issues.append('Alt or dimensions invalid for ' + role)
        original = actual['src']
        # WP may render a responsive derivative. Verify the original and rendered URL.
        upload_url = original.rsplit('/', 1)[0] + '/' + expected['file']
        resource = get(upload_url)
        data = resource.read()
        if resource.headers.get_content_type() != 'image/webp' or len(data) >= 250000:
            issues.append('Invalid original WebP for ' + role)
        if hashlib.sha256(data).digest() != hashlib.sha256((directory / expected['file']).read_bytes()).digest():
            issues.append('Original differs from locally reviewed asset for ' + role)
        rendered = get(original)
        if rendered.status != 200 or rendered.headers.get_content_type() != 'image/webp':
            issues.append('Rendered image unavailable for ' + role)
        checked_images.append({'role': role, 'url': upload_url, 'bytes': len(data), 'alt': actual['alt']})
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'id': ident, 'url': url,
              'status': response.status, 'h1': page.h1, 'canonical': page.canonicals,
              'robots': robots.strip(), 'schema_article': has_article_schema,
              'toc_headings': len(expected_anchors), 'images': checked_images, 'issues': issues}
    (directory / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return {'id': ident, 'status': response.status, 'images': len(checked_images), 'issues': issues}


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        reports = list(pool.map(verify, sys.argv[1:]))
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    if not reports or any(r['issues'] for r in reports):
        raise SystemExit(1)
