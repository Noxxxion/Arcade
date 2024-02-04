# TO-DO: Create a Pong game using Python and Pygame.
# GOAL: A single player Graphical recreation of the classic Pong game. With Possible AI opponent or local split screen multiplayer.

# Import the Pygame library --------------------------------------------------->
import pygame
import random
import time

# Initialize Pygame ----------------------------------------------------------->
pygame.init()

# Set the screen dimensions ---------------------------------------------------->
screen_width = 800
screen_height = 600

# Set the screen size ---------------------------------------------------------->
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the screen title ---------------------------------------------------------->
title_name = "Pong"
pygame.display.set_caption(title_name)

# Set the screen background color ---------------------------------------------->
background_color = (0, 0, 0) # Black

# Set the screen refresh rate -------------------------------------------------->
clock = pygame.time.Clock() # Set the clock to control the screen refresh rate.

# Set the game variables ------------------------------------------------------->
player_width = 15 # Width of the player paddle
player_height = 100 # Height of the player paddle
player_speed = 5 # Speed of the player paddle

opponent_width = 15 # Width of the opponent paddle
opponent_height = 100 # Height of the opponent paddle
opponent_speed = 5 # Speed of the opponent paddle

ball_width = 15 # Width of the ball
ball_height = 15 # Height of the ball
base_ball_speed = 2 # Base speed of the ball
ball_speed = base_ball_speed # Speed of the ball
ball_x_speed = ball_speed # X speed of the ball
ball_y_speed = ball_speed # Y speed of the ball

# Set the game colors ---------------------------------------------------------->
white = (255, 255, 255) # White
red = (255, 0, 0) # Red
blue = (0, 0, 255) # Blue
green = (0, 255, 0) # Green
yellow = (255, 255, 0) # Yellow
orange = (255, 165, 0) # Orange
purple = (128, 0, 128) # Purple
pink = (255, 192, 203) # Pink
brown = (165, 42, 42) # Brown
cyan = (0, 255, 255) # Cyan
magenta = (255, 0, 255) # Magenta
grey = (128, 128, 128) # Grey
black = (0, 0, 0) # Black

# Set the game fonts ----------------------------------------------------------->
font = pygame.font.Font(None, 36) # Set the font for the game

# Set the game text ----------------------------------------------------------->
player_score = 0 # Set the player score
opponent_score = 0 # Set the opponent score
player_text = font.render("Player: " + str(player_score), 1, white) # Set the player text
opponent_text = font.render("Opponent: " + str(opponent_score), 1, white) # Set the opponent text

# Set the game paddles ---------------------------------------------------------->
player_x = 50 # Set the player paddle x position
player_y = (screen_height / 2) - (player_height / 2) # Set the player paddle y position
player_move_up = False # Set the player move up variable
player_move_down = False # Set the player move down variable

opponent_x = screen_width - 50 - opponent_width # Set the opponent paddle x position
opponent_y = (screen_height / 2) - (opponent_height / 2) # Set the opponent paddle y position
opponent_move_up = False # Set the opponent move up variable
opponent_move_down = False # Set the opponent move down variable

# Set the game ball ----------------------------------------------------------->
ball_x = (screen_width / 2) - (ball_width / 2) # Set the ball x position
ball_y = (screen_height / 2) - (ball_height / 2) # Set the ball y position
ball_move_up = False # Set the ball move up variable
ball_move_down = False # Set the ball move down variable
ball_move_left = False # Set the ball move left variable
ball_move_right = False # Set the ball move right variable

# Set the game loop ----------------------------------------------------------->
running = True # Set the running variable

# Set the game functions ------------------------------------------------------->
def player_paddle():
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

def opponent_paddle():
    pygame.draw.rect(screen, red, (opponent_x, opponent_y, opponent_width, opponent_height))

def ball():
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_width, ball_height))

def player_score_text():
    global player_text
    player_text = font.render("Player: " + str(player_score), 1, white) # Set the player text
    screen.blit(player_text, (50, 50))

def opponent_score_text():
    global opponent_text
    opponent_text = font.render("Opponent: " + str(opponent_score), 1, white) # Set the opponent text
    screen.blit(opponent_text, (screen_width - 250, 50))

def ball_reset():
    global ball_x, ball_y, ball_x_speed, ball_y_speed, ball_speed
    ball_x = (screen_width / 2) - (ball_width / 2)
    ball_y = (screen_height / 2) - (ball_height / 2)
    ball_x_speed = ball_speed
    ball_y_speed = ball_speed
    ball_speed = base_ball_speed

def ball_speed_increase():
    global ball_speed
    ball_speed += 0.5 # Increase the ball speed by 0.5

def ball_speed_decrease():
    global ball_speed
    ball_speed -= 0.5 # Decrease the ball speed by 0.5

def ball_speed_reset():
    global ball_speed
    ball_speed = base_ball_speed

def player_score_increase():
    global player_score
    player_score += 1 # Increase the player score by 1
    player_text = font.render("Player: " + str(player_score), 1, white) # Set the player text

def opponent_score_increase():  
    global opponent_score
    opponent_score += 1 # Increase the opponent score by 1
    opponent_text = font.render("Opponent: " + str(opponent_score), 1, white) # Set the opponent text

def player_paddle_collision():
    global ball_x_speed
    ball_x_speed = -ball_x_speed

def opponent_paddle_collision():
    global ball_x_speed
    ball_x_speed = -ball_x_speed

def wall_collision():
    global ball_y_speed
    ball_y_speed = -ball_y_speed

def player_paddle_movement():
    global player_y, player_move_up, player_move_down
    if player_move_up:
        player_y -= player_speed
    if player_move_down:
        player_y += player_speed
    if player_y <= 0:
        player_y = 0
    if player_y >= screen_height - player_height:
        player_y = screen_height - player_height

def opponent_paddle_movement():
    global opponent_y, opponent_move_up, opponent_move_down
    if opponent_move_up:
        opponent_y -= opponent_speed
    if opponent_move_down:
        opponent_y += opponent_speed
    if opponent_y <= 0:
        opponent_y = 0
    if opponent_y >= screen_height - opponent_height:
        opponent_y = screen_height - opponent_height

def ball_movement():
    global ball_x, ball_y, ball_x_speed, ball_y_speed
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    # Top wall collision
    if ball_y <= 0:
        wall_collision() # Call the wall collision function
    # Bottom wall collision
    if ball_y >= screen_height - ball_height:
        wall_collision() # Call the wall collision function
    # Player score increase
    if ball_x <= 0:
        opponent_score_increase() # Call the opponent score increase function
        ball_reset() # Call the ball reset function
    # Opponent score increase
    if ball_x >= screen_width - ball_width:
        player_score_increase() # Call the player score increase function
        ball_reset() # Call the ball reset function
    # Player paddle collision
    if ball_x <= player_x + player_width and ball_y >= player_y and ball_y <= player_y + player_height:
        player_paddle_collision() # Call the player paddle collision function
    # Opponent paddle collision
    if ball_x >= opponent_x - opponent_width and ball_y >= opponent_y and ball_y <= opponent_y + opponent_height:
        opponent_paddle_collision() # Call the opponent paddle collision function



# Set the game loop ----------------------------------------------------------->
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_move_up = True
            if event.key == pygame.K_s:
                player_move_down = True
            if event.key == pygame.K_UP:
                opponent_move_up = True
            if event.key == pygame.K_DOWN:
                opponent_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_move_up = False
            if event.key == pygame.K_s:
                player_move_down = False
            if event.key == pygame.K_UP:
                opponent_move_up = False
            if event.key == pygame.K_DOWN:
                opponent_move_down = False

    player_paddle_movement() # Call the player paddle movement function
    opponent_paddle_movement() # Call the opponent paddle movement function
    ball_movement() # Call the ball movement function

    screen.fill(background_color) # Set the screen background color
    player_paddle() # Call the player paddle function
    opponent_paddle() # Call the opponent paddle function
    ball() # Call the ball function
    player_score_text() # Call the player score text function
    opponent_score_text() # Call the opponent score text function
    
    pygame.display.flip() # Update the display
    clock.tick(60) # Set the screen refresh rate to 60 frames per second

# Set the game over screen ---------------------------------------------------->   
game_over = True # Set the game over variable
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    screen.fill(background_color) # Set the screen background color
    player_paddle() # Call the player paddle function
    opponent_paddle() # Call the opponent paddle function
    ball() # Call the ball function
    player_score_text() # Call the player score text function
    opponent_score_text() # Call the opponent score text function

    if player_score > opponent_score:
        # Set the winner text to Player Wins with playerscore Points!
        winner_text = font.render("Player Wins with " + str(player_score) + " Points!", 1, white)
    elif player_score < opponent_score:
        # Set the winner text to Opponent Wins with opponentscore Points!
        winner_text = font.render("Opponent Wins with " + str(opponent_score) + " Points!", 1, white)
    else:
        winner_text = font.render("It's a draw!", 1, white)

    screen.blit(winner_text, (screen_width / 2 - 200, screen_height / 2 - 50)) # Set the winner text position
    pygame.display.flip() # Update the display
    clock.tick(60) # Set the screen refresh rate to 60 frames per second    

# Quit Pygame ------------------------------------------------------------------>
pygame.quit()

