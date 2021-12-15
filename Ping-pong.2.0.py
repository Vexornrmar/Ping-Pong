from pygame import *
from random import randint




win_width = 700
win_height = 500
Display.set_caption('Ping_Pong')
window = display.set_mode((win_width, win_height))

win_width = 1000
win_height = 700


background = transform.scale(image.load(img_fon), (700, 500))
wall_1 = Player_1(img_wall, 30, 200, 4, 50, 150 )
wall_2 = Player_2(img_wall, 30, 200, 4, 50, 150 )
ball 

class GameSprite(sprite.Sprite):



    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player_1(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed




class Player_2(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_A] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_D] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


wall_1 = Player_1(img_wall, 30, 200, 4, 50, 150 )
wall_2 = Player_2(img_wall, 30, 200, 4, 50, 150 )
ball = GameSprite(img_ball, 0, 0, 40, 40, 130)
