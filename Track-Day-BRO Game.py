import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)#measured in 'RGB'
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

block_color = (53,115,255)

car_width = 75

gameDisplay = pygame.display.set_mode((display_width,display_height)) #sets display and width and height
pygame.display.set_caption('Track Day: BRO') #Window title
clock = pygame.time.Clock() #Define the games clock

carImg = pygame.image.load('miata.png') #load an image, must be in same folder as program


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: '+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])



def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font,):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    #text surface and text rectangle
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed! :\'( ')



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * .72)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 75
    thing_height = 75

    dodged = 0

    gameExit = False

    while not gameExit:
        #EVENT HANDLING LOOP
        for event in pygame.event.get(): #gets any event that happens such as key presses, list of events per frame
            if event.type == pygame.QUIT: #pygame.quit is when 'x' is hit to close
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change
        gameDisplay.fill(white) #Order matters like layers

        #things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += .5
            thing_width += (dodged * 1.05)


        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and  x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update() #or pygame.display.flip() .update can focus its scope
        clock.tick(60) # FPS set



game_loop()
pygame.quit() #must quit pygame to stop it from running
quit()
