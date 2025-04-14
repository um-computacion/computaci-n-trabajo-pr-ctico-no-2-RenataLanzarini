import re

def is_palindrome(text):
    """Detecta si una palabra o frase es un palíndromo."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1] 


if __name__ == "__main__":
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo\n')
            else:
                print(f'"{entrada}" no es un palíndromo\n')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")


