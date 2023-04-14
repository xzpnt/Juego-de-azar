import random
import keyboard

Palabras = ['*', '<', '|', '#', '>']

Vidas = 3
Puntaje = 1
Check = None


while Vidas > 0:
    print("Presiona la tecla 'p' para jugar")
    keyboard.wait('p')
    Generar = random.sample(Palabras, 3)
    print(" ".join(Generar))

    if Check is not None and len(set(Generar).intersection(set(Check))) >= 2:
        Vidas += 1
        print("Ojo parece que..")
    else:
        if len(set(Generar)) == 1 and Generar[0] == Generar[1] == Generar[2]:
            print("Increible!")
            break
        elif len(set(Generar)) == 1:
            print("Buena suerte!")
        else:
            print("Estaba claro...")
            Vidas -= 1
            if Vidas == 0:
                print("Normal...")
        


Check = Generar   