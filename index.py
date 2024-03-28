 
import pygame 
  
screen = pygame.display.set_mode((1000, 1000)) 
pygame.display.set_caption('LA | Mini create task - TikTakToe') 

def draw_board(screen):
	# Lines down
	pygame.draw.line(screen, "#000000", [screen.get_width() / 3, 0], [screen.get_width() / 3, screen.get_height()], 20)
	pygame.draw.line(screen, "#000000", [(screen.get_width() / 3) * 2, 0], [(screen.get_width() / 3) * 2, screen.get_height()], 20)

	# Lines across
	pygame.draw.line(screen, "#000000", [0, screen.get_height()/3], [screen.get_width(), screen.get_height()/3], 20)
	pygame.draw.line(screen, "#000000", [0, (screen.get_height()/3) * 2], [screen.get_width(), (screen.get_height()/3) * 2], 20)

def draw_circle(x, y):
	pygame.draw.circle(screen, "#000000", [x, y], 40, 0)
	

background_color = (234, 212, 252) 
currentTurn = 'X'
placesUsed = []

screen.fill(background_color) 
  
pygame.display.flip() 

running = True
  
while running: 
	
	for event in pygame.event.get():
	  
		if event.type == pygame.QUIT:
			running = False

	draw_board(screen)
	
	draw_circle(screen.get_width() / 6, screen.get_height() / 6) # Top left circle

	# pygame.draw.line(screen, "#000000", [(screen.get_width() / 3) * x, (screen.get_height() / 3) * y], [(screen.get_width() / 3) * (x + 1), (screen.get_height() / 3) * (y + 1)], 20)
	# pygame.draw.line(screen, "#000000", [(screen.get_width() / 3) * (x + 1), (screen.get_height() / 3) * y], [(screen.get_width() / 3) * x, (screen.get_height() / 3) * (y + 1)], 20)

	pygame.display.flip()
