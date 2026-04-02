from utils import validate_year

def clean_book(book):
    """Limpia y normaliza los datos de un libro.
    Devuelve un libro limpio si es valido, o None si debe ser descartado
    """

    # Si el nombre del libro es faltante, lo descartamos
    title = (book.get("Title") or "").strip()
    if not title:
        return None

    # Si el autor es faltante, lo marcamos como 'Author Unknown'
    author = (book.get("Author") or "").strip()
    if not author:
        author = "Author Unknown"
    
    # Si el año de publicación es inválida, la marcamos como '0'
    if not validate_year(book.get("PublicationYear")):
        pub_year = 0
    else:
        pub_year = int(book.get("PublicationYear"))


    return {
        "Title": title,
        "Author": author,
        "PublicationYear": pub_year,
    }

