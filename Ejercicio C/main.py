from collections import Counter
import re
import unicodedata 

def read_text(file_path):
    "Lee un archivo de texto y devuelve una lista de líneas."
    try: 
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return []


def clean_text(text):
    "Limpia el texto eliminando caracteres especiales, tildes y convirtiendo a minúsculas."
    text = text.lower()

    text = unicodedata.normalize("NFD", text)
    text = ''.join(c for c in text if unicodedata.category(c) != "Mn")
    
    text = re.sub(r'[^a-z0-9ñ\s]', '', text)
    return text


def main():
    file_path = "texto.txt"
    text = read_text(file_path)
    text = clean_text(text)
    
    word_count = Counter(text.split())

    # Si quisieramos filtrar palabras de 3 o más caracteres para evitar palabras comunes como "el", "la", "de", etc.
    # word_count = Counter(w for w in text.split() if len(w) > 2)

    print("Las 10 palabras más comunes y sus frecuencias son:")
    for word, count in word_count.most_common(10):
        print(f"- {word}: {count}")


if __name__ == "__main__":
    main()