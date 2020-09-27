import numpy as np
import prettytable
import random


class Environment():    
    def __init__(self):
        self.width = 0
        self.height = 0
        self.matrix = None
        self.vacuum = None
        self.world = None

    def createRandom(self):
        self.width = random.randint(1, 20)
        self.height = random.randint(1, 20)        
        self.matrix = np.random.randint(0,2, size = (self.width, self.height))

        self.world = prettytable.PrettyTable(header=False)
        for row in self.matrix:
            self.world.add_row(row)

        self.vacuum = VacuumCleaner(self.width, self.height)

    def createCustom(self):
        self.width = 3
        self.height = 3
        self.x = 0
        self.y = 0
        cont = 0

        while cont == 0:

            print("¿Cuáles valores quieres modificar?")
            print("**Si no modificas el tamaño será de 3x3 por default. Si no modificas la posición inicial, será (0,0) por default.**")
            print("")
            print("1) Tamaño")
            print("2) Posición inicial")
            print("3) Salir")
            opt = int(input())
           
            if opt == 1:
                while True:
                    try:
                        self.width = int(input("Ingrese la altura del ambiente: "))
                        self.height = int(input("Ingrese la anchura  del ambiente: "))                         
                        break
                    except ValueError:
                        print("Solo enteros! intente de nuevo.")
                        continue
            
            if opt == 2:
                while True:
                    flag1 = True
                    flag2 = True
                    
                    print("Ingrese la posición inicial de la aspiradora en: ")
                    self.x = int(input("X: "))
                    if self.x <= 0 or self.x >= self.width:
                        print('ERROR: Ingrese valores validos')
                        flag1 = False

                    self.y = int(input("Y: "))
                    if self.y <= 0 or self.y >= self.width:
                        print('ERROR: Ingrese valores validos')
                        flag2 = False

                    if flag1 and flag2:
                        break
            if opt == 3:
                self.vacuum = VacuumCleaner(self.width, self.height)
                self.matrix = np.random.randint(0,2, size = (self.width, self.height))
                self.vacuum.x = self.x
                self.vacuum.y = self.y
                self.matrix[self.x][self.y] = 4
                cont = 1
                break

            if opt <= 0 or opt >= 4:
                print("Selecciona una opción válida.")
            

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
        
    def createAgent(self):
        pass

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        pass

    def moveDown(self):
        pass

    def cleanDirt(self):
        pass

    def detectDirt(self):
        pass

def main():
    env = Environment()
    opt = menu()
    if opt == 1:
        env.createRandom()
        print("Este es tu nuevo ambiente: ")
        print(env.matrix)
    elif opt == 2:
        env.createCustom()
        print("Este es tu nuevo ambiente: ")
        print(env.matrix)

def menu():
    print("Bienvenido al entorno de aspiradora. Escoge una opción: ")
    print("\t 1. Ambiente aleatorio")
    print("\t 2. Ambiente personalizado")

    opt = int(input('Ingrese una opcion: '))
    if opt > 2 or opt < 0:
        print("Opción no válida, escoge de nuevo")
        menu()
    return opt


if __name__ == "__main__":
    main()
