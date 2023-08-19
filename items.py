import arcade
import time

from settings import screen_settings
from settings import settings

ITEMS_SETTING = settings['Items']

class Pea(arcade.Sprite):
    def __init__(self, x, y, game):
        super().__init__('items/bul.png', .1)

        self.set_position(x, y)

        self.change_x = ITEMS_SETTING['Pea']['speed']
        self.game = game
        self.damage = 1

    def update(self):
        self.center_x += self.change_x

        if self.left >= screen_settings['WIDTH']:
            self.kill()

        for zombie in arcade.check_for_collision_with_list(self, self.game.zombies):
            zombie.health -= self.damage
            self.kill()

class Sun(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('items/sun.png', .1)
        self.lifeTime = time.time()
        self.set_position(x, y)
    def update(self):
        self.angle += 1

        if time.time() - self.lifeTime > ITEMS_SETTING['Sun']['lifeTime']:
            self.kill()