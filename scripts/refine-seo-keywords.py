#!/usr/bin/env python3
"""Apply the reviewed SEO wording, preserving article titles, slugs and image files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESCRIPTIONS = {
    'E5.3.09': 'Socialismo y medio ambiente: Aral, Chernóbil y emisiones de Polonia. Fuentes primarias, análisis institucional y límites para comparar sus efectos.',
    'E7.6.11': 'INDEC y las estadísticas argentinas de 2007–2015: multas a consultoras, censura del FMI y revisión de series. Fuentes y límites de la comparación.',
    'E7.10.11': 'Puertas giratorias: qué exige la Ley 3/2015 tras el cese, qué muestran los informes de 2026 y cómo comparar controles sin acusaciones automáticas.',
    'E7.5.01': 'Tipos de monopolio: natural, legal y de facto. Revisa a Baumol, el papel de la tecnología y los criterios de MEE para evaluar privilegios y redes.',
    'E3.4.10': 'Intercambio en Cuba: mercados duales, moneda, reglas y disponibilidad. Revisa la libreta, las divisas y la diferencia entre norma y acceso real.',
    'E7.6.04': 'Autopistas radiales: RPA, concesiones en quiebra, liquidaciones de 2025 y gestión de SEITT. Qué permite calcular el coste público del rescate.',
    'E7.6.02': 'Beneficios concentrados y costes dispersos: Olson, Buchanan y el caso del azúcar estudiado por la GAO. Quién gana, quién paga y cómo revisar ayudas.',
    'E7.5.04': 'Fijar precios por decreto: de Diocleciano a los topes actuales. Escasez, colas y mercados informales, con matices ante emergencias y monopolios.',
    'E7.5.03': 'Reforma de telecomunicaciones de México en 2013: diagnóstico de la OCDE, precios y concentración. Revisa el cambio del IFT por la CRT en 2025.',
    'E7.10.13': 'Corrupción y regulación: qué relaciona permisos y sobornos, qué muestran Djankov y Svensson y por qué conviene comprobar los efectos de cada reforma.',
    'E5.3.04': 'Libertad política y económica: Friedman, Fraser y Freedom House. Revisa las diferencias y los límites de comparar Singapur, China y Chile.',
    'E5.3.03': 'Incentivos y trabajo: la reforma agrícola china, evidencia de Lin y límites de la comparación soviética. Objeciones sobre motivación y cooperación.',
    'E7.10.14': 'Denunciar corrupción: canales oficiales y protección del informante en España, con referencias de México y Perú. Requisitos, límites y preparación.',
    'E7.5.02': 'Apertura de las telecomunicaciones en Costa Rica: referéndum de 2007, Ley 8642 y operadores desde 2011. Datos de SUTEL y límites de la evaluación.',
    'E7.10.15': 'Pedir información pública en España, México y Colombia: contratos, normas, plazos y autoridades. Modelo de solicitud y revisión de respuestas incompletas.',
    'E5.1.14': 'Preguntas sobre el capitalismo: pobreza, grandes fortunas, medio ambiente y solidaridad. Respuestas con fuentes, límites y lecturas para ampliar.',
    'E7.8.08': 'Cuentas congeladas en Canadá en 2022: medidas de emergencia, informe Rouleau y recurso admitido por el Supremo en octubre de 2026. Claves del caso.',
    'E7.8.06': 'Rescate interno en Chipre en 2013: depósitos no asegurados, Laiki y Bank of Cyprus. Conversión en acciones y controles temporales: qué ocurrió.',
    'E5.3.11': 'El sistema económico de Cuba en 2026: Constitución, reformas de empresas privadas y divisas. Fuentes originales y límites para evaluar el papel de GAESA.',
    'E7.6.09': 'Financiación de ONG: cómo revisar ayudas en la BDNS y distinguir transparencia de persecución. Rusia, Nicaragua y garantías para el control público.',
    'E7.10.07': 'Sobornos cotidianos: qué miden la ENCIG 2025 y el Barómetro regional de 2019. Experiencias, pagos, trámites y límites para interpretar sus cifras.',
    'E7.6.06': 'Medios públicos: compara financiación y control en BBC, RTVE y Cuba, las garantías europeas y los límites del índice de RSF de 2026.',
    'E7.6.08': 'Libertad académica: qué mide el Academic Freedom Index 2026 y qué límites tienen las encuestas. Presiones, financiación y autonomía universitaria.',
}


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    path = ROOT / 'editorial/seo-keyword-refinements.json'
    rows = json.loads(path.read_text())
    payload_path = ROOT / 'wordpress/plugins/mee-editorial/data/seo-migration.json'
    payload = json.loads(payload_path.read_text())
    by_id = {entry['id']: entry for entry in payload}
    changes = []
    # Validate the complete review before writing any article.
    for row in rows:
        row['description'] = DESCRIPTIONS.get(row['id'], row['description'])
        assert row['keyword'].casefold() in row['seo_title'].casefold(), row['id']
        assert row['keyword'].casefold() in row['description'].casefold(), row['id']
        assert len(row['description']) <= 160, row['id']
    for row in rows:
        article_path = ROOT / 'editorial/articles' / row['id'] / 'article.json'
        article = json.loads(article_path.read_text())
        entry = by_id[row['id']]
        assert article['title'] == entry['title'] and article['slug'] == entry['slug']
        for key in ('keyword', 'seo_title', 'description'):
            assert article[key] in (row['previous_' + key], row[key]), (row['id'], key)
            article[key] = entry[key] = row[key]
        if not any(row['keyword'].casefold() in image['alt'].casefold() for image in article['images'].values()):
            image = article['images']['featured']
            previous = image['alt']
            scene = previous.split('»: ', 1)[-1]
            scene = scene[:1].lower() + scene[1:]
            image['alt'] = f'Ilustración editorial para «{row["keyword"]}»: {scene}'
            entry['images']['featured']['previous_alt'] = previous
            entry['images']['featured']['alt'] = image['alt']
            entry['images']['featured']['description'] = image['alt'] + f' Ilustración conceptual original del artículo «{article["title"]}», de MEE.'
            changes.append({'id': row['id'], 'role': 'featured', 'before': previous, 'after': image['alt']})
        write(article_path, article)
    write(path, rows)
    write(payload_path, payload)
    write(ROOT / 'editorial/seo-keyword-image-refinements.json', changes)
    print(json.dumps({'articles_reviewed': len(rows), 'descriptions_refined': len(DESCRIPTIONS), 'cover_alts_refined': len(changes), 'article_titles_slugs_files': 'preserved'}, ensure_ascii=False))
