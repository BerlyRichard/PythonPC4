
from pyfiglet import Figlet
import random

def fuenteFi():
    figlet = Figlet()
    fonts = figlet.getFonts()

    while True:
        fuente = input("Ingrese el nombre de una fuente (deje en blanco para elegir una aleatoriamente): ").strip()
        if fuente == "":
            fuente = random.choice(fonts)  
            break
        elif fuente in fonts:
            break
        else:
            print("Error. Fuente no válida. Elija una fuente de la lista proporcionada.")

    text = input("Ingrese un texto: ")

    figlet.setFont(font=fuente)

    print(figlet.renderText(text))

if __name__ == "__main__":
    try:
        fuenteFi()
    except Exception as e:
        print("Se ha producido un error:", e)