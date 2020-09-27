import numpy as np
import prettytable
import random


class Environment():    
    def __init__(self):
        self.width = 0
        self.height = 0
        self.matrix = None
        self.table = None
        self.vacuum = None

    def createRandom(self):
        self.width = random.randint(0, 25)
        self.height = random.randint(0, 25)        
        self.matrix = np.random.randint(0,2, size = (self.width, self.height))
        
        for row in matrix:
            table.add_row(row)
        
        self.vacuum = VacuumCleaner(self.width, self.height)

    def createCustom(self):
        gridWidth = 0
        gridHeight = 0
        
        while True:
            try:
                gridWidth = int(input("Ingrese la altura del ambiente: "))
                gridHeight = int(input("Ingrese la anchura  del ambiente: "))
                print("Ingrese la posición inicial de la aspiradora en")
                vcX = int(input("X: "))
                vcY = int(input("Y: "))
                
            except ValueError:
                print("Solo enteros! intente de nuevo.")
                continue
            else:
                if gridWidth <= 0 or gridHeight <= 0:
                    print('ERROR: Ingrese valores validos')
                else:
                    break

class VacuumCleaner():
    def __init__(self, width, height):
        # Vacuum position
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        
        # Vacuum preformance
        self.energyUsed = 0
        self.sensorIterations = 0
        self.dirtDetected = 0

        self.sensors = {'up': False, 'down': False,  'left': True, 'right': True}
        
    def create(self):
        pass

    def move(self):
        pass

    def clean(self):
        pass


def main():
    """
    docstring
    """
    env = Environment()
    env.create()

    menu()


def menu(env):
    print("Bienvenido al entorno de aspiradora. Escoge una opción: ")
    print("/t 1. Ambiente aleatorio")
    print("/t 2. Ambiente personalizado")
    
    opt = int(input('Ingrese una opcion'))
    if opt == 1:
        env.createRandom()
    elif opt == 2:
        env.createCustom()
    else:
        print("Opción no válida, escoge de nuevo")
        opt = int(input())
        menu()


if __name__ == "__main__":
    main()
