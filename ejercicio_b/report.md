
# Reporte de Limpieza y Deduplicación

- Total de libros en el archivo original: 44
- Total de libros después de la limpieza y deduplicación: 23
- Libros descartados por falta de información: 3
- Libros corregidos por datos faltantes o inválidos: 16
- Libros duplicados detectados y eliminados: 18

## Detalles de las Estadísticas

- El número total de libros en el archivo original es la cantidad de filas leídas del CSV que tienen 3 columnas válidas.
- El total de libros después de la limpieza y deduplicación es la cantidad de libros que se escriben en el archivo limpio, después de eliminar duplicados.
- Los libros descartados son aquellos que no tienen un título válido después de la limpieza.
- Los libros corregidos son aquellos que tuvieron datos faltantes o inválidos que fueron corregidos durante la limpieza, como años de publicación no válidos o autores faltantes.
- Los libros duplicados son aquellos que fueron identificados como iguales durante el proceso de deduplicación y se eliminaron del resultado final.

## Estrategia de deduplicación

Los libros se agrupan por título y dentro de cada grupo se aplica la siguiente lógica:
- Mismo autor: se consideran el mismo libro, se conserva el registro con más información completa.
- Autores distintos conocidos: se consideran libros diferentes, se conservan ambos.
- Un autor conocido y uno desconocido con el mismo año: se consideran el mismo libro, se conserva el registro con autor conocido.
- Un autor conocido y uno desconocido con distinto año: se consideran libros diferentes, se conservan ambos.
