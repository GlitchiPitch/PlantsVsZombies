import arcade
import random

from settings import screen_settings

import plants
import zombies

WIDTH = screen_settings['WIDTH']
HEIGHT = screen_settings['HEIGHT']

SPAWN_ZOMBIE_TIME = 5
ZOMBIE_LIST = [zombies.EasyZombie, zombies.MediumZombie, zombies.HeavyZombie]

LEFT_BORDER = 230
BOTTOM_BORDER = 35

CELL_WIDTH = 100
CELL_HEIGHT = 60

def find_center_cell_x(x):
    right_x = LEFT_BORDER + CELL_WIDTH
    row = 0
    while x < right_x:
        right_x += CELL_WIDTH
        row += 1
    center_x = right_x - CELL_WIDTH / 2
    return center_x, row

def find_center_cell_y(y):
    right_y = BOTTOM_BORDER + CELL_HEIGHT
    column = 0
    while y < right_y:
        right_y += CELL_HEIGHT
        column += 1
    center_y = right_y - CELL_HEIGHT / 2
    return center_y, column


class Game(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT)
        self.seed = None

        self.plants = arcade.SpriteList()
        self.zombies = arcade.SpriteList()

        self.taken_cell = []
        self.spawn_zombie_time = 0

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT, arcade.load_texture('textures/background.jpg'))
        arcade.draw_texture_rectangle(WIDTH / 18, HEIGHT / 2, WIDTH/8 , HEIGHT, arcade.load_texture('textures/menu_vertical.png'))

        self.plants.draw()
        self.zombies.draw()

        if self.seed != None:
            self.seed.draw()

    def update(self, delta_time):
        self.plants.update()
        self.zombies.update()

        # self.spawn_zombie(delta_time)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x,y)
        if 5 < x < 100:
            if 375 < y < 480:
                self.seed = plants.Sunflower()
            if 265 < y < 365:
                self.seed = plants.PeaShooter()
            if 150 < y < 250:
                self.seed = plants.WallNut()
            if 35 < y < 135:
                self.seed = plants.FireTree()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if 230 < x < 940 and 35 < y < 520:
            if self.seed != None:
                center_x, row = find_center_cell_x(x)
                center_y, column = find_center_cell_y(y)
                if not (row, column) == self.taken_cell:
                    print('add')
                    self.seed.planting(center_x, center_y, row, column)
                    self.plants.append(self.seed)
                    self.seed = None
                else:
                    print('taken')
                    self.seed = None
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.seed != None:
            self.seed.set_position(x, y)

    def spawn_zombie(self, delta_time):
        self.spawn_zombie_time += delta_time
        if self.spawn_zombie_time > SPAWN_ZOMBIE_TIME:
            self.spawn_zombie_time = 0
            zombie = random.choice(ZOMBIE_LIST)()
            center_y, column = find_center_cell_y(random.randint(35, 520))
            zombie.spawn(center_y, column)
            self.zombies.append(zombie)

game = Game()
arcade.run()