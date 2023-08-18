import arcade
from settings import settings

PLANTS_SETTINGS = settings['Plants']

class Plant(arcade.Sprite):
    def __init__(self, image, health, cost):
        super().__init__(image, .15)
        self.health = health
        self.cost = cost
        self.row = 0
        self.column = 0
    def update(self):
        if self.health <= 0:
            self.kill()
    def planting(self, x, y, row, column):
        self.set_position(x, y)
        self.row = row
        self.column = column

class Sunflower(Plant):
    def __init__(self):
        super().__init__('plants/sun1.png', PLANTS_SETTINGS['Sunflower']['health'], PLANTS_SETTINGS['Sunflower']['cost'])
    def update(self):
        super().update()

class PeaShooter(Plant):
    def __init__(self):
        super().__init__('plants/pea1.png', PLANTS_SETTINGS['PeaShooter']['health'], PLANTS_SETTINGS['PeaShooter']['cost'])
    def update(self):
        super().update()

class WallNut(Plant):
    def __init__(self):
        super().__init__('plants/nut1.png', PLANTS_SETTINGS['WallNut']['health'], PLANTS_SETTINGS['WallNut']['cost'])
    def update(self):
        super().update()

class FireTree(Plant):
    def __init__(self):
        super().__init__('plants/tree1.png', PLANTS_SETTINGS['FireTree']['health'], PLANTS_SETTINGS['FireTree']['cost'])
    def update(self):
        super().update()

