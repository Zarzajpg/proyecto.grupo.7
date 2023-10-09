#Proyecto G 7 
#Alumnos:Zarza, Juan Pablo

# Lista de palabras predefinidas
palabras = ["informatorio", "septima", "programacion", "boquita", "libertadores", "chiquito"]

# Función para seleccionar una palabra aleatoria
def seleccionar_palabra():
    return random.choice(palabras)

# Función para inicializar el juego
def iniciar_juego():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
