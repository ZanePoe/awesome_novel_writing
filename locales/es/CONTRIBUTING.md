# Guía de contribución

Se aceptan nuevos proyectos, correcciones de categoría y evidencia adicional de versiones y licencias. Tener pocas estrellas no es motivo de rechazo.

1. Modifica `data/projects.json`; no edites a mano las tablas generadas del README.
2. Aporta la dirección canónica de GitHub, el uso, la forma del proyecto, su frontera de aplicación y los enlaces de evidencia fijados a un commit.
3. Elige una sola categoría principal. Las herramientas generales adyacentes deben explicar su relación con la novela; no mezcles software, skills y bancos de investigación.
4. Distingue lo ya implementado, la vista previa en desarrollo y la hoja de ruta. Los resultados del modelo, los objetivos de palabras y las métricas autoinformadas por el autor no pueden redactarse como conclusiones verificadas de forma independiente.
5. Verifica la licencia; las notas comerciales adicionales y las brechas de licencia deben conservarse. Que algo sea público no equivale automáticamente a MIT.
6. Las forks o los puertos se incluyen aparte solo cuando existe una diferencia explicable de anfitrión, funciones o ruta de mantenimiento, y se documenta la relación con el origen.
7. Tras añadir un proyecto, vuelve a obtener la instantánea completa de métricas y regenera los documentos:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

`data/seed-references.json` registra los proyectos de referencia iniciales y normalmente no cambia con las contribuciones ordinarias. Cada verificación manual de funciones debe actualizar la fecha y el commit de evidencia; el refresco automático de estrellas no toca esos campos.

No envíes claves de modelos, direcciones de búsqueda privadas, manuscritos no publicados ni textos internos de artículos. Los resúmenes de investigación se guardan en `record/YYYY-MM-DD-título-en-chino.md`.

## Archivos multilingües

- `data/projects.json` es el dato de revisión canónico en chino: los hechos solo se cambian una vez, aquí.
- En los demás idiomas, el texto viene de `locales/<lang>/entries.json` (`description`, `form`, `boundary`, `license_label`, `license_note`) y de `locales/<lang>/ui.json`; `zh` recae directamente en `data/projects.json`, por eso no existe `locales/zh/entries.json`.
- Al añadir un proyecto o reformular su presentación, sus fronteras o sus conclusiones de licencia, el mismo PR debe completar los cuatro locales en/es/hi/fr; si no, `python scripts/build.py --check` y `python -m unittest discover -s tests -v` fallarán.
- Documentos estáticos: el inglés está en `docs/` y `CONTRIBUTING.md` en la raíz; los demás idiomas, en las mismas rutas relativas bajo `locales/<lang>/`. Los enlaces relativos de un espejo se resuelven desde el directorio del archivo; apuntar desde el espejo a `data/`, `scripts/`, `research/`, `LICENSE` o `record/` de la raíz del repositorio requiere `../../`; `docs/readme-intro.md` es la excepción: se inserta en el README y resuelve desde la raíz del idioma.
- `record/` y `research/` conservan el texto original con el que se redactaron, como huella de auditoría; no se traducen automáticamente.
- Los artefactos generados (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` y sus homólogos en cada espejo de idioma) no se editan a mano: los produce `python scripts/build.py`.
