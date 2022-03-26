
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
 
# cell dimensions 
WIDTH = 100
HEIGHT = 100 
MARGIN = 5
 
grid = []
for row in range(4):
    grid.append([])
    for column in range(4):
        grid[row].append(0)  
 
pygame.init()
 
WINDOW_SIZE = [425, 425]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Reaction Game")
 
done = False
 
clock = pygame.time.Clock()
 
# -------- Main Program -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(4):
        for column in range(4):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
 
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()
