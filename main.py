from tracemalloc import start
import pygame, numpy as np, random, time, sys

pygame.init()

RED = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREY = (100, 100, 100)

# Game Mode
binary = True
integer = False

def board_create(width=4, height=None):
    if height is None:
        height = width

    box_size = 100
    gap = 5
    border_x = (screen.get_width() - (width * (box_size + gap) - gap))/2
    border_y = (screen.get_height() - (height * (box_size + gap) - gap))/2

    board = [pygame.Rect(border_x + (box_size + gap) * i,
                         border_y + (box_size + gap) * j,
                         box_size, box_size) for i in range(height) for j in range(width)]

    sprite2num = {tuple(s): n for n, s in enumerate(board)}
    num2sprite = {n: s for n, s in enumerate(board)}
    return board, sprite2num, num2sprite

pattern = []
num_list = []
target_sum = 0

def draw(clicked):
    for i in sprites:
        pygame.draw.rect(screen, LIGHT_GREY, i)
    for j in clicked:
        pygame.draw.rect(screen, GREEN, j)

def show_pattern():
    
    pattern.clear()
    num_list.clear()

    new_pattern = list(np.random.permutation(np.arange(0,15))[:5])
    for x in new_pattern:
        pattern.append(x)

    for i in pattern:
        draw([])
        new_rect = pygame.draw.rect(screen, (255, 0, 0), sprites[i])

        if (binary):
            rand = random.randint(0,1)
            num_list.append(rand)
            num_text = pygame.font.SysFont('Times New Roman', 32).render(str(rand), True, RED)
            text_rect = num_text.get_rect(center = new_rect.center)
            screen.blit(num_text, text_rect)

        if (integer):
            rand = random.randint(1,9)
            num_list.append(rand)
            num_text = pygame.font.SysFont('Times New Roman', 32).render(str(rand), True, RED)
            text_rect = num_text.get_rect(center = new_rect.center)
            screen.blit(num_text, text_rect)

        

        pygame.display.flip()
        time.sleep(0.5)
    
    return sum(num_list)


WINDOW_SIZE = [425, 600]
screen = pygame.display.set_mode(WINDOW_SIZE) 

sprites, sprite_to_number, number_to_sprite = board_create()
clicked_sprites = []
clicked_order = []
trial_counter = 1
start_time = 0
answer = ''

sum_entered = False
round_done = True
first_round = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.collidepoint(pygame.mouse.get_pos())]
            if len(clicked_sprites) != 0:
                clicked_order.append(sprite_to_number[tuple(clicked_sprites[0])])
        
    draw(clicked_sprites)
        
    if round_done:
        target_sum = show_pattern()
        start_time = time.time()
        clicked_sprites = []
        clicked_order = []
        first_round = False
        round_done = False

    if len(clicked_order) == 5:
        end_time = time.time()
        duration = end_time - start_time
        sum_result = ''

        if first_round is False:
            while (sum_entered is False):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            sum_entered = True
                        elif event.key == pygame.K_BACKSPACE:
                            answer = answer[:-1]
                        else:
                            answer += event.unicode 

        if (integer or binary):
            if target_sum == int(answer):
                sum_result = 'Correct'
            else:
                sum_result = 'Incorrect'
        else:
            sum_result = 'No'


        if clicked_order == pattern[:len(clicked_order)+1]:
            print(f'Trial #{trial_counter}: Pattern: {pattern} -> Clicked Order {clicked_order}\nCorrect Sequence\nTarget Sum: {str(target_sum)} -> Entered Sum: {answer}\n{sum_result} Summation\nDuration: {duration}')
        else:
            print(f'Trial #{trial_counter}: Pattern: {pattern} -> Clicked Order {clicked_order}\nIncorrect Sequence\nTarget Sum: {str(target_sum)} -> Entered Sum: {answer}\n{sum_result} Summation\nDuration: {duration}')

        time.sleep(3)
        start_time = 0
        end_time = 0
        target_sum = 0
        answer = ''
        trial_counter += 1
        sum_entered = False
        round_done = True

    if len(clicked_order) >= len(pattern):
        clicked_order = clicked_order[:len(clicked_order)]

    pygame.display.flip()

pygame.quit()  
