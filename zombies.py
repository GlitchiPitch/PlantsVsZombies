import arcade

import settings

ZOMBIE_SETTINGS = settings.settings['Zombies']
SCREEN_SETTINGS = settings.screen_settings

class Zombie(arcade.Sprite):
    def __init__(self, image, health, damage, speed):
        super().__init__(image, .11)
        self.health = health
        self.damage = damage

        self.column = 0
        self.speed = speed
        self.eating = False

    def update(self):
        if not self.eating:
            self.change_x = self.speed
        else:
            self.change_x = 0
        
        self.center_x -= self.change_x

    def spawn(self, y, column):
        self.set_position(SCREEN_SETTINGS['WIDTH'], y)
        self.column = column

class EasyZombie(Zombie):
    def __init__(self):
        super().__init__('zombies/zom1.png', ZOMBIE_SETTINGS['EasyZombie']['health'], ZOMBIE_SETTINGS['EasyZombie']['damage'], ZOMBIE_SETTINGS['EasyZombie']['speed'])

    def update(self):
        super().update()

class MediumZombie(Zombie):
    def __init__(self):
        super().__init__('zombies/cone1.png', ZOMBIE_SETTINGS['MediumZombie']['health'], ZOMBIE_SETTINGS['MediumZombie']['damage'], ZOMBIE_SETTINGS['MediumZombie']['speed'])

    def update(self):
        super().update()

class HeavyZombie(Zombie):
    def __init__(self):
        super().__init__('zombies/buck1.png', ZOMBIE_SETTINGS['HeavyZombie']['health'], ZOMBIE_SETTINGS['HeavyZombie']['damage'], ZOMBIE_SETTINGS['HeavyZombie']['speed'])

    def update(self):
        super().update()
