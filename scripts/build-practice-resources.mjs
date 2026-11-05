import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const out='/private/tmp/mee-resources-20261105/outputs/mee-20261105';
await fs.mkdir(out,{recursive:true});
function base(title,cols='E',rows=35){
 const w=Workbook.create(),s=w.worksheets.add('Practica');s.showGridLines=false;
 s.getRange(`A1:${cols}${rows}`).format.font={name:'Arial',size:11,color:'#161820'};
 s.getRange(`A1:${cols}${rows}`).format.rowHeight=25;
 s.getRange('A:A').format.columnWidth=35;
 s.getRange(`B:${cols}`).format.columnWidth=22;
 s.mergeCells(`A2:${cols}2`);s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:17,bold:true,color:'#1642cd'};s.getRange('A2').format.rowHeight=36;
 s.mergeCells(`A3:${cols}3`);s.getRange('A3').values=[['MEE · Datos ficticios. Cantidades en unidades monetarias (u.m.).']];
 s.getRange('A3').format.font={color:'#555b67',size:10};s.getRange('A3').format.rowHeight=28;
 s.freezePanes.freezeRows(6);return {w,s};
}
function heading(s,range){s.getRange(range).format.fill='#1642cd';s.getRange(range).format.font={bold:true,color:'#ffffff'};}
function note(s,row,text,last='E'){s.mergeCells(`A${row}:${last}${row}`);s.getRange(`A${row}`).values=[[text]];s.getRange(`A${row}`).format.wrapText=true;s.getRange(`A${row}`).format.rowHeight=40;}
async function finish(slug,w,s,range,checks){
 w.recalculate();
 for(const [cell,expected]of checks){const actual=s.getRange(cell).values[0][0];if(typeof expected==='number'?Math.abs(actual-expected)>1e-8:actual!==expected)throw Error(slug+' '+cell+' expected '+expected+' got '+actual);}
 const scan=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:30},maxChars:1500});
 await fs.writeFile(out+'/'+slug+'-inspection.json',JSON.stringify({checks,scan:scan.ndjson},null,2));
 const blob=await w.render({sheetName:'Practica',range,scale:1.5});await fs.writeFile(out+'/'+slug+'.png',new Uint8Array(await blob.arrayBuffer()));
 await(await SpreadsheetFile.exportXlsx(w)).save(out+'/'+slug+'.xlsx');
 console.log(slug,checks);
}
{
 const {w,s}=base('Presupuesto de un mes','D',29);
 note(s,4,'Edita B y C. Diferencia = registrado − previsto. El saldo no incluye importes fuera de esta hoja.','D');
 s.getRange('A6:D6').values=[['Concepto','Previsto','Registrado','Diferencia']];heading(s,'A6:D6');
 s.getRange('A7:C8').values=[['Ingreso principal',2000,2000],['Otros ingresos',100,50]];
 s.getRange('A10').values=[['Total ingresos']];s.getRange('B10:C10').formulas=[['=SUM(B7:B8)','=SUM(C7:C8)']];
 s.getRange('A12:D12').values=[['Gastos','Previsto','Registrado','Diferencia']];heading(s,'A12:D12');
 s.getRange('A13:C18').values=[['Vivienda',780,800],['Alimentación',260,300],['Transporte',120,110],['Suministros',90,100],['Ocio',80,70],['Otros gastos',150,150]];
 for(const row of [7,8,10,13,14,15,16,17,18,20,22])s.getRange(`D${row}`).formulas=[[`=C${row}-B${row}`]];
 s.getRange('A20').values=[['Total gastos']];s.getRange('B20:C20').formulas=[['=SUM(B13:B18)','=SUM(C13:C18)']];
 s.getRange('A22').values=[['Saldo del mes']];s.getRange('B22:C22').formulas=[['=B10-B20','=C10-C20']];
 s.getRange('B7:C8').format.font={color:'#1642cd'};s.getRange('B13:C18').format.font={color:'#1642cd'};s.getRange('B7:D22').setNumberFormat('#,##0.00;(#,##0.00);"—"');
 for(const row of [10,20,22]){s.getRange(`A${row}:D${row}`).format.font={bold:true,color:'#161820'};s.getRange(`A${row}:D${row}`).format.fill='#eef1fa';}
 note(s,24,'Prueba: añade 100 u.m. al gasto registrado de vivienda. El saldo registrado baja de 520 a 420.','D');
 note(s,26,'Antes de usar: sustituye todos los ejemplos, comprueba el periodo y revisa que no falten ingresos o pagos.','D');
 note(s,28,'Origen: ejemplo educativo original MEE · moevec.org/recursos/ · 05/11/2026.','D');
 s.getRange('C13').values=[[900]];w.recalculate();if(s.getRange('C22').values[0][0]!==420)throw Error('budget edit failed');s.getRange('C13').values=[[800]];
 await finish('presupuesto-mensual',w,s,'A1:D29',[['B22',620],['C22',520],['D22',-100]]);
}
{
 const {w,s}=base('Practicar diez funciones','E',35);
 note(s,4,'Edita cantidades, precios y stock. D calcula cantidad × precio. E contiene el stock; IF lo compara con la cantidad pedida.');
 s.getRange('A6:E6').values=[['Producto ficticio','Cantidad','Precio unitario','Importe','Stock']];heading(s,'A6:E6');
 s.getRange('A7:C10').values=[['Cuaderno',8,4.5],['Carpeta',5,3],['Lápiz',20,0.8],['Agenda',3,12]];
 s.getRange('E7:E10').values=[[12],[4],[30],[5]];
 for(let row=7;row<=10;row++)s.getRange(`D${row}`).formulas=[[`=ROUND(B${row}*C${row},2)`]];
 s.getRange('B7:C10').format.font={color:'#1642cd'};s.getRange('E7:E10').format.font={color:'#1642cd'};s.getRange('C7:D10').setNumberFormat('#,##0.00');
 s.getRange('A13:C13').values=[['Función en inglés','Resultado','Qué observar']];heading(s,'A13:C13');
 const rows=[['SUM','=SUM(D7:D10)','Suma de importes'],['AVERAGE','=AVERAGE(C7:C10)','Precio medio simple'],['MIN','=MIN(C7:C10)','Precio mínimo'],['MAX','=MAX(C7:C10)','Precio máximo'],['COUNT','=COUNT(B7:B10)','Celdas numéricas'],['COUNTA','=COUNTA(A7:A10)','Nombres presentes'],['IF','=IF(E8>=B8,"Suficiente","Revisar stock")','Carpeta: 4 en stock para 5 pedidas'],['SUMIF','=SUMIF(C7:C10,">=4",D7:D10)','Importes de precios ≥ 4'],['COUNTIF','=COUNTIF(C7:C10,">=4")','Productos con precio ≥ 4'],['ROUND','=ROUND(10/3,2)','Redondeo a dos decimales']];
 for(let i=0;i<rows.length;i++){const n=14+i;s.getRange(`A${n}`).values=[[rows[i][0]]];s.getRange(`B${n}`).formulas=[[rows[i][1]]];s.getRange(`C${n}:E${n}`).merge();s.getRange(`C${n}`).values=[[rows[i][2]]];}
 s.getRange('B14:B23').setNumberFormat('0.00');s.getRange('B14:B23').format.horizontalAlignment='center';
 note(s,26,'Prueba: cambia la cantidad de cuadernos de 8 a 10. El total pasa de 103 a 112 u.m.');
 note(s,28,'XLSX almacena fórmulas en inglés. Tu programa puede mostrarlas traducidas y con separadores distintos.');
 note(s,30,'Para extender la tabla, revisa los rangos de las fórmulas. Un resultado calculado no detecta todos los errores de datos.');
 note(s,32,'Fuente de datos: ejemplo ficticio MEE. Funciones: help.libreoffice.org/latest/es/text/scalc/01/04060100.html');
 s.getRange('B7').values=[[10]];w.recalculate();if(s.getRange('B14').values[0][0]!==112)throw Error('practice edit failed');s.getRange('B7').values=[[8]];
 await finish('practica-hojas-de-calculo',w,s,'A1:E33',[['B14',103],['B20','Revisar stock'],['B21',72],['B22',2],['B23',3.33]]);
}
{
 const {w,s}=base('Comparar dos alternativas','E',29);
 note(s,4,'Ejemplo ficticio: dos cursos. Cambia criterios, pesos y notas (0–5, mayor es mejor). La puntuación depende de tus juicios.');
 s.getRange('A6:E6').values=[['Criterio','Peso','Curso A (0–5)','Curso B (0–5)','Dato pendiente']];heading(s,'A6:E6');
 s.getRange('A7:E9').values=[['Ajuste al objetivo',0.5,3,4,'Ver el temario'],['Tiempo disponible',0.3,4,2,'Confirmar horarios'],['Coste asumible',0.2,2,4,'Ver precio completo']];
 s.getRange('B7:D9').format.font={color:'#1642cd'};s.getRange('B7:B9').setNumberFormat('0%');s.getRange('B11').formulas=[['=SUM(B7:B9)']];s.getRange('A11').values=[['Suma de pesos']];s.getRange('B11').setNumberFormat('0%');
 s.getRange('A13').values=[['Puntuación ponderada']];s.getRange('C13:D13').formulas=[['=IF(OR(COUNT(B7:B9)<3,COUNT(C7:C9)<3,SUM(B7:B9)<=0),"Faltan datos",SUMPRODUCT(B7:B9,C7:C9)/SUM(B7:B9))','=IF(OR(COUNT(B7:B9)<3,COUNT(D7:D9)<3,SUM(B7:B9)<=0),"Faltan datos",SUMPRODUCT(B7:B9,D7:D9)/SUM(B7:B9))']];s.getRange('C13:D13').setNumberFormat('0.00');
 s.getRange('C7:D9').dataValidation={rule:{type:'whole',operator:'between',formula1:0,formula2:5}};s.getRange('B7:B9').dataValidation={rule:{type:'decimal',operator:'between',formula1:0,formula2:1}};
 note(s,16,'Coste total A (u.m.): 120. Coste total B: 180. Tiempo A: 20 h. Tiempo B: 12 h. Son ejemplos, no ofertas.');
 note(s,18,'Antes de decidir: escribe qué información falta, cómo la comprobarás y qué condición descarta cada opción.');
 note(s,20,'Condición que descarta A: _____________________   Condición que descarta B: _____________________');
 note(s,22,'Prueba: si el ajuste de A pasa de 3 a 5, su puntuación pasa de 3,10 a 4,10. Revisa si el criterio sigue teniendo sentido.');
 note(s,24,'La puntuación no incorpora condiciones de descarte, riesgos no descritos ni incertidumbre. Completa esos datos antes de actuar.');
 note(s,26,'Origen: ejemplo educativo original MEE · moevec.org/recursos/ · 05/11/2026.');
 s.getRange('C7').values=[[5]];w.recalculate();if(Math.abs(s.getRange('C13').values[0][0]-4.1)>1e-8)throw Error('decision edit failed');s.getRange('C7').values=[[3]];
 s.getRange('D8').values=[[null]];w.recalculate();if(s.getRange('D13').values[0][0]!=='Faltan datos')throw Error('blank guard failed');s.getRange('D8').values=[[2]];
 await finish('comparar-decisiones',w,s,'A1:E27',[['C13',3.1],['D13',3.4]]);
}
