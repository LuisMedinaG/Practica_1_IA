
import random

class VacuumCleaner:
    def __init__(self, width, height):
        # Vacuum position
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        # Vacuum preformance
        self.energyUsed = 0
        self.sensorIterations = 0
        self.dirtDetected = 0

        # Vacuum sensors
        self.sensors = {"up": False, "down": False, "left": True, "right": True}

        self.environment = None

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
