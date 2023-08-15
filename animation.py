import arcade

FRAME_PER_SECOND = .2

class Animation(arcade.Sprite):
    i = 0
    time = 0
    def update_animation(self, delta_time):
        self.time += delta_time
        if self.time > FRAME_PER_SECOND:
            self.time = 0
            if self.i == len(self.textures) - 1:
                self.i = 0
            else:
                self.i += 1
            self.set_texture(self.i)