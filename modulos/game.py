# Modulos, comunicación entre distintos archivos de código.
# game.py
# import the draw module from draw.py
# import draw 
from draw import draw_game

def play_game():
    ...

# def main():
#     result = play_game()
#     draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
# if __name__ == '__main__':
#     main()
    
# Importando módulos objetos al espacio de nombre actual

# A namespace is a system where every object is named and can be accessed in Python.
# We import the function draw_game into the main script's namespace by using the from command.
# game.py



def main():
    result = play_game()
    draw_game(result)
    
# Importar todos los objetos de un módulo
# from draw import *

# Nombre personalización para la importación
# Podremos definir un nombre al objeto que importamos
# game.py
# import the draw module
# if visual_mode:
#     # in visual mode, we draw using graphics
#     import draw_visual as draw
# else:
#     # in textual mode, we print out text
#     import draw_textual as draw

# def main():
#     result = play_game()
#     # this can either be visual or textual depending on visual_mode
#     draw.draw_game(result)