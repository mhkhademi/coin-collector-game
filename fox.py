import pgzrun
from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
time = 120

fox = Actor("fox")
fox.pos = 100, 100

hedgehog = Actor("hedgehog")
hedgehog.pos = 100, 100

coin1 = Actor("coin")
coin1.pos = 200 , 200

coin2 = Actor("coin")
coin2.pos = 200, 200

def draw():
    screen.fill("pink")
    fox.draw()
    hedgehog.draw()
    coin1.draw()
    coin2.draw()
    screen.draw.text("Final Score : " + str(score) , topleft = (10,10) , color = "black")
    if game_over :
        screen.fill("blue")
        screen.draw.text("Final Score : " + str(score) , topleft = (200,200))

def place_coin1():
    coin1.x = randint(0 , WIDTH-30)
    coin1.y = randint(0 , HEIGHT-30)

def place_coin2():
    coin2.x = randint(0, WIDTH-30)
    coin2.y = randint(0, HEIGHT-30)

def place_hedgehog():
    hedgehog.x = randint(0, WIDTH-30)
    hedgehog.y = randint(0, HEIGHT-30)

def times_up():
    global game_over
    game_over = True

def update():

    global time

    global score
    
    if keyboard.left :
        fox.x = fox.x - 3

    if keyboard.right :
        fox.x = fox.x + 3

    if keyboard.up :
        fox.y = fox.y - 3

    if keyboard.down :
        fox.y = fox.y + 3

    coin_collected1 = fox.colliderect(coin1)

    coin_collected2 = fox.colliderect(coin2)

    hedgehog_collected = fox.colliderect(hedgehog)
    
    if coin_collected1 :
        time += 10
        score += 10
        place_coin1()
    
    if coin_collected2 :
        time += 10
        score += 10
        place_coin2()

    if hedgehog_collected :
        time -= 10
        score -= 10
        place_hedgehog()
        
clock.schedule(times_up , time)

place_coin1()
place_coin2()
place_hedgehog()

pgzrun.go()
