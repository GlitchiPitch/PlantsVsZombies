import arcade
import time

import animation

import settings
import items

SCALE = .15

class Plant(animation.Animation):
    def __init__(self, image, health, cost):
        super().__init__(image, SCALE)
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
        prop = settings.settings['Plants']['Sunflower']
        super().__init__('plants/sun1.png', prop['Health'], prop['Cost'], game)
        self.append_texture(arcade.load_texture('plants/sun2.png'))

        self.spawn_sun = time.time()
        self.game = game
    def update(self):
        super().update()
        if time.time() - self.spawn_sun > 5:
            self.game.suns.append(items.Sun(self.right, self.top))
            self.spawn_sun = time.time()

class Pea_shooter(Plant):
    def __init__(self, game):
        prop = settings.settings['Plants']['Pea_shooter']
        super().__init__('plants/pea1.png', prop['Health'], prop['Cost'], game)
        self.shoot_time = time.time()
        for i in range(1, 3):
            self.append_texture(arcade.load_texture(f'plants/pea{i}.png'))

    def update(self):
        super().update()

class Nut(Plant):
    def __init__(self, game):
        prop = settings.settings['Plants']['Wall_nut']
        super().__init__('plants/nut1.png', prop['Health'], prop['Cost'], game)

        for i in range(1, 3):
            self.append_texture(arcade.load_texture(f'plants/nut{i}.png'))

    def update(self):
        super().update()

class Tree(Plant):
    def __init__(self, game):
        prop = settings.settings['Plants']['Tree']
        super().__init__('plants/tree1.png', prop['Health'], prop['Cost'], game)

        for i in range(1, 3):
            self.append_texture(arcade.load_texture(f'plants/tree{i}.png'))

    def update(self):
        super().update()
