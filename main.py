import arcade

import plants

WIDTH, HEIGHT = 1000, 600

BACKGROUND = 'textures/background.jpg'
VERTICAL_MENU = 'textures/menu_vertical.png'

LEFT_BORDER_COOR = 226
RIGHT_BORDER_COOR = 950
BOTTOM_BORDER_COOR = 30
TOP_BORDER_COOR = 510

LEFT_BORDER_VERTICAL_MENU = 10
RIGHT_BORDER_VERTICAL_MENU = 100

CELL_WIDTH, CELL_HEIGHT = 90, 100

def find_center_of_cell(x, y):
    right_x = LEFT_BORDER_COOR + CELL_WIDTH
    row = 0
    while x > right_x:
        right_x += CELL_WIDTH
        row += 1
    center_x = right_x - CELL_WIDTH/2
    
    right_y = BOTTOM_BORDER_COOR + CELL_HEIGHT
    column = 0
    while y > right_y:
        right_y += CELL_HEIGHT
        column += 1
    center_y = right_y - CELL_HEIGHT/2

    return center_x, center_y, row, column


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT)
        self.plants = arcade.SpriteList()
        self.zombies = arcade.SpriteList()

        self.zombie_spawn_time = 0

        self.seed = None
        self.taken_cell = []

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, arcade.load_texture(BACKGROUND))
        arcade.draw_texture_rectangle(WIDTH/18, HEIGHT/2, WIDTH/8, HEIGHT, arcade.load_texture(VERTICAL_MENU))
        self.plants.draw()
        self.zombies.draw()

        if self.seed != None:
            self.seed.draw()

    def update(self, delta_time):
        self.plants.update()
        self.zombies.update()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # print(x)
        # print(y)
        if LEFT_BORDER_VERTICAL_MENU < x < RIGHT_BORDER_VERTICAL_MENU:
            if 376 < y < 482:
                # print('sun')
                self.seed = plants.Sunflower(self)
            elif 260 < y < 370:
                # print('pea')
                self.seed = plants.Pea_shooter(self)
            elif 145 < y < 252:
                # print('nut')
                self.seed = plants.Nut(self)
            elif 32 < y < 135:
                # print('tree')
                self.seed = plants.Tree(self)
            
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if LEFT_BORDER_COOR < x < RIGHT_BORDER_COOR and BOTTOM_BORDER_COOR < y < TOP_BORDER_COOR:
            if self.seed != None:
                center_x, center_y, row, column = find_center_of_cell(x, y)
                if (row, column) == self.taken_cell:
                    self.seed = None
                else:
                    self.seed.planting(center_x, center_y, row, column)
                    self.plants.append(self.seed)
                    self.taken_cell.append((row, column))
                    self.seed = None
        else:
            if self.seed != None:
                self.seed = None
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.seed != None:
            self.seed.set_position(x, y)
    
    def spawn_zombie(self, delta_time):
        pass
    
game = Game()
arcade.run()