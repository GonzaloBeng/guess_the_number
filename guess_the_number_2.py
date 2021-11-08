import random as rm #Importe para conseguir el numero random

""" Computadora adivina un numero generado por el usuario """


def guess_the_number(x):

    print('========================')
    print('= Bienvenid@! al Juego!=')
    print('========================')
    print(f'Ingresa un numero entre 1 y {x} para que la computadora lo adivine.')

    limite_inf = 1
    limite_sup = x

    respuesta = ''

    while respuesta != 'c':
        # Generamos la prediccion del numero

        if limite_inf != limite_sup:
            prediccion = rm.randint(limite_inf, limite_sup) # Es decir 1 y X pero va descartando a medida que avanza
        else:
            prediccion = limite_inf #Podrian ser iguales
        
        # Consultar al usuario el resultado
        respuesta= input(f'''Mi prediccion es {prediccion}. 
Si es muy alta escribe (A), muy baja (B) y si es correcta (C).
''').lower()

        if respuesta == 'a':
            limite_sup = prediccion - 1
        elif respuesta == 'b':
            limite_inf = prediccion + 1
    
    print(f'La computadora adivino el numero correctamente!. El numero: {prediccion}.')


guess_the_number(20)