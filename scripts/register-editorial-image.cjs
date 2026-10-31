// Register a newly generated original without overwriting an existing asset.
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

(async () => {
  const [id, role, source] = process.argv.slice(2);
  if (!/^E\d+\.\d+\.\d+$/.test(id) || !['featured', 'interior-1', 'interior-2'].includes(role)) throw Error('Invalid article or role');
  const directory = path.resolve(__dirname, '../editorial/articles', id);
  const promptsPath = path.join(directory, 'image-prompts.json');
  const prompts = JSON.parse(fs.readFileSync(promptsPath));
  const metadata = JSON.parse(fs.readFileSync(path.join(directory, 'metadata-draft.json')));
  const output = path.join(directory, metadata.images[role].file);
  if (fs.existsSync(output) || prompts.sources[role]) throw Error('Asset already registered; inspect before resuming');
  const width = role === 'featured' ? 1200 : 1600;
  const height = role === 'featured' ? 630 : 900;
  let quality = 80, buffer;
  do {
    buffer = await sharp(source).resize(width, height, { fit: 'cover', position: 'centre' }).webp({ quality, effort: 6 }).toBuffer();
    if (buffer.length < 250000) break;
    quality -= 4;
  } while (quality >= 40);
  if (buffer.length >= 250000) throw Error('Image exceeds budget');
  fs.writeFileSync(output, buffer, { flag: 'wx' });
  const assetsPath = path.join(directory, 'assets.json');
  const assets = fs.existsSync(assetsPath) ? JSON.parse(fs.readFileSync(assetsPath)) : {};
  assets[role] = { file: metadata.images[role].file, width, height, bytes: buffer.length, quality };
  fs.writeFileSync(assetsPath, JSON.stringify(assets, null, 2) + '\n');
  prompts.sources[role] = source;
  fs.writeFileSync(promptsPath, JSON.stringify(prompts, null, 2) + '\n');
  fs.writeFileSync(path.join(directory, 'generation-' + role + '.json'), JSON.stringify({ id, role, tool: 'builtin_image_gen', local_paths: [source] }, null, 2) + '\n');
  process.stdout.write(JSON.stringify({ id, role, file: output, bytes: buffer.length, quality }) + '\n');
})().catch(error => { process.stderr.write(error.message + '\n'); process.exitCode = 1; });
