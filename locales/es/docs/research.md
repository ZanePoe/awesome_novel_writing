# Registro de búsqueda y decisiones de inclusión

El 2026-11-05 se completó la primera versión: 41 proyectos, 6 categorías, con los 13 proyectos de referencia deduplicados cubiertos en su totalidad. El 2026-11-06 se añadió Reveric por indicación del usuario; actualmente son 42 proyectos y 14 referencias. Esta ronda se centró en proyectos e implementaciones, sin expandir los artículos relacionados hacia una lista propia de papers.

## Ejes de búsqueda derivados de los proyectos de referencia

| Dirección | Palabras clave en inglés | Palabras clave en chino |
| --- | --- | --- |
| Herramientas completas de creación | AI novel writer, writing workspace, fiction IDE, local-first | AI 小说写作、小说工作台、桌面码字软件 |
| Automatización de novela larga | long-form fiction, writing agent, novel generator, harness | 长篇生成、分章写作、写作 Agent |
| Estado y continuidad | story bible, character state, foreshadowing, continuity, RAG | 世界观、人物状态、伏笔、连贯性、长期记忆 |
| Recursos para agentes | novel writing skill, workflow, prompt framework | 小说 Skill、网文技能、方法框架 |
| Revisión | narrative revision, humanizer, style lint, editing | 叙事修复、去模板化、文风、审稿 |
| Adaptación | screenplay, short drama, story adaptation, narration | 剧本、短剧、小说改编、影视解说 |

## Tres rondas de búsqueda

| Ronda | Lotes | Resultados | Fuentes nuevas | Tasa de fuentes nuevas |
| --- | --- | --- | --- | --- |
| 1 | 15 | 331 | 300 | 90.6% |
| 2 | 4 | 127 | 90 | 70.9% |
| 3 | 3 | 17 | 15 | 88.2% |

En total, 22 lotes de búsqueda o verificación: búsquedas web, búsqueda nativa de GitHub, recolección de enlaces de directorios curados y verificación en lote de repositorios y métricas. El número de fuentes cuenta URLs del registro de búsqueda, no proyectos incluidos, y cada candidato no resultaba relevante por necesidad.

La primera ronda partió de todos los proyectos de referencia y cubrió ocho direcciones: definición, fuente original, directorios curados, repositorio, comparaciones, evaluaciones, fronteras y cambios recientes. Buscar `小说` en GitHub mezcla lectores, descargadores, CMS y listas de libros, que se descartan según el objetivo de creación; `easy-writing` también mezcla un framework de desarrollo homónimo, y no basta con el puesto en los resultados de búsqueda para incluir.

La segunda ronda incorporó las líneas de Oh Story, webnovel-writer, NovelClaw y OpenFic, entre otras, leyendo los README oficiales para distinguir aplicaciones, skills y metodologías. Los directorios curados sirven para descubrir pistas, no para copiar sus estrellas, información de conferencias o conclusiones de efectividad.

La tercera ronda verificó cambios de nombre, excepciones de licencia y el README en chino de Sepia aportado por el usuario, e incorporó Long-Novel-GPT. Las métricas de los proyectos finales se recolectaron de forma uniforme vía GitHub GraphQL, con las fuentes funcionales fijadas a un commit.

La razón de parada fue el límite de tres rondas establecido de antemano, no «haber agotado la búsqueda»; la tercera ronda aún produjo hallazgos. Los géneros verticales, la ficción interactiva, la traducción, los modelos de escritura locales y todas las herramientas industriales de drama corto no se han explorado por completo. Las herramientas puras de lectura, recolección o publicación de novelas no se metieron a la fuerza en la lista como si fueran de escritura.

## Proyectos de referencia, nombres y deduplicación

| Nombre del usuario / nombre antiguo | Inclusión actual |
| --- | --- |
| Denova | [alfredxw/denova](https://github.com/alfredxw/denova) |
| 易创 easy-writing | [yilujian/easy-writing](https://github.com/yilujian/easy-writing) |
| ai-juben | [VanGong1999/juben](https://github.com/VanGong1999/juben), confirmado por el usuario |
| AI Novel Writer | [书童 Pagekin](https://github.com/EthanYoQ/Pagekin), repositorio renombrado; la dirección antigua redirige automáticamente |
| AI Novel Writing Assistant | [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant), mismo repositorio |
| Storyteller | [Dankular/Storyteller](https://github.com/Dankular/Storyteller), el README actual lo llama novel-harness |
| Sepia duplicado y `-g` | Un solo elemento para el mismo repositorio; la skill no se instaló |

Todos los mapeos de semillas están en [seed-references.json](../../../data/seed-references.json). El repositorio canónico es la clave de deduplicación; renombrar un repositorio no añade un proyecto. El puerto de OpenCode figura aparte por las diferencias de anfitrión y funciones, con su relación con el upstream explicada; las forks sin diferencia declarada de contenido no se incluyen.

## Correcciones sobre la documentación original

- [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) se centra de forma explícita en artículos e hilos en chino y la ficción pura sigue requiriendo un método propio, así que queda clasificada como herramienta de revisión adyacente.
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) guía el uso de una CLI de narración audiovisual y no se describe como generador original de novela larga.
- [NeuroBook](https://github.com/notnotype/neuro-book) está reconstruyendo su v2 actual y parte de las capacidades del estudio de IA figuran en la hoja de ruta; la entrada conserva la frontera de versión previa.
- [Novel Studio](https://github.com/bbaz123/novel-studio) tiene una línea experimental como rama predeterminada; las métricas se toman efectivamente de esa rama, sin forzar la main antigua.
- [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT) sigue listando como planes parte de sus capacidades de libro completo con un clic; el eslogan de portada no equivale a una aceptación completada.
- [Reveric](https://github.com/looplj/reveric) tiene `unstable` como rama predeterminada actual, y el catálogo la verifica. Su archivo `NOTICES` exige, al amparo de la Sección 7 de AGPLv3, que las versiones modificadas conserven la firma del proyecto y el enlace, y ofrece además una vía de licencia comercial.

## Verificación de licencias

La identificación SPDX de GitHub y la comprobación manual de excepciones se guardan por separado. El LICENSE de Biz Novel Studio incluye a la vez la AGPL y notas de autorización comercial para el servicio; el LICENSE de Kimi Writer es un texto con condiciones adicionales de atribución comercial. Ambos conservan el enlace al original y no se simplifica su registro a un AGPL/MIT ordinario.

Agnes declara explícitamente la ausencia de licencia; varios harnesses de escritura, skills y repositorios de evaluación pequeños no permitieron localizar una licencia completa. Una insignia del README o una frase «MIT» no bastan para marcarlas automáticamente como licencia verificada. El estado concreto está en [la tabla de proyectos](projects.md). Este catálogo registra las condiciones del autor y no otorga garantías de uso comercial entre proyectos.

## Content factory

Se reutilizó `content-factory-search-api`, llamando a la búsqueda estructurada mediante curl; intervalo de fechas **2026-08-05 a 2026-11-05**, consultas `小说` y `inkos OR sepia OR 小说写作`. Ambas devolvieron un JSON correcto, pero con el array de resultados vacío. No se ejecutó una búsqueda de historial completo, y el resultado vacío no se interpreta como que esos proyectos no existan.

Sin contenido devuelto no se realizó ningún cálculo vectorial. La inclusión final se basa en los repositorios originales de GitHub; las direcciones de búsqueda privadas, las claves y los textos internos no entran en el repositorio público.

## Verificación y limitaciones

Las descripciones funcionales se apoyan en la documentación oficial; no se instalaron ni ejecutaron todos los programas ni se hizo una evaluación ciega con modelo, presupuesto y temas de historia uniformes. Las afirmaciones de los autores sobre número de capítulos, millones de palabras, eliminación del toque de IA y ventajas multi-agente no alimentan ninguna clasificación de capacidad. Esta ronda no incluyó experimentos de ablación por componente, así que no puede decirse «cuánto baja la calidad al quitar la memoria».

Se completaron la comprobación de integridad de proyectos/semillas, las pruebas de fronteras del ranking, la prueba de conservación de la instantánea anterior ante fallo de API y la comprobación de consistencia de los archivos generados. El detalle de las métricas está en [methodology.md](methodology.md).

Materiales de auditoría públicos:

- [Registro de búsqueda](../../../research/search-log.json): consultas, rondas y estadísticas de resultados.
- [Decisiones de inclusión](../../../research/decisions.json): uso, fronteras, commits fijados y verificación de licencias.
- [Cobertura de referencia](../../../research/coverage.json): los 14 enlaces de referencia cubiertos en su totalidad.
- [Métricas iniciales](../../../research/initial-metrics.json) y [métricas actuales](../../../data/metrics.json): la toma inicial y las actualizaciones continuas separadas.
- [Estado](../../../research/status.json) y [resultado de integridad](../../../research/verification.json): razón de parada y resultados vacíos conocidos.

Los textos fuente completos y los registros de herramientas se quedan en local. Las estadísticas públicas de investigación contienen 84 juicios y 123 métricas, verificables a través de las decisiones y las instantáneas anteriores.
