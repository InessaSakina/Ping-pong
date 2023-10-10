from pygame import *

window = display.set_mode((900,700))
display.set_caption("Пинг-понг")
fon = transform.scale(image.load("images.jpg"), (900,700))

font.init()
font = font.Font(None,35)

class Character(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player (Character):
    def control_1(self):
        control = key.get_pressed()
        if control[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if control[K_s] and self.rect.y<800:
            self.rect.y += self.speed
    def control_2(self):
        control = key.get_pressed()
        if control[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if control[K_DOWN] and self.rect.y<800:
            self.rect.y += self.speed

game = True
finish = False
clock = time.Clock()
Wall_1 = Player('wallfirst.jpg',30,200,35,300,7)
Wall_2 = Player('wallsecond.jpg',860,200,35,300,7)
ball = Player('ballforfootball.jpg',90,250,50,50,0)
lose_1 = font.render ('1 игрок проиграл',True,(225,10,90))
lose_2 = font.render ('2 игрок проиграл',True,(225,10,90))
ball_x = 2
ball_y = 2

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:    
        window.blit(fon,(0,0))
        Wall_1.reset()
        Wall_1.control_1()
        Wall_2.reset()
        Wall_2.control_2()
        ball.reset()
        ball.rect.x += ball_x
        ball.rect.y -= ball_y
        if sprite.collide_rect(Wall_1, ball) or sprite.collide_rect(Wall_2, ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y < 0 or ball.rect.y > 860:
            ball_y *= -1
        if ball.rect.x < -30:
            finish = True
            window.blit(lose_1,(350,200))
        if ball.rect.x > 890:
            finish = True
            window.blit(lose_2,(350,200))
        display.update()
    clock.tick()

