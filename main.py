
import pygame

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Geeksforgeeks')

screen.fill((0,0,255)))

running = True

while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
