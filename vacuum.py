import random


class VacuumCleaner():
    def __init__(self, width, height):
        # Vacuum position
        self.x = random.randint(0, width - 1)
        self.y = random.randint(0, height - 1)

        # Vacuum preformance
        self.moves = 0
        self.dirt  = 0

    def detectDirt(self, matrix):
        return matrix[self.y][self.x] == 1

    def cleanDirt(self, matrix):
        matrix[self.y][self.x] = 0
        self.dirt += 1

    def moveRight(self):
        self.x += 1
        self.moves += 1

    def moveLeft(self):
        self.x -= 1
        self.moves += 1

    def performance(self):
        # puntos sucios/bloques caminados del ambiente * 100 = 34% de los bloqus recorridos eran sucios
        print(self.moves)
        print(self.dirt)

        if self.moves <= 0:
            return self.dirt / 1 * 100
        else:
            return self.dirt / self.moves * 100
    
    def performancePenalized(self):
        return  self.dirt - self.moves
                

#    def moveUp(self):
#        pass

#    def moveDown(self):
#        pass
