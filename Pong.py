from PPlay.sprite import *

from PPlay.window import *

janela = Window(800,600)
bola = Sprite("bola.png", 1)

while True:

    janela.set_background_color((100,150,150))
    janela.set_title("Rafael")
    bola.set_position(400,300)
    bola.draw()
    janela.update()
