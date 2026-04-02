from utils import read_csv, write_csv, sort_books
from cleaner import clean_book
from deduplicator import deduplicate
from report import generate_report

INPUT_FILE = "books.csv"
OUTPUT_FILE = "books_clean.csv"

def main():
    """Función principal que ejecuta el proceso de limpieza, deduplicación y generación de reportes."""
    books = read_csv(INPUT_FILE)
    total_input = len(books)

    cleaned_books = []
    discarded = 0
    corrected = 0

    for book in books:
        cleaned = clean_book(book)

        if cleaned is None:
            discarded += 1
            continue
        
        if (str(book["PublicationYear"]) != str(cleaned["PublicationYear"]) or
            cleaned["Author"] == "Author Unknown"
        ):
            corrected += 1

        cleaned_books.append(cleaned)
    
    
    final_books = sort_books(deduplicate(cleaned_books))
    
    duplicates = total_input - discarded - len(final_books)
    total_output = len(final_books)

    write_csv(final_books, OUTPUT_FILE)
    generate_report(total_input, total_output, discarded, corrected, duplicates)


if __name__ == "__main__":
    main()