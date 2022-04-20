#***********************************************************************************************************************************
# George Salib
# École secondaire catholique Renaissance
# ISC4U, Quad 4, 2020-21
# 
# Dernière modification: 21-06-2021
# 
# DESCRIPTION:
# Ceci est un programme en python qui implemente les méthode de turtle et pygame de python afin
# de crée un jeu de chenille dont la chenille se tranforme dépendament à ce qu'elle mange. Il y a 
# aussi une système de menus, sons et images qui fonctionnent afin de bien diriger l'utilisateur dans le jeu.
# 
# HYPOTHÈSE:
# Elle éxécuterait bien et fonctionnerais selon les données de l'utilisateur
#***********************************************************************************************************************************

# Importing the required modules
import random
import turtle as t
import pygame
from pygame import mixer
from pygame.locals import *
import os
import time

# Main menu initialization
t.title('Jeu Chenille - George')
pygame.init()
 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
# Colors
white=(255, 255, 255)
red=(255, 0, 0)
blue=(0, 150, 255)
gray=(80, 80, 80)
 
# Game Fonts
font = "Retro.ttf"

# Initialises background image
background_image = pygame.image.load("snakegamebg.jpg").convert()

# Initialises and plays intro music
pygame.mixer.init()
intro_music = mixer.Sound('2bitmusic.wav')
intro_music.play(100)

#***********************************************************************************************************************************

# Main Menu
#***********************************************************************************************************************************

def main_menu():
 
    menu = True
    selected = "start"
 
    while menu:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        player_menu=True
                        while player_menu:        
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                if event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_RETURN:                    
                                        return True
                    
                            # Main Menu UI
                            screen.blit(background_image, [0, 0])
                            title=text_format("Instructions", font, 90, red)
                            text_info=text_format("Bienvenue à ChanilleMania!", font, 35, white)
                            text_desc1=text_format("- Mange les feuilles ou etoiles pour agrandir", font, 35, white)
                            text_desc2=text_format("- Ne sort pas de la fenaitre et ne mange pas les bombes", font, 35, white)
                            text_desc3=text_format("- Récupérer l'horloge pour ralentir votre vitesse", font, 35, white)
                            if selected=="start":
                                text_start=text_format("JOUER!", font, 75, gray)
                    
                            title_rect=title.get_rect()
                            start_rect=text_info.get_rect()
                            start_rect=text_desc1.get_rect()
                            start_rect=text_desc2.get_rect()
                            start_rect=text_desc3.get_rect()
                            quit_rect=text_start.get_rect()
                    
                            # Main Menu Text
                            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
                            screen.blit(text_info, (screen_width/2 - (start_rect[2]/2), 200))
                            screen.blit(text_desc1, (screen_width/2 - (start_rect[2]/2), 230))
                            screen.blit(text_desc2, (screen_width/2 - (start_rect[2]/2), 260))
                            screen.blit(text_desc3, (screen_width/2 - (start_rect[2]/2), 290))
                            screen.blit(text_start, (screen_width/2 - (quit_rect[2]/2), 360))
                            pygame.display.update()      

                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.blit(background_image, [0, 0])
        title=text_format("ChenilleMania", font, 90, red)
        if selected=="start":
            text_start=text_format("COMMENCER", font, 75, gray)
        else:
            text_start = text_format("COMMENCER", font, 75, white)
        if selected=="quit":
            text_quit=text_format("QUITTER", font, 75, gray)
        else:
            text_quit = text_format("QUITTER", font, 75, white)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        pygame.display.set_caption("ChenilleMania - George")

#***********************************************************************************************************************************

# Game exectution
#***********************************************************************************************************************************

# Runs game when user selects start
run = main_menu()
intro_music.stop()

# Game execution
while run:
    # Initialising and declaring the background color and title of game
    t.title("ChenilleMania - George")
    t.addshape('slitherbg2.gif')
    bg = t.Turtle()
    bg.shape('slitherbg2.gif')

    # Creating the 1st caterpillar head turtle and assigning its values
    caterpillar = t.Turtle()            # Creates a new turtle for the 1st caterpillar
    caterpillar.shape('square')
    caterpillar.color('red')
    caterpillar.speed(0)                # Keeps the caterpillar still until game starts
    caterpillar.penup()                 # Disables line of movement of the turtle
    caterpillar.hideturtle()
    caterpillar.direction = 'stop'

    # Creating the 2nd caterpillar head turtle and assigning its values
    caterpillar2 = t.Turtle()           # Creates a new turtle for the 2nd caterpillar
    caterpillar2.shape('square')
    caterpillar2.color('blue')
    caterpillar2.speed(0)               # Keeps the caterpillar still until game starts
    caterpillar2.penup()                # Disables line of movement of the turtle
    caterpillar2.hideturtle()

    # Creating the leaf turtle and assigning its values
    t.addshape('leafcartoon.gif')
    leaf = t.Turtle()                   # Creates a new turtle for the leaves
    leaf.shape('leafcartoon.gif')
    leaf.color('green')
    leaf.penup()
    leaf.hideturtle()
    leaf.speed(0)

    # Creating the bomb turtle and assigning its values
    t.addshape('bombpython.gif')
    bomb = t.Turtle()                   # Creates a new turtle for the bomb
    bomb.shape('bombpython.gif')  
    bomb.penup()
    bomb.hideturtle()
    bomb.speed(0)

    # Creating the timer turtle and assigning its values
    t.addshape('timerpython.gif')
    timerbomb = t.Turtle()              # Creates a new turtle for the timer
    timerbomb.shape('timerpython.gif')  
    timerbomb.penup()
    timerbomb.hideturtle()
    timerbomb.speed(0)

    # Creating the star turtle and assigning its values
    t.addshape('starpython.gif')
    star = t.Turtle()              # Creates a new turtle for the star
    star.shape('starpython.gif')  
    star.penup()
    star.hideturtle()
    star.speed(0)

    # Turtle text asking user how many players are playing
    player_count_turtle = t.Turtle()
    player_count_turtle.color('white')
    player_count_turtle.write('Appuyez \'1\' pour 1 joueur ou \'2\' pour 2 joueurs', align = 'center', \
                        font = ('Arial', 16, 'bold')) # Draws the text on screen
    player_count_turtle.hideturtle()

    # Adds the intro text to the game
    game_started = False
    text_turtle = t.Turtle()
    text_turtle.color('white')
    def start():
        text_turtle.write('Appuyez SPACE pour commencer', align = 'center', \
                        font = ('Arial', 16, 'bold')) # Draws the text on screen
    text_turtle.hideturtle()                          # Hides the turtle but not the text

    # Adds player 1 score text
    player1_score_turtle = t.Turtle()
    player1_score_turtle.color('white')
    player1_score_turtle.hideturtle()
    player1_score_turtle.speed(0)

    # Adds player 2 score text
    player2_score_turtle = t.Turtle()
    player2_score_turtle.color('white')
    player2_score_turtle.hideturtle()
    player2_score_turtle.speed(0)

    # Function that determines if the caterpillar goes out or the bounds of the window
    def outside_window(caterpillar):
        left_wall = -t.window_width() / 2
        right_wall = t.window_width() / 2
        top_wall = t.window_height() / 2
        bottom_wall = -t.window_height() / 2
        (x, y) = caterpillar.pos()
        outside = \
                x < left_wall or \
                x > right_wall or \
                y < bottom_wall or \
                y > top_wall
        return outside

    # Function that terminates the game by clearing the turtles from screen and displaying an end message
    def singleplayer_game_over():
        death_sound()
        caterpillar.hideturtle()
        caterpillar2.hideturtle()
        leaf.hideturtle()
        bomb.hideturtle()
        timerbomb.hideturtle()
        star.hideturtle()
        t.penup()
        t.hideturtle()
        t.color('white')
        t.write('GAME OVER!', align = 'center', font = ('Arial', 30, 'normal'))

    def multiplayer_game_over(winner):
        death_sound()
        caterpillar.hideturtle()
        caterpillar2.hideturtle()
        leaf.hideturtle()
        bomb.hideturtle()
        timerbomb.hideturtle()
        star.hideturtle()
        t.penup()
        t.hideturtle()
        t.color('white')
        if winner == caterpillar:
            t.write('ROUGE GAGNE!', align = 'center', font = ('Arial', 30, 'normal'))
        else:
            t.write('BLEU GAGNE!', align = 'center', font = ('Arial', 30, 'normal'))

    # Function that displays player 1 current score on screen
    def player1_display_score(current1_score):
        player1_score_turtle.clear()
        player1_score_turtle.penup()
        x = (t.window_width() / 2) - 600
        y = (t.window_height() / 2) - 50
        player1_score_turtle.setpos(x, y)
        player1_score_turtle.write('Rouge Score: ' + str(current1_score), align = 'left', \
                        font = ('Arial', 20, 'bold'))

    # Function that displays player 2 current score on screen
    def player2_display_score(current2_score):
        player2_score_turtle.clear()
        player2_score_turtle.penup()
        x = (t.window_width() / 2) - 50
        y = (t.window_height() / 2) - 50
        player2_score_turtle.setpos(x, y)
        player2_score_turtle.write('Bleu Score: ' + str(current2_score), align = 'right', \
                        font = ('Arial', 20, 'bold'))

    # Function that places a leaf at a random coordinate insite the bounds of the window
    def place_leaf():
        leaf.ht()       # Hides the leaf turtle (ht short for hideturtle)

        # Creates random coordinates for the new leaf
        leaf.setx(random.randint(-200, 200))
        leaf.sety(random.randint(-200, 200))

        leaf.st()       # Shows the leaf turtle (st sort for show turtle)

    def place_bomb(score1, score2, bomb_exists):
        if score1 == 20 or score2 == 20 or score1 == 40 or score2 == 40 and score1 == 60 or score2 == 60 and not(bomb_exists):
            bomb.ht()   # Hides the bomb turtle (ht short for hideturtle)

            # Creates random coordinates for the new bomb
            bomb.setx(random.randint(-200, 200))
            bomb.sety(random.randint(-200, 200))

            bomb.st()      

            return True

        else:
            return bomb_exists

    def hide_bomb():
        bomb.ht()
        return False

    def place_timerbomb(score1, score2, timerbomb_exists):
        if score1 == 30 or score2 == 30 or score1 == 60 or score2 == 60 and score1 == 90 or score2 == 90 and not(timerbomb_exists):
            timerbomb.ht()       # Hides the timerbomb turtle (ht short for hideturtle)

            # Creates random coordinates for the new timerbomb
            timerbomb.setx(random.randint(-200, 200))
            timerbomb.sety(random.randint(-200, 200))

            timerbomb.st()      

            return True

        else:
            return timerbomb_exists

    def hide_timerbomb():
        timerbomb.ht()
        return False

    def place_star(score1, score2, star_exists):
        if score1 == 40 or score2 == 40 or score1 == 80 or score2 == 80 and score1 == 80 or score2 == 120 and not(star_exists):
            star.ht()       # Hides the star turtle (ht short for hideturtle)

            # Creates random coordinates for the new star
            star.setx(random.randint(-200, 200))
            star.sety(random.randint(-200, 200))

            star.st()      

            return True

        else:
            return star_exists

    def hide_star():
        star.ht()
        return False

    # Initialises and plays the leaf bite sound
    def leaf_sound():
        pygame.mixer.init()
        bite_sound = mixer.Sound('Leaf bite.wav')
        bite_sound.play()

    # Initialises and plays the bomb explosion sound
    def bomb_sound():
        pygame.mixer.init()
        explosion_sound = mixer.Sound('bombsound.wav')
        explosion_sound.play()

    # Initialises and plays the timer sound
    def timebomb_sound():
        pygame.mixer.init()
        time_sound = mixer.Sound('timesound.wav')
        time_sound.play()

    # Initialises and plays the star powerup sound
    def star_sound():
        pygame.mixer.init()
        star_sound = mixer.Sound('mariostarsound.wav')
        star_sound.play()
    
    # Initialises and plays the death sound
    def death_sound():
        pygame.mixer.init()
        death_sound = mixer.Sound('mariodeathsound.wav')
        death_sound.play()

    global player_count

    # Executes main game loop for 1 player
    def singleplayer():
        global player_count
        player_count = 1
        player_count_turtle.clear()
        start()
        return player_count

    # Executes main game loop for 2 players
    def multiplayer():
        global player_count
        player_count = 2
        player_count_turtle.clear()
        start()
        return player_count

    # Function that initialises the beginning of the game (main game loop)
    def start_game():
        # Starts the game and makes sure it runs only once
        global game_started
        if game_started:
            return
        game_started = True

        # Resets the score to 0 and clears the text from screen
        score1 = 0
        score2 = 0
        text_turtle.clear()

        # Sets up the caterpillar
        bomb_exists = False
        timerbomb_exists = False
        star_exists = False
        caterpillar1_speed = 2
        caterpillar1_length = 3
        caterpillar2_speed = 2
        caterpillar2_length = 3
        caterpillar.showturtle()
        caterpillar2.setheading(180)
        caterpillar2.showturtle()
        player1_display_score(score1)
        player2_display_score(score2)
        place_leaf()                        # Calls the place_leaf function to place a random leaf

        if player_count == 1:
        
            caterpillar2.ht()
            player2_score_turtle.clear()

            # Loop moving the caterpillar and checking if it eats a leaf or is outside the bounds of the window
            while True:
                caterpillar.forward(caterpillar1_speed)
                if caterpillar.distance(leaf) < 20:                  # Caterpillar eats the leaf if its closer then 20 pixels
                    place_leaf()
                    leaf_sound()
                    caterpillar1_length = caterpillar1_length + 1    # Increases the caterpillar length
                    caterpillar.shapesize(1, caterpillar1_length, 1)        
                    caterpillar1_speed = caterpillar1_speed + 1
                    score1 = score1 + 10
                    player1_display_score(score1)
                    bomb_exists = place_bomb(score1, score2, bomb_exists)
                    timerbomb_exists = place_timerbomb(score1, score2, timerbomb_exists)
                    star_exists = place_star(score1, score2, star_exists)
                if caterpillar.distance(bomb) < 20 and bomb_exists:
                    pygame.mixer.stop()
                    bomb_sound()
                    bomb_exists = hide_bomb()
                    singleplayer_game_over()
                    break
                if caterpillar.distance(timerbomb) < 20 and timerbomb_exists:
                    timebomb_sound()
                    timerbomb_exists = hide_timerbomb()
                    caterpillar1_speed -= 2               
                if caterpillar.distance(star) < 20 and star_exists:
                    pygame.mixer.stop()
                    star_sound()
                    star_exists = hide_star()
                    score1 = score1 + 30
                    player1_display_score(score1)
                if outside_window(caterpillar) or outside_window(caterpillar2):
                    pygame.mixer.stop()
                    singleplayer_game_over()
                    break

        elif player_count == 2:

            # Loop moving the caterpillar and checking if it eats a leaf or is outside the bounds of the window
            while True:
                caterpillar.forward(caterpillar1_speed)
                caterpillar2.forward(caterpillar2_speed)
                if caterpillar.distance(leaf) < 20:                  # Caterpillar eats the leaf if its closer then 20 pixels
                    place_leaf()
                    leaf_sound()
                    caterpillar1_length = caterpillar1_length + 1    # Increases the caterpillar length
                    caterpillar.shapesize(1, caterpillar1_length, 1)
                    caterpillar1_speed = caterpillar1_speed + 1
                    score1 = score1 + 10
                    player1_display_score(score1)
                    bomb_exists = place_bomb(score1, score2, bomb_exists)
                    timerbomb_exists = place_timerbomb(score1, score2, timerbomb_exists)
                    star_exists = place_star(score1, score2, star_exists)
                elif leaf.distance(caterpillar2) < 20:
                    place_leaf()
                    leaf_sound()
                    caterpillar2_length = caterpillar2_length + 1    # Increases the caterpillar length
                    caterpillar2.shapesize(1, caterpillar2_length, 1)
                    caterpillar2_speed = caterpillar2_speed + 1
                    score2 = score2 + 10
                    player2_display_score(score2)
                    bomb_exists = place_bomb(score1, score2, bomb_exists)
                    timerbomb_exists = place_timerbomb(score1, score2, timerbomb_exists)
                    star_exists = place_star(score1, score2, star_exists)
                if caterpillar.distance(bomb) < 20 and bomb_exists:
                    pygame.mixer.stop()
                    bomb_sound()
                    bomb_exists = hide_bomb()
                    winner = caterpillar2
                    multiplayer_game_over(winner)
                    break
                if caterpillar2.distance(bomb) < 20 and bomb_exists:
                    pygame.mixer.stop()
                    bomb_sound()
                    bomb_exists = hide_bomb()
                    winner = caterpillar
                    multiplayer_game_over(winner)
                    break
                if caterpillar.distance(timerbomb) < 20 and timerbomb_exists:
                    timebomb_sound()
                    timerbomb_exists = hide_timerbomb()
                    caterpillar1_speed -= 2               
                if caterpillar2.distance(timerbomb) < 20 and timerbomb_exists:
                    timebomb_sound()
                    timerbomb_exists = hide_timerbomb()
                    caterpillar2_speed -= 2
                if caterpillar.distance(star) < 20 and star_exists:
                    pygame.mixer.stop()
                    star_sound()
                    star_exists = hide_star()
                    score1 = score1 + 30
                    player1_display_score(score1)
                if caterpillar2.distance(star) < 20 and star_exists:
                    pygame.mixer.stop()
                    star_sound()
                    star_exists = hide_star()
                    score2 = score2 + 30
                    player2_display_score(score2)
                if outside_window(caterpillar):
                    pygame.mixer.stop()
                    winner = caterpillar2
                    multiplayer_game_over(winner)
                    break
                if outside_window(caterpillar2):
                    pygame.mixer.stop()
                    winner = caterpillar
                    multiplayer_game_over(winner)
                    break

    # Function that changes the heading of the 1st caterpillar upwards
    def move_up():
        if caterpillar.heading() == 0 or caterpillar.heading() == 180:
            caterpillar.setheading(90)

    # Function that changes the heading of the 1st caterpillar downwards
    def move_down():
        if caterpillar.heading() == 0 or caterpillar.heading() == 180:
            caterpillar.setheading(270)

    # Function that changes the heading of the 1st caterpillar leftward
    def move_left():
        if caterpillar.heading() == 90 or caterpillar.heading() == 270:
            caterpillar.setheading(180)

    # Function that changes the heading of the 1st caterpillar rightward
    def move_right():
        if caterpillar.heading() == 90 or caterpillar.heading() == 270:
            caterpillar.setheading(0)

    # Function that changes the heading of the 2nd caterpillar upwards
    def caterpillar2_move_up():
        if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
            caterpillar2.setheading(90)

    # Function that changes the heading of the 2nd caterpillar downwards
    def caterpillar2_move_down():
        if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
            caterpillar2.setheading(270)

    # Function that changes the heading of the 2nd caterpillar leftward
    def caterpillar2_move_left():
        if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
            caterpillar2.setheading(180)

    # Function that changes the heading of the 2nd caterpillar rightward
    def caterpillar2_move_right():
        if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
            caterpillar2.setheading(0)

    def snake1_move():
        if caterpillar.direction == 'Up':
            y = caterpillar.ycor()
            caterpillar.sety(y + 20)
        if caterpillar.direction == 'Down':
            y = caterpillar.ycor()
            caterpillar.sety(y - 20)
        if caterpillar.direction == 'Left':
            x = caterpillar.xcor()
            caterpillar.setx(x - 20)
        if caterpillar.direction == 'Right':
            x = caterpillar.xcor()
            caterpillar.setx(x + 20)

    # Assigns buttons (keys) to execute certain functions
    t.onkey(singleplayer, '1')
    t.onkey(multiplayer, '2')
    t.onkey(start_game, 'space')            # Executes the game
    t.onkey(move_up, 'Up')                  # Orients the 1st caterpillar upwards
    t.onkey(move_down, 'Down')              # Orients the 1st caterpillar downwards
    t.onkey(move_left, 'Left')              # Orients the 1st caterpillar leftward
    t.onkey(move_right, 'Right')            # Orients the 1st caterpillar rightward
    t.onkey(caterpillar2_move_up, 'w')      # Orients the 1st caterpillar upwards
    t.onkey(caterpillar2_move_down, 's')    # Orients the 1st caterpillar downwards
    t.onkey(caterpillar2_move_left, 'a')    # Orients the 1st caterpillar leftward
    t.onkey(caterpillar2_move_right, 'd')   # Orients the 1st caterpillar rightward
    t.listen()
    t.mainloop()

#***********************************************************************************************************************************

pygame.quit()
quit()