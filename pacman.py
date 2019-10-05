import pygame
from pygame.locals import *
from numpy import loadtxt
import time
from random import randint as ri

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
GHOST_COLOR = [ pygame.Color(50, 205, 50), pygame.Color(169, 169, 169), pygame.Color(225, 225, 225)]
COIN_COLOR = pygame.Color(128, 128, 128)
POINT_COLOR = pygame.Color(225, 225, 225)
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)
SCORE = 0
direction = 'right'
NUMBER_OF_COINS = 0
COINS_TAKEN = 0



#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws pacman animation
i = 0
def draw_pacman(screen, pos, direction):
	global i
	if direction == 'right':
		direction = 0
	if direction == 'left':
		direction = 180
	if direction == 'up':
		direction = 90
	if direction == 'down':
		direction = 270

	pixels = pixels_from_points(pos)
	if i <= 3:
		screen.blit(pygame.transform.rotate(pygame.transform.scale(pacman1,(30,30)),direction),pixels)
	elif i <= 6:
		screen.blit(pygame.transform.rotate(pygame.transform.scale(pacman2,(30,30)),direction),pixels)	

	elif i <= 9:
		screen.blit(pygame.transform.rotate(pygame.transform.scale(pacman3,(30,30)),direction),pixels)	

	elif i <= 12:
		screen.blit(pygame.transform.rotate(pygame.transform.scale(pacman4,(30,30)),direction),pixels)
	i +=1
	if i == 13:
		i = 0


#draws ghost
def draw_ghost(screen, pos, i = 1): 
	pixels = pixels_from_points(pos)
	if i == 0:
		screen.blit(pygame.transform.scale(g11,(30,30)),pixels)	

	if i == 1:
		screen.blit(pygame.transform.scale(g21,(30,30)),pixels)	

	if i == 2:
		screen.blit(pygame.transform.scale(g31,(30,30)),pixels)	

#draw tunnel for teleportation
def draw_tunnel(screen, pos,):
	pixels = pixels_from_points(pos)
	screen.blit(pygame.transform.scale(t, (30,30)),pixels)

# draws coins
def draw_coin(screen, pos):
	global NUMBER_OF_COINS
	pixels = pixels_from_points(pos)
	pixels = [pixels[0],pixels[1]]
	pixels[0] += WIDTH//2
	pixels[1] +=HEIGHT//2
	pygame.draw.circle(screen, COIN_COLOR, pixels,7)
	
#draws points
def draw_point(screen, pos):
	global NUMBER_OF_COINS
	pixels = pixels_from_points(pos)
	pixels = [pixels[0],pixels[1]]
	pixels[0] += WIDTH//2
	pixels[1] +=HEIGHT//2
	pygame.draw.circle(screen, POINT_COLOR, pixels,2)
	

# Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#function to write text the screen
font_name = pygame.font.match_font('arial', bold= True)
def draw_text(screen, text, size, x, y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, (255,255,255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	screen.blit(text_surface, text_rect)



#Initializing pygame
pygame.init()
pygame.display.set_caption('Pacman by-Nikunj Singhal')
screen = pygame.display.set_mode((650,520), 0)
background = pygame.surface.Surface((650,520)).convert()




#Initializing variables
layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = [1,1]
ghost1_position = [6,6]
ghost2_position = [9,6]
ghost3_position = [6,9]
background.fill((0,0,0))
pacman1 = pygame.image.load("./pictures/pacman1.gif").convert()
pacman2 = pygame.image.load("./pictures/pacman2.gif").convert()
pacman3 = pygame.image.load('./pictures/pacman3.gif').convert()
pacman4 = pygame.image.load('./pictures/pacman4.gif').convert()
g11 = pygame.image.load('./pictures/0.png').convert()
g21 = pygame.image.load('./pictures/9.png').convert()
g31 = pygame.image.load('./pictures/21.png').convert()
t = pygame.image.load('./pictures/tunnel.jpg').convert()


slowit1 = 0
slowit2 = 0
slowit3 = 0
def move_ghost(ghost1_position,ghost2_position,ghost3_position):

	global slowit1,slowit2, slowit3
	if slowit1 % 2 == 0:
		

		
		b1=ri(0,1)
		if b1==0:
			a1=ri(-1,1)
			if layout[ghost1_position[1]+a1][ghost1_position[0]] != 'w' :

				ghost1_position = [ghost1_position[0], ghost1_position[1] +a1]
		else:
			a1=ri(-1,1)
			if layout[ghost1_position[1]][ghost1_position[0]+a1] != 'w' and layout[ghost1_position[1]][ghost1_position[0] + a1] != 't'  :
				ghost1_position = [ghost1_position[0]+a1, ghost1_position[1]]

		
	if slowit2 % 2 ==0:
		b2=ri(0,1)
		if b2 == 0:
			a2 = ri(-1,1)
			if layout[ghost2_position[1]+a2][ghost2_position[0]] != 'w' :
				ghost2_position = [ghost2_position[0], ghost2_position[1] +a2]
		else:
			a2=ri(-1,1)
			if layout[ghost2_position[1]][ghost2_position[0]+a2] != 'w' and layout[ghost2_position[1]][ghost2_position[0]+a2] != 't' :
				ghost2_position = [ghost2_position[0]+a2, ghost2_position[1]]
		

	if slowit3 % 2 ==0:
		b3=ri(0,1)
		if b3 == 0:
			a3 = ri(-1,1)
			if layout[ghost3_position[1]+a3][ghost3_position[0]] != 'w' :
				ghost3_position = [ghost3_position[0], ghost3_position[1] +a3]
		else:
			a3=ri(-1,1)
			if layout[ghost3_position[1]][ghost3_position[0]+a3] != 'w' and layout[ghost3_position[1]][ghost3_position[0]+a3] != 't':
				ghost3_position = [ghost3_position[0]+a3, ghost3_position[1]]

	slowit1 += 1
	slowit2 += 1
	slowit3 += 1
	return [ghost1_position, ghost2_position, ghost3_position]




for row in range(rows):
	NUMBER_OF_COINS += list(layout[row]).count('.')+ list(layout[row]).count('c')


# Main game loop 
while True:

	while COINS_TAKEN != NUMBER_OF_COINS:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		screen.blit(background, (0,0))

	  #In the board, '.' denote 1 point, 'w' are the walls, 'c' are the coins worth 10 points
		for col in range(cols):
			for row in range(rows):
				value = layout[row][col]
				pos = (col, row)
				if value == 'w':
					draw_wall(screen, pos)
				elif value == 'c':
					draw_coin(screen, pos)
				elif value == '.' :
					draw_point(screen, pos)
				elif value == 't' :
					draw_tunnel(screen, pos)


		#Drawing Ghosts
		draw_ghost(screen, ghost1_position, 0)
		draw_ghost(screen, ghost2_position, 1)
		draw_ghost(screen, ghost3_position, 2)
		keys = pygame.key.get_pressed()

		if pacman_position == (16,7) and keys[K_RIGHT]:
			pacman_position = (0,7)
		if pacman_position == (0, 7) and keys[K_LEFT]:
			pacman_position = (16, 7)
		
		if keys[pygame.K_LEFT] and layout[pacman_position[1]][pacman_position[0]-1]!='w' :
			move_direction = LEFT
			pacman_position = add_to_pos(pacman_position, move_direction)
			direction = 'left'

		if keys[pygame.K_RIGHT] and layout[pacman_position[1]][pacman_position[0]+1]!='w' :
			move_direction = RIGHT
			pacman_position = add_to_pos(pacman_position, move_direction)
			direction = 'right'


		if keys[pygame.K_UP] and layout[pacman_position[1]-1][pacman_position[0]]!='w' :
			move_direction = TOP
			pacman_position = add_to_pos(pacman_position, move_direction)
			direction = 'up'

		if keys[pygame.K_DOWN] and layout[pacman_position[1]+1][pacman_position[0]]!='w' :
			move_direction = DOWN
			pacman_position = add_to_pos(pacman_position, move_direction)
			direction = 'down'
			
		if layout[pacman_position[1]][pacman_position[0]]=='c':
			COINS_TAKEN += 1
			layout[pacman_position[1]][pacman_position[0]]='n'
			SCORE += 10
			

		if layout[pacman_position[1]][pacman_position[0]]=='.':
			COINS_TAKEN += 1
			layout[pacman_position[1]][pacman_position[0]]='n'
			SCORE +=1
		

		[ghost1_position, ghost2_position, ghost3_position]=move_ghost(ghost1_position, ghost2_position, ghost3_position)
		draw_text(screen, 'SCORE:', 40, pixels_from_points((18,4))[0]+10, pixels_from_points((10,4))[1] )
		draw_text(screen, str(SCORE), 35, pixels_from_points((18,5))[0], pixels_from_points((10,5))[1] )
		

		draw_pacman(screen, pacman_position, direction  )
		if list(pacman_position) == ghost1_position:
			SCORE -= 5
			pixel = pixels_from_points(pacman_position)
			pygame.draw.circle(screen, (255, 0, 0), (pixel[0] + HEIGHT//2, pixel[1]+WIDTH//2),19)
			pacman_position = (1,1)
		if list(pacman_position) == ghost2_position:
			SCORE -= 5
			pixel = pixels_from_points(pacman_position)
			pygame.draw.circle(screen, (255, 0, 0), (pixel[0] + HEIGHT//2, pixel[1]+WIDTH//2),19)
			pacman_position = (1,1)
		if list(pacman_position) == ghost3_position:
			SCORE -= 5
			pixel = pixels_from_points(pacman_position)
			pygame.draw.circle(screen, (255, 0, 0), (pixel[0] + HEIGHT//2, pixel[1]+WIDTH//2),19)
			pacman_position = (1,1)

		#Update the display
		pygame.display.update()

		#Wait for a while, computers are very fast.
		pygame.time.delay(90)


	screen.fill(pygame.Color(0, 0, 0))
	draw_text(screen, 'GAME OVER!', 70, pixels_from_points((8,5))[0], pixels_from_points((8,5))[1] )
	draw_text(screen, 'YOUR SCORE IS: '+str(SCORE), 20, pixels_from_points((8,8))[0], pixels_from_points((8,8))[1] )
	draw_text(screen, 'PRESS Q TO QUIT AND C TO PLAY AGAIN: ', 20, pixels_from_points((8,10))[0], pixels_from_points((8,10))[1] )
	screen.blit(screen,(0,0))
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN and event.key == K_q:
			exit()
		if event.type == KEYDOWN and event.key == K_c:
			SCORE = 0
			COINS_TAKEN = 0
			layout = loadtxt('layout.txt',dtype=str)
			pacman_position = (1,1)
			ghost1_position = [6,6]
			ghost2_position = [9,6]
			ghost3_position = [6,9]
			direction = 'right'
