from datetime import datetime
import csv

def validate_year(year):
    """Valida que el año de publicacion no sea faltante, negativo, 
    en el futuro o string
    """
    if year is None:
        return False
    try:
        year = int(year)
        current_year = datetime.now().year
        if year < 0 or year > current_year:
            return False
        return True
    except ValueError:
        return False


def normalize_text(text):
    """Normaliza el texto eliminando espacios extra y convirtiendolo a minúsculas."""
    if not text:
        return ""
    return " ".join(str(text).strip().lower().split())


def sort_books(books):
    """Ordena los libros por autor y por año de publicación."""
    return sorted(books, key=lambda b: (
        b["Author"] == "Author Unknown",
        normalize_text(b["Author"]),
        b["PublicationYear"] == 0,
        b["PublicationYear"]
    ))


def read_csv(file_path):
    books = []

    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 3:
                    print("Fila con número incorrecto de columnas:", row)
                    continue

                book = {
                    "Title": row[0],
                    "Author": row[1],
                    "PublicationYear": row[2],
                }
                books.append(book)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")

    return books


def write_csv(books, file_path):
    """Escribe una lista de libros en un archivo CSV."""
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f,
                                fieldnames=["Title", 
                                            "Author", 
                                            "PublicationYear"])
        writer.writeheader()
        writer.writerows(books)