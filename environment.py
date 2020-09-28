import numpy as np
import prettytable
import random
import vacuum


class Environment():
    def __init__(self):
        self.width = 0      # La anchura del entorno
        self.height = 0     # La altura del entorno
        self.matrix = None  # Los matriz que contiene donde hay suciedad
        self.vacuum = None  # El entorno tiene un objeto aspiradora
        # Objeto para dibujar el entorno en consola
        self.world = prettytable.PrettyTable(header=False)

    def createRandom(self):
        self.width = random.randint(1, 10)
        self.height = random.randint(1, 10)
        self.vacuum = vacuum.VacuumCleaner(self.width, self.height)
        self.matrix = np.random.randint(2, size=(self.width, self.height))

        for row in self.matrix:
            self.world.add_row(row)

    def createCustom(self):
        self.width = 3
        self.height = 3
        x = 0
        y = 0
        opt = 0

        while opt != 3:
            print(
                "¿Cuáles valores quieres modificar?"
                "\n**Si no modificas el tamaño será de 3x3 por default. "
                "Si no modificas la posición inicial, será (0,0) por default.**"
                "\n1) Tamaño"
                "\n2) Posición inicial"
                "\n3) Terminar\n")

            opt = int(input("Ingrese una opcion: "))
            if opt == 1:
                while True:
                    try:
                        self.width = int(
                            input("Ingrese la altura del ambiente: "))
                        self.height = int(
                            input("Ingrese la anchura  del ambiente: "))
                        break
                    except ValueError:
                        print("Solo enteros! intente de nuevo.")
                        continue

            elif opt == 2:
                while True:
                    flag1 = True
                    flag2 = True

                    print("Ingrese la posición inicial de la aspiradora en: ")

                    x = int(input("X: "))
                    if x < 0 or x >= self.width:
                        print("ERROR: Ingrese valores validos")
                        flag1 = False
                        continue

                    y = int(input("Y: "))
                    if y < 0 or y >= self.width:
                        print("ERROR: Ingrese valores validos")
                        flag2 = False
                        continue

                    if flag1 and flag2:
                        break
            else:
                print("Selecciona una opción válida.")

        self.vacuum = vacuum.VacuumCleaner(self.width, self.height)
        self.vacuum.x = x
        self.vacuum.y = y
        self.matrix = np.random.randint(0, 2, size=(self.width, self.height))

        for row in self.matrix:
            self.world.add_row(row)
