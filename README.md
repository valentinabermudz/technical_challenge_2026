# Technical Challenge – Intern Program 2026

## Ejercicio B – The Library's Lost Books
Lee un archivo CSV con registros de libros y genera un catálogo limpio y deduplicado.

### Salida
- `books_clean.csv` — catálogo limpio y deduplicado, ordenado por autor y año de publicación.
- `report.md` — resumen con estadísticas y estrategia de deduplicación.

### Decisiones de diseño
- Los libros sin título son descartados.
- Los autores faltantes se marcan como `Author Unknown`.
- Los años inválidos (negativos, futuros o no numéricos) se reemplazan por `0`.
- La deduplicación agrupa por título normalizado y resuelve duplicados en base al autor y año de publicación.


## Ejercicio C – Análisis de Frecuencia de Palabras
Lee un archivo de texto y muestra las 10 palabras más frecuentes sin distinción entre mayúsculas y minúsculas y sin
considerar signos de puntuación y caracteres especiales.

### Salida
Imprime por consola las 10 palabras más frecuentes y su cantidad de apariciones.
