from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
import random

janela = Window(800,600)
bola = Sprite("bola.png", 1)
teclado = Keyboard()

list = [-0.2, -0.1, 0.1, 0.2]

vel_x = random.choice(list)
vel_y = random.choice(list)

print(vel_x, vel_y)

start = False

altura_janela = janela.height
largura_janela = janela.width

bola.set_position((largura_janela/2)-(bola.width/2), (altura_janela/2)-(bola.height/2))

while True:

    janela.set_background_color((0,0,255))
    janela.set_title("Rafael")
    
    if(teclado.key_pressed("space")):
        start = True

    if(start == True):
        bola.y += vel_y
        bola.x += vel_x 

    if bola.y >= altura_janela-bola.height or bola.y <= 0:
        vel_y = vel_y*-1
        if -1 < vel_y < 1:
            vel_y = vel_y *1.1
    
    if bola.x >= (largura_janela-(bola.width)) or bola.x <= 0:
        vel_x = vel_x*-1
        if -1 < vel_x < 1:
            vel_x = vel_x *1.1
    bola.draw()
    janela.update()