#!/usr/bin/python

import pygame, random, time
from pygame.locals import *
    
class Card():
    
    def __init__(self, s):
        self.shape = s

    def place(self, back, shape, x, y):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)

        if x + 113 > mouse[0] > x and y + 164 > mouse[1] > y :
            if self.move_sound_played == False:
                if winner == False and self.matched == False:
                    move.play(0)
                    self.move_sound_played = True

            if winner == False and self.matched == False:
                screen.blit(highlight, (x-25, y-37))

            if click[0] == 1 and self.click == False:
                self.click = True
                self.flipped = True
        else:
            self.move_sound_played = False

        if self.flipped == True and self.flip_sound_played == False:
            self.flip_sound_played = True
            flip.play(0)
        
        """if self.flipped == True:
            screen.blit(flipping, (x, y))
            screen.blit(shape, (x, y))
            return True
        """

        if self.flipped == True:

            if self.flip_animation == 0:
                screen.blit(flipping_white, (x, y))
                self.flip_animation += 1
            elif self.flip_animation == 1:
                screen.blit(flipping_side, (x, y))
                self.flip_animation += 1
            elif self.flip_animation == 2:
                screen.blit(flipping_pink, (x, y))
                self.flip_animation += 1
            elif self.flip_animation == 3:
                screen.blit(shape, (x, y))
                
                return True
        
        else:
            if self.flag == True:
                time.sleep(1)
                self.flag = False
            screen.blit(back, (x, y))
            return False

    flipped = False
    counted = False
    high_light = False
    flip_sound_played = False
    move_sound_played = False
    match_sound_played = False
    no_match_sound_played = False
    matched = False
    shape = ''
    click = False
    flag = False
    flip_animation = 0

def select_board():

    random_number = random.randrange(1, 9)
    
    board1 = ['flower', 'star', 'oneup', 'flower', 'twenty', 'mushroom', 'ten', 'mushroom', 'twenty', 'oneup', 'mushroom', 'ten', 'star', 'flower', 'star', 'mushroom', 'flower', 'star']
    board2 = ['flower', 'twenty', 'mushroom', 'star', 'oneup', 'flower', 'oneup', 'flower', 'ten', 'mushroom', 'twenty', 'star', 'mushroom', 'ten', 'star', 'mushroom', 'flower', 'star']
    board3 = ['mushroom', 'flower', 'twenty', 'mushroom', 'ten', 'star', 'flower', 'oneup', 'mushroom', 'ten', 'oneup', 'twenty', 'star', 'flower', 'star', 'mushroom', 'flower', 'star']
    board4 = ['oneup', 'mushroom', 'ten', 'mushroom', 'flower', 'star', 'mushroom', 'ten', 'star', 'twenty', 'twenty', 'flower', 'star', 'oneup', 'flower', 'mushroom', 'flower', 'star']
    board5 = ['mushroom', 'flower', 'oneup', 'flower', 'star', 'star', 'twenty', 'star', 'mushroom', 'ten', 'oneup', 'flower', 'twenty', 'mushroom', 'ten', 'mushroom', 'flower', 'star']
    board6 = ['flower', 'ten', 'oneup', 'flower', 'oneup', 'mushroom', 'star', 'mushroom', 'twenty', 'star', 'mushroom', 'ten', 'star', 'flower', 'twenty', 'mushroom', 'flower', 'star']
    board7 = ['mushroom', 'flower', 'twenty', 'flower', 'ten', 'star', 'twenty', 'oneup', 'mushroom', 'ten', 'oneup', 'flower', 'star', 'mushroom', 'star', 'mushroom', 'flower', 'star']
    board8 = ['flower', 'star', 'oneup', 'flower', 'oneup', 'mushroom', 'ten', 'mushroom', 'flower', 'star', 'mushroom', 'ten', 'star', 'twenty', 'twenty', 'mushroom', 'flower', 'star']

    if random_number == 1:
        return board1
    elif random_number == 2:
        return board2
    elif random_number == 3:
        return board3
    elif random_number == 4:
        return board4
    elif random_number == 5:
        return board5
    elif random_number == 6:
        return board6
    elif random_number == 7:
        return board7
    elif random_number == 8:
        return board8

# Import borders
lborder = pygame.image.load('images/left.jpg')
tborder = pygame.image.load('images/top.jpg')
rborder = pygame.image.load('images/right.jpg')
hud = pygame.image.load('images/hud.jpg')

# Import Card Images
back = pygame.image.load('images/back.jpg')
flipping_white = pygame.image.load('images/flipping_pink.png')
flipping_pink = pygame.image.load('images/flipping_white.png')
side = pygame.image.load('images/side.png')
flipping_side = pygame.image.load('images/side.png')
mushroom = pygame.image.load('images/mushroom.jpg')
flower = pygame.image.load('images/flower.jpg')
star = pygame.image.load('images/star.jpg')
ten = pygame.image.load('images/ten.jpg')
twenty = pygame.image.load('images/twenty.jpg')
oneup = pygame.image.load('images/oneup.jpg')
highlight = pygame.image.load('images/highlight.png')
game_over_continue = pygame.image.load('images/game_over_cont.PNG')
game_over_end = pygame.image.load('images/game_over_end.PNG')
win_continue = pygame.image.load('images/win_choice_cont.PNG')
win_end = pygame.image.load('images/win_choice_end.PNG')
three_guesses = pygame.image.load('images/3_guesses.jpg')
two_guesses = pygame.image.load('images/2_guesses.jpg')
one_guess = pygame.image.load('images/1_guess.jpg')
zero_guesses = pygame.image.load('images/0_guesses.jpg')

# Initialize the game engine
pygame.init()
pygame.display.set_caption('Super Mario Bros. 3 Memory Game')
pygame.mixer.init()

# Import Sound Files
enter = pygame.mixer.Sound('sounds/enter.wav')
move = pygame.mixer.Sound('sounds/move.wav')
flip = pygame.mixer.Sound('sounds/flip.wav')
match = pygame.mixer.Sound('sounds/match.wav')
no_match = pygame.mixer.Sound('sounds/no_match.wav')
game_over = pygame.mixer.Sound('sounds/game_over_man.wav')
lost_life = pygame.mixer.Sound('sounds/lost_life.wav')
for_the_win = pygame.mixer.Sound('sounds/victory.wav')
#victory = pygame.mixer.Sound('sounds/victory.wav')
#falling = pygame.mixer.Sound('sounds/falling.wav')
#finish = pygame.mixer.Sound('sounds/exit.wav')

# Plays entry sound, begins looping game music
enter.play()
pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1)

# Defines background color (RGB) 
black = [0, 0, 0]

# Sets the height/width of the screen
size = [1210, 974]
screen = pygame.display.set_mode(size)

# Causes the program to loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

matches = 0

# Initializes all 18 of our Card objects

current_board = select_board()

card1 = Card(current_board[0])
card2 = Card(current_board[1])
card3 = Card(current_board[2])
card4 = Card(current_board[3])
card5 = Card(current_board[4])
card6 = Card(current_board[5])

card7 = Card(current_board[6])
card8 = Card(current_board[7])
card9 = Card(current_board[8])
card10 = Card(current_board[9])
card11 = Card(current_board[10])
card12 = Card(current_board[11])

card13 = Card(current_board[12])
card14 = Card(current_board[13])
card15 = Card(current_board[14])
card16 = Card(current_board[15])
card17 = Card(current_board[16])
card18 = Card(current_board[17])

# Creates array of all Card objects for looping
full_set = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18]

match_counter = 0
game_won = 18
wrong_guesses = 0
winner = False
end_move_played = False
c_move = False
e_move = False
     
while done == False:

    
    # Game running at 30 frames per second
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicks close button
            done = True # causes program to exit at the beginning of next loop

    # Adds borders and Mario 3 HUD 
    screen.fill(black)

    screen.blit(lborder, (0, 0))
    screen.blit(tborder, (0, 0))
    screen.blit(rborder, (1154, 0))
    
    if wrong_guesses == 0:
        screen.blit(three_guesses, (-15, 730))
    elif wrong_guesses == 1:
        screen.blit(two_guesses, (-15, 730))
    elif wrong_guesses == 2:
        screen.blit(one_guess, (-15, 730))
    else:
        screen.blit(zero_guesses, (-15, 730))
        
    x_card_coord = [160, 310, 460, 610, 760, 910, 160, 310, 460, 610, 760, 910, 160, 310, 460, 610, 760, 910]
    y_card_coord = [130, 130, 130, 130, 130, 130, 370, 370, 370, 370, 370, 370, 600, 600, 600, 600, 600, 600]

    control = 0
    #if winner == False:

    for x in full_set:
        if x.shape == 'mushroom':
            x.flipped = x.place(back, mushroom, x_card_coord[control], y_card_coord[control])
        elif x.shape == 'flower':
            x.flipped = x.place(back, flower, x_card_coord[control], y_card_coord[control])
        elif x.shape == 'star':
            x.flipped = x.place(back, star, x_card_coord[control], y_card_coord[control])
        elif x.shape == 'oneup':
            x.flipped = x.place(back, oneup, x_card_coord[control], y_card_coord[control])
        elif x.shape == 'ten':
            x.flipped = x.place(back, ten, x_card_coord[control], y_card_coord[control])
        elif x.shape == 'twenty':
            x.flipped = x.place(back, twenty, x_card_coord[control], y_card_coord[control])
        control += 1
    
    control = 0

    counter = 0
   
    # Match checking loop 
    for x in full_set:
        
        if x.click == True and x.flipped == False:
            x.click = False
            x.flip_sound_played = False
            
        if x.flipped == True and x.matched == False:


            if counter == 0:
                match1 = x
                counter += 1
            elif counter == 1:
                match2 = x
                if match1.shape == match2.shape:
                    if match1.match_sound_played == False:
                        
                        match.play(0)

                        match1.match_sound_played = True
                        match2.match_sound_played = True

                        match1.matched = True
                        match2.matched = True                   

                        counter = 0    
                        break
                else:
                    if match1.no_match_sound_played == False:
                        no_match.play(0)
                        match1.flipped = False
                        match2.flipped = False
                        match2.flag = True
                        match1.flip_animation = 0
                        match2.flip_animation = 0
                        wrong_guesses += 1
                        counter = 0
                        break
                        
        if counter == 2:
            break
    
    for x in full_set:
        if x.matched == True and x.counted == False:
            x.counted = True
            match_counter += 1
    if match_counter == game_won:
        pygame.mixer.music.stop()
        if winner == False:
            for_the_win.play(0)
            winner = True

        end_mouse = pygame.mouse.get_pos()
        if 542 + 421 > end_mouse[0] > 542 and 488 + 54 > end_mouse[1] > 488 :
        
            screen.blit(win_continue, (240, 265))
            if end_move_played == False:
                end_move_played = True
                move.play(0)
                
        elif 546 + 421 > end_mouse[0] > 546 and 539 + 54 > end_mouse[1] > 539:
            screen.blit(win_end, (240, 265))
            if end_move_played == False:
                end_move_played = True
                move.play(0)
        else:
            screen.blit(win_continue, (240, 265))
            end_move_played = False
                

    pygame.display.flip()

pygame.quit()
