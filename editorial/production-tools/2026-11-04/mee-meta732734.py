from pathlib import Path
import json

def source(name, url, scope, public_scope):
    return dict(name=name, url=url, scope=scope, public_scope=public_scope)

metadata = {
    'E6.7.12': dict(
        seo_title='Delegar sin perder el control: decisiones y límites | MEE',
        description='Delegar sin perder el control: una actividad, facultades y revisión. MEE propone siete posiciones orientativas y tres preguntas para revisar acuerdos.',
        keyword='delegar sin perder el control',
        secondary=['pequeños negocios', 'facultades de decisión', 'procesos documentados', 'conocimiento distribuido'],
        standfirst='Delegar sin perder el control: una propuesta de MEE para conversar sobre resultados, recursos y facultades, con ejemplos hipotéticos y revisión del trabajo.',
        sources=[source(
            'F. A. Hayek · The Use of Knowledge in Society · 1945',
            'https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/92/Hayek_0766_EBk_v6.0.pdf',
            'PDF primario de Library of Economics and Liberty/OLL, copia archivada y texto seleccionado. Para esta entrada se han leído las páginas PDF5 y7 sobre información incompleta y conocimiento de circunstancias particulares. No se declara lectura íntegra de las17 páginas. Aplicación a encargos, siete posiciones y tres preguntas: propuestas originales de MEE, no metodología de Hayek ni escala científica. Sin citar o declarar leído La fatal arrogancia.',
            'Pasajes sobre conocimiento distribuido, páginas5 y7 del PDF; aplicación empresarial propuesta por MEE.')],
        omitted=['No escala validada ni método atribuido a un autor sin fuente.', 'Sin mejoras de productividad o errores medidas; tienda y taller hipotéticos.', 'No libro o PDF completo declarado leído.']),
    'E6.7.13': dict(
        seo_title='Redes de negocios autónomos: acuerdos y límites | MEE',
        description='Redes de negocios autónomos: compras y servicios compartidos. MEE propone revisar recursos, identidad, decisiones y desacuerdos antes de comprometerse.',
        keyword='redes de negocios autónomos',
        secondary=['cooperación empresarial', 'compras conjuntas', 'marca colectiva', 'gobernanza'],
        standfirst='Redes de negocios autónomos: ejemplos hipotéticos, un caso corporativo delimitado y preguntas de MEE para revisar qué compartir y quién responde por ello.',
        sources=[
            source('Covirán · información para asociados', 'https://unete.coviran.es/',
                   'HTML oficial archivado y pasajes web visibles40–68 leídos. Cooperativa de minoristas independientes; servicios de logística, asesoramiento y formación. Descripción corporativa, sin comparación independiente, tarifas, contrato completo, resultados o rentabilidad verificados. No se utilizan cifras variables de tiendas/plataformas/asociados de otras páginas.',
                   'Presentación corporativa de su modelo y servicios; sin verificar resultados para un negocio particular.'),
            source('EUIPO · tipos de marcas', 'https://www.euipo.europa.eu/es/trade-marks/before-applying/types-of-trade-marks',
                   'Pasajes primarios devueltos por búsqueda oficial sobre marca colectiva: productos/servicios de miembros de la asociación titular. Acceso directo403 registrado; no lectura íntegra del HTML. Ámbito de la Unión Europea, sin trámites, tasas, plazos ni garantía de calidad o protección automática.',
                   'Definición de marca colectiva en pasajes oficiales recuperados por búsqueda; marco de la Unión Europea.'),
            source('EUIPO · indicaciones geográficas', 'https://www.euipo.europa.eu/es/gi-hub',
                   'Pasajes primarios devueltos por búsqueda de EUIPO: vínculo con origen geográfico, condiciones y distinción respecto de un signo informal. Acceso directo403 registrado; no página íntegra. Sin casos particulares ni procedimientos/tasas/fechas o certificaciones vigentes atribuidas a la ilustración.',
                   'Pasajes oficiales sobre origen y condiciones; sin revisión de una indicación geográfica concreta.'),
            source('Elinor Ostrom · conferencia Nobel · 2009', 'https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf',
                   'PDF primario37 páginas archivado; SOLO página PDF15/impresa422 leída y render inspeccionado en esta revisión. Límites, participación, seguimiento y resolución de conflictos en instituciones de recursos comunes. No lectura íntegra ni de Governing the Commons1990; no validación causal de redes comerciales. MEE adapta preguntas para un servicio compartido, no atribuye a Ostrom una receta empresarial.',
                   'Página15 del PDF, principios sobre instituciones de recursos comunes; aplicación comercial propuesta por MEE.')],
        omitted=['Sin ahorro o descuento garantizado ni resultados económicos de Covirán.', 'La ilustración no es sello, certificación o marca registrada.', 'No texto completo de EUIPO obtenido: se documenta acceso403 y lectura de pasajes primarios de búsqueda.', 'Sin validación de redes empresariales atribuida a Ostrom.']),
    'E6.7.14': dict(
        seo_title='Escalar en Cuba: tamaño, reforma y acuerdos revisables | MEE',
        description='Escalar en Cuba: la reforma de 2026 reconoce empresas privadas de más de cien personas. MEE distingue clasificación, capacidad y acuerdos por revisar.',
        keyword='escalar en Cuba',
        secondary=['Decreto-Ley133/2026', 'mipymes', 'empresas privadas', 'cooperación empresarial'],
        standfirst='Escalar en Cuba: el tema del plan editorial actualizado con los apartados oficiales revisados de 2026, ejemplos hipotéticos y preguntas sobre capacidad y acuerdos.',
        sources=[
            source('Gaceta Oficial · edición ordinaria71 · Decreto-Ley133/2026', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o71_0.pdf',
                   'PDF oficial200 de398346B/34 páginas, SHA en archivo access. Publicación2sept2026, decreto-ley19agosto2026. Leídos PDF1–4 y19, referencias impresas2083–2086 y2101; PDF20 extraído como contexto pero no utilizado. Art2 modifica clasificación por personas ocupadas incluidos socios, añade privada superior100. Disposición final séptima fija siete días posteriores a publicación. No lectura íntegra del PDF/ordenamiento ni aprobación de operación particular. Se evita repetir una referencia cruzada discordante de la edición concordada.',
                   'Páginas1–4 y19: reforma de clasificación y vigencia. Consulta de apartados, sin auditoría completa del ordenamiento.'),
            source('Gaceta Oficial · edición especial12 · texto anotado y concordado', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-es12.pdf',
                   'PDF oficial200 de461810B/57 páginas,7sept2026, GOC2026-496-ES12. Leídas PDF1–3, página3 render inspeccionado: artículo4 micro1–10/pequeña11–35/mediana36–100/privada>100, incluidos socios; artículo6 contratación entre actores reconocidos bajo disposiciones aplicables. Texto4 extraído sin declarar lectura. No todo el texto ni expediente individual ni fuente para burlar requisitos. Primera página contiene remisión a disposición final segunda del DL133 que no se utiliza: la orden de concordar figura en final sexta del original.',
                   'Páginas1–3: versión concordada, categorías y artículo6 sobre contratación bajo las disposiciones aplicables.')],
        omitted=['Premisa antigua del brief:100 no es un techo general de toda empresa privada tras la reforma consultada.', 'No elusión por multiplicar entidades ni legitimación automática de contratos o actividades.', 'Sin efectos medidos sobre competencia o concentración: argumento normativo identificado.', 'No asesoramiento sobre permisos concretos ni certificación exhaustiva de todas las normas.'])
}
for ident, m in metadata.items():
    print(ident, len(m['seo_title']), len(m['description']))
    assert 50 <= len(m['seo_title']) <= 60
    assert 140 <= len(m['description']) <= 155
path=Path(__file__).with_name('metadata732734.json')
assert not path.exists()
path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+'\n')
