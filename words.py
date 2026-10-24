import random

# Lista de palabras en mayúsculas para el juego
WORD_LIST = [
    "PYTHON", "PROGRAMACION", "DESARROLLO", "SOFTWARE", 
    "COMPUTADORA", "ALGORITMO", "VARIABLE", "FUNCION",
    "MATRICES", "REPOSITORIO", "LIBRERIA", "INTERFAZ"
]

def get_random_word():
    """Selecciona y retorna una palabra aleatoria de la lista."""
    return random.choice(WORD_LIST).upper()