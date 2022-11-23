

import random 





pruebas=int(input('Ingrese la cantidad de veces que desee jugar: '))
while pruebas!=0:
    maquina=random.randint(1,3)
    if maquina==1:
        eleccion='Piedra'

    elif maquina==2:
        eleccion='Papel'

    elif maquina==3:
        eleccion='Tijera'
    
    opcion=int(input('''
    Menu de opción
    
    1.Piedra
    2.Papel
    3.Tijera
    
    Elija su opción:'''))
    if maquina==opcion:
        print('')
        print(f'Empate!! Tú y la maquina sacaron {eleccion}')
        pruebas-=1

    elif maquina==1 and opcion==2 or maquina==2 and opcion==3 or maquina==3 and opcion==1:
        print('')
        print(f'1 punto para tí, la maquina sacó {eleccion}')
        pruebas-=1

    else:
        print('')
        print(f'Punto para la maquina, la maquina sacó {eleccion}')
        pruebas-=1


