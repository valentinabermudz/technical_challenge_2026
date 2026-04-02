from utils import normalize_text

def best_book(book1, book2):
    """Determina cuál de los dos libros es de mejor calidad para mantenerlo en 
    caso de duplicado.
    """
    def get_quality_score(book):
        return (
            book["Author"] != "Author Unknown",
            book["PublicationYear"] != 0
        )

    if get_quality_score(book2) > get_quality_score(book1):
        return book2
    return book1


def deduplicate(books):
    """Agrupa libros por título y resuelve duplicados basándose en autor y año de 
    publicación.
    """
    groups = {}

    for book in books:
        key = normalize_text(book["Title"])
        if key not in groups:
            groups[key] = []
        groups[key].append(book)

    final_books = []
    for key, group in groups.items():
        final_books.extend(resolve_group(group))

    return final_books


def resolve_group(group):
    """Resuelve un grupo de libros con el mismo título, 
    determinando cuáles son duplicados y cuál es el mejor para mantener.
    """
    resolved = []

    for book in group:
        merged = False
        for i, existing in enumerate(resolved):

            same_author = normalize_text(book["Author"]) == normalize_text(existing["Author"])
            one_is_unknown = book["Author"] == "Author Unknown" or existing["Author"] == "Author Unknown"
            same_year = book["PublicationYear"] == existing["PublicationYear"]

            if same_author:
                resolved[i] = best_book(existing, book)
                merged = True
                break
            elif one_is_unknown and same_year:
                resolved[i] = best_book(existing, book)
                merged = True
                break

        if not merged:
            resolved.append(book)

    return resolved

