import {readFile,writeFile} from 'node:fs/promises';
const shared=await readFile('app/styles.css','utf8');
const editorial=await readFile('wordpress/themes/mee-child/editorial.css','utf8');
await writeFile('wordpress/themes/mee-child/style.css',`/*\nTheme Name: MEE Editorial\nDescription: Editorial MEE conectado visualmente con React.\nTemplate: hello-elementor\nVersion: 1.0.0\nText Domain: mee-editorial\n*/\n${shared}\n${editorial}`);
