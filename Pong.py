from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
import random

janela = Window(800,600)

teclado = Keyboard()

bola = Sprite("bola.png", 1)

barra_player = Sprite("barra.png", 1)
barra_player.set_position(10,400-barra_player.height)
speed_player = 1
pontos_player = 0

barra_ia = Sprite("barra.png", 1)
barra_ia.set_position(janela.width - barra_ia.width - 10, 400-barra_ia.height)
speed_ia = 0.4
pontos_ia = 0

list = [150, 100, -100, -150]

vel_x = random.choice(list)
vel_y = random.choice(list)

start = False

altura_janela = janela.height
largura_janela = janela.width

bola.set_position((largura_janela/2)-(bola.width/2), (altura_janela/2)-(bola.height/2))

while True:

    janela.set_background_color((0,0,255))
    janela.set_title("Rafael")
    
    if start == False:
        bola.set_position((largura_janela/2)-(bola.width/2), (altura_janela/2)-(bola.height/2))
        vel_x = random.choice(list)
        vel_y = random.choice(list)

    if bola.x >= (largura_janela-(bola.width)):
        pontos_player += 1
        start = False

    if bola.x <= 0:
        pontos_ia += 1
        start = False

    if(teclado.key_pressed("space")):
        start = True

    if(start == True):
        bola.y += vel_y * janela.delta_time()
        bola.x += vel_x * janela.delta_time()

        barra_player.move_key_y(speed_player)

    if barra_player.collided(bola):
        vel_x = vel_x*-1
        if -600 < vel_x < 600:
            vel_x = vel_x *1.5

    if barra_ia.collided(bola):
        vel_x = vel_x*-1
        if -600 < vel_x < 600:
            vel_x = vel_x *1.5

    if bola.y >= altura_janela-bola.height or bola.y <= 0:
        vel_y = vel_y*-1
        if -600 < vel_y < 600:
            vel_y = vel_y *1.2

    if barra_player.y >= altura_janela-barra_player.height:
        barra_player.y = altura_janela-barra_player.height

    if barra_player.y <= 0:
        barra_player.y = 0

    if barra_ia.y >= altura_janela-barra_ia.height:
        barra_ia.y = altura_janela-barra_ia.height

    if barra_ia.y <= 0:
        barra_ia.y = 0

    if vel_y < 0 and start == True:
        barra_ia.move_y(speed_ia*-1)
        if barra_ia.y > bola.y:
            barra_ia.move_y(speed_ia*-1.1)
    
    if vel_y > 0 and start == True:
        barra_ia.move_y(speed_ia)
        if barra_ia.y < bola.y:
            barra_ia.move_y(speed_ia*1.1)

    janela.draw_text(f"{pontos_player}     X     {pontos_ia}",335, 20, 30,
                     bold=True, color=(200, 200, 0), font_name="Times")

    barra_ia.draw()
    barra_player.draw()
    bola.draw()
    janela.update()