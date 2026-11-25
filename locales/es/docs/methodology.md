# Método de ranking y alcance de la verificación

Se reutiliza el esquema de métricas recalculables de [awesome_bot](https://github.com/ZanePoe/awesome_bot), y el catálogo principal ordena por separado dentro de cada categoría. Software, skills y herramientas de evaluación no son la misma clase de producto: la puntuación de mantenimiento no se usa como clasificación general de resultados de escritura.

## Datos crudos

A través de la API GraphQL de GitHub se leen `stargazerCount`, el SHA y las fechas de la rama predeterminada, los conteos de commits a 30/90 días, el estado de archivo y el resultado de identificación de licencia. Los datos completos recolectados se guardan en `data/metrics.json`, y la primera instantánea se conserva aparte para poder rastrearla.

`commits_30d` y `commits_90d` usan `history.totalCount` del historial de la rama predeterminada, con el inicio y el final de la ventana fijados al mismo instante de recolección UTC. No se confunde el número de commits de la primera página con el total de commits.

La última actualización usa el `committedDate` del HEAD de la rama predeterminada. `pushed_at` y `updated_at` se guardan aparte, pero no se hace pasar un cambio de metadatos del repositorio ni un push de otra rama por una actualización de la rama predeterminada. La rama predeterminada no siempre se llama main, y las ramas experimentales se cuentan tal cual y se indican.

`latest_release` registra el nodo de release creado más recientemente y si es un pre-lanzamiento. Una skill sin releases no se declara por eso abandonada.

## Capas de mantenimiento y fórmula

Primero se agrupa en cuatro capas: con commits en la rama predeterminada en los últimos 90 días; sin commits desde hace 91–365 días; sin commits desde hace más de 365 días; archivado, disabled o proyecto claramente histórico.

Dentro de cada capa, la puntuación combinada:

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
Puntuación_de_mantenimiento = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Las estrellas pesan 40%, la actividad de commits a 90 días 35% y la frescura 25%. Los logaritmos y los topes reducen la ventaja de los proyectos gigantes; los anclajes fijos hacen que una entrada nueva no cambie la puntuación de las antiguas. En caso de empate se comparan las estrellas y luego se ordena establemente por nombre de repositorio.

[Las vistas de ranking](rankings.md) ofrecen a la vez la puntuación combinada, las estrellas, la actividad a 90 días y el último commit; todas agrupan primero por capa de mantenimiento. Para ordenar solo por los valores crudos, usa [el CSV](../../../data/rankings.csv).

## Limitaciones

El volumen de commits incluye fusiones, bots y actualizaciones de documentación, y la actividad total de un monorepo tampoco equivale a la actividad del módulo de novela. Una skill con reglas estables puede cometer muy poco, así que una puntuación baja de actividad no implica que sea inválida. Un proyecto nuevo puede tener muchos commits y pocos usuarios; uno antiguo puede acumular muchas estrellas con poco mantenimiento actual.

Esta ronda verificó la documentación del repositorio, las fronteras de versión, la licencia y los metadatos de GitHub; no se instaló todo el software ni se ejecutó una prueba de escritura uniforme. De aquí no puede afirmarse que un proyecto sea el que mejor escribe novelas, que mantenga de forma estable la calidad de un millón de palabras o que aumente los ingresos de un contrato editorial.

Para una evaluación de capacidad haría falta fijar modelo, presupuesto, tema de historia, longitud objetivo y versión, y comparar consistencia de la ambientación, comportamiento de los personajes, cumplimiento de los presagios, nivel de repetición, cantidad de revisión humana y coste de generación. Las cifras que los autores informan por su cuenta sobre "millones de palabras" o "mejoras por multi-agente" no se mezclan directamente con las de otros proyectos.

## Actualización y gestión de fallos

El refresco de métricas depende de la sesión de `gh` o de `GH_TOKEN`. La instantánea se reemplaza de forma atómica solo cuando todos los lotes terminan; si la API falla parcialmente, un repositorio queda inaccesible o no tiene rama predeterminada, se conserva el archivo anterior y la tarea se marca como fallo, para no escribir un cero donde hay desconocimiento.

Las funciones y las licencias son datos revisados a mano, con su propia fecha de verificación y fuentes fijadas a un commit. El refresco diario solo actualiza métricas: no confirma funciones nuevas ni reinterpreta licencias. Los cambios de nombre, las eliminaciones y los cambios de licencia requieren una nueva revisión del mantenedor.
