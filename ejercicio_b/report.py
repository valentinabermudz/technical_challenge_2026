def generate_report(total_input,
                    total_output,
                    discarded,
                    corrected,
                    duplicates,
                    file_path="report.md"):
    
    """Genera un informe con las estadísticas."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n# Reporte de Limpieza y Deduplicación\n\n")
        f.write(f"- Total de libros en el archivo original: {total_input}\n")
        f.write(f"- Total de libros después de la limpieza y deduplicación: {total_output}\n")
        f.write(f"- Libros descartados por falta de información: {discarded}\n")
        f.write(f"- Libros corregidos por datos faltantes o inválidos: {corrected}\n")
        f.write(f"- Libros duplicados detectados y eliminados: {duplicates}\n")

        f.write("\n## Detalles de las Estadísticas\n\n")
        f.write(f"- El número total de libros en el archivo original es la cantidad de filas leídas del CSV que tienen 3 columnas válidas.\n")
        f.write(f"- El total de libros después de la limpieza y deduplicación es la cantidad de libros que se escriben en el archivo limpio, después de eliminar duplicados.\n")
        f.write(f"- Los libros descartados son aquellos que no tienen un título válido después de la limpieza.\n")
        f.write(f"- Los libros corregidos son aquellos que tuvieron datos faltantes o inválidos que fueron corregidos durante la limpieza, como años de publicación no válidos o autores faltantes.\n")
        f.write(f"- Los libros duplicados son aquellos que fueron identificados como iguales durante el proceso de deduplicación y se eliminaron del resultado final.\n")

        f.write("\n## Estrategia de deduplicación\n\n")
        f.write(
            "Los libros se agrupan por título y dentro de cada grupo se aplica la siguiente lógica:\n"
            "- Mismo autor: se consideran el mismo libro, se conserva el registro con más información completa.\n"
            "- Autores distintos conocidos: se consideran libros diferentes, se conservan ambos.\n"
            "- Un autor conocido y uno desconocido con el mismo año: se consideran el mismo libro, se conserva el registro con autor conocido.\n"
            "- Un autor conocido y uno desconocido con distinto año: se consideran libros diferentes, se conservan ambos.\n"
        )
        
       