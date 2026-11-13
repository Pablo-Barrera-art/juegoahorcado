# Lista con las 7 etapas del dibujo (desde 6 vidas hasta 0 vidas)
HANGMAN_STAGES = [
    # 0 Vidas restantes (Ahorcado completo - Perdió)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    # 1 Vida restante
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 2 Vidas restantes
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 3 Vidas restantes
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 4 Vidas restantes
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 5 Vidas restantes
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 6 Vidas restantes (Inicio - Horca vacía)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

def get_hangman_art(lives):
    """Devuelve el dibujo según la cantidad de vidas (0 a 6)."""
    return HANGMAN_STAGES[lives]