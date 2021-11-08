import random as rm

""" Usuario adivina un numero generado por la computadora """

def guess_the_number(x):

    print('========================')
    print('= Bienvenid@! al Juego!=')
    print('========================')
    print('Debes adivinar el numero generado por la computadora.')

    numero_aleatorio = rm.randint(1,x) #Numero aleatorio entre 1 y X inclusive.

    prediccion = 0 #Es 0 para que no coincida con el numero aleatorio.

    while prediccion != numero_aleatorio:
        #Ingreso de numero del usuario

        prediccion = int(input(f'Adivina un numero entre 1 y {x}: '))
        if prediccion < numero_aleatorio:
            print('Intenta otra vez, con un numero mas alto.')
        elif prediccion > numero_aleatorio:
            print('Intenta otra vez, con un numero mas bajo.')
        
    print(f'Has adivinado el numero!, el numero era {numero_aleatorio}.')


guess_the_number(20)