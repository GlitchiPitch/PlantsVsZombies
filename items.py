import arcade

import settings

class Sun(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('items/sun.png')
        self.change_angle = settings.settings['Items']['Sun']['Change_angle']
    def update(self):
        self.angle += self.change_angle

class Pea(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('items/bul.png')
        self.change_x = settings.settings['Items']['Pea']['Speed']
    def update(self):
        self.center_x += self.change_x