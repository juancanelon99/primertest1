import sys

def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")
        return
    words = text.split()
    print(len(words))

if __name__ == "__main__":
    filepath = 'capitulo1.txt' if len(sys.argv) == 1 else sys.argv[1]
    count_words(filepath)
