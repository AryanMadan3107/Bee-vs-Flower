import pgzrun
import random

WIDTH=600
HEIGHT=500
score=0
gameover=False

b=Actor("bee")
b.x=random.randint(50,550)
b.y=random.randint(50,450)

f=Actor("flower")
f.x=random.randint(50,550)
f.y=random.randint(50,450)

def timeup():
    global gameover
    gameover=True

def r():
    f.x=random.randint(50,550)
    f.y=random.randint(50,450)

def draw():
    screen.blit("background",(0,0))
    b.draw()
    f.draw()
    screen.draw.text(str(score),(50,50))
    if gameover:
        screen.fill("orange")
        screen.draw.text("time's up you scored "+ str(score)+" points",center=(300,225),fontsize=50,color="blue")

def update():
    global score
    if keyboard.left:
        b.x-=3
    if keyboard.right:
        b.x+=3
    if keyboard.up:
        b.y-=3
    if keyboard.down:
        b.y+=3
    if f.colliderect(b):
        r()
        score+=1
    
clock.schedule(timeup,10.0)

pgzrun.go()