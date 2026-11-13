from words import get_random_word
from display import get_hangman_art

def validate_input(user_input, used_letters):
    """
    Verifica que el usuario ingrese exactamente 1 letra, 
    que esté en el rango A-Z y que no se haya usado antes.
    """
    user_input = user_input.strip().upper()

    # 1. Validar que sea un solo carácter y sea una letra
    if len(user_input) != 1 or not user_input.isalpha():
        print("-> Debe ingresar solo 1 letra (A-Z).")
        return None
    
    # 2. Validar que no se haya usado previamente
    if user_input in used_letters:
        print("-> Ya ha utilizado la letra.")
        return None

    return user_input

def play_game():
    secret_word = get_random_word()
    guessed_word = ["_"] * len(secret_word)
    used_letters = set()
    lives = 6

    print("\n==========================================")
    print("      ¡BIENVENIDO AL JUEGO DEL AHORCADO!  ")
    print("==========================================\n")

    # Bucle principal del juego mientras tenga vidas y falten letras por adivinar
    while lives > 0 and "_" in guessed_word:
        print(get_hangman_art(lives))
        print(f"Vidas restantes: {lives}")
        print("Palabra: " + " ".join(guessed_word))
        
        if used_letters:
            print("Letras usadas: " + ", ".join(sorted(used_letters)))
        else:
            print("Letras usadas: Ninguna")
        
        inp = input("\nIngrese una letra: ")
        letter = validate_input(inp, used_letters)

        # Si la validación falla, se pide otra letra sin restar vidas
        if letter is None:
            print("-" * 40)
            continue

        used_letters.add(letter)

        # Verificar si la letra está en la palabra oculta
        if letter in secret_word:
            print(f"¡Correcto! La letra '{letter}' está en la palabra.")
            for idx, char in enumerate(secret_word):
                if char == letter:
                    guessed_word[idx] = letter
        else:
            lives -= 1
            print(f"La letra '{letter}' NO está en la palabra. Pierdes una vida.")
        
        print("-" * 40)

    # Resultado final al terminar el bucle
    if "_" not in guessed_word:
        print("\n" + "=" * 40)
        print(f"¡GANASTE! Adivinaste la palabra: {secret_word}")
        print("=" * 40)
    else:
        print("\n" + "=" * 40)
        print(get_hangman_art(0))
        print("¡HAS PERDIDO!")
        print("Vidas restantes: 0")
        print(f"La palabra oculta era: {secret_word}")
        print("=" * 40)

def main():
    while True:
        play_game()
        
        print("\n¿Deseas jugar de nuevo?")
        print("1. Volver a jugar")
        print("2. Finalizar (Terminar el programa)")
        
        choice = input("Seleccione una opción (1 o 2): ").strip()
        while choice not in ["1", "2"]:
            choice = input("Opción inválida. Ingrese 1 para volver a jugar o 2 para salir: ").strip()

        if choice == "2":
            print("\n¡Gracias por jugar! Hasta pronto.")
            break

if __name__ == "__main__":
    main()