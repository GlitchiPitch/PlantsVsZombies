import arcade
import time

from settings import settings

import items

PLANTS_SETTINGS = settings['Plants']

class Plant(arcade.Sprite):
    def __init__(self, image, health, cost):
        super().__init__(image, .11)
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
    def __init__(self, game):
        super().__init__('plants/sun1.png', PLANTS_SETTINGS['Sunflower']['health'], PLANTS_SETTINGS['Sunflower']['cost'])

        self.game = game
        self.spawn_sun_time = time.time()

    def update(self):
        super().update()

        if time.time() - self.spawn_sun_time > PLANTS_SETTINGS['Sunflower']['spawnSunTime']:
            self.spawn_sun_time = time.time()
            sun = items.Sun(self.right, self.top)
            self.game.suns.append(sun)

class PeaShooter(Plant):
    def __init__(self, game):
        super().__init__('plants/pea1.png', PLANTS_SETTINGS['PeaShooter']['health'], PLANTS_SETTINGS['PeaShooter']['cost'])

        self.shoot_time = time.time()

        self.game = game

    def update(self):
        super().update()

        for zombie in self.game.zombies:
            if zombie.line == self.row:
                if time.time() - self.shoot_time > PLANTS_SETTINGS['PeaShooter']['reloadTime']:
                    self.shoot_time = time.time()
                    pea = items.Pea(self.right, self.top - 5, self.game)
                    self.game.peas.append(pea)


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

