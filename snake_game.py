import pygame,random
from colors import PURPLE

pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
Blue = (0, 0, 255)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Bg img
img = pygame.image.load("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\Snake_Game\DemoGames\glass.jpg")
img = pygame.transform.scale(img,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Master")
pygame.display.update()
font = pygame.font.SysFont("calibri", 30)
clock = pygame.time.Clock()

def screen_score( text, Color, x, y):
    screen_text = font.render(text, True, Color)
    gameWindow.blit(screen_text, [x,y])   

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
    
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((255,255,0))
        screen_score("Welcome to snake master", black, 250, 250)
        screen_score("Enter Space Bar to play", black, 265, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                event.key == pygame.K_SPACE

                pygame.mixer.music.load("DemoGames//back.mp3")
                pygame.mixer.music.play()

                game_loop()
        pygame.display.update()
        clock.tick(60)

# Game Loop
def game_loop():
    
    # Game specific variables
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    velocity_x = 0
    velocity_y = 0

    snake_size = 15

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    
    
    with open("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\Snake_Game\DemoGames\high_score.txt", "r") as f:
        high_score = f.read()

    snk_list = []
    snk_length = 1
    
    score = 0
    fps = 30
    
    while not exit_game:
        
        if game_over:
            with open("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\Snake_Game\DemoGames\high_score.txt", "w") as f:
                f.write(str(high_score))
            
            gameWindow.fill(white)
            screen_score("Game Over! Press any key to Continue", red, 250,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    event.key == pygame.K_RETURN
                    pygame.mixer.music.load("DemoGames//back.mp3")
                    pygame.mixer.music.play()

                    game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

            
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 8
                        velocity_y = 0
                    if event.key == pygame.K_d:
                        velocity_x = 8
                        velocity_y = 0
                    
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -8
                        velocity_y = 0
                    elif event.key == pygame.K_a:
                        velocity_x = -8
                        velocity_y = 0
                        
                    elif event.key == pygame.K_UP:
                        velocity_y = -8
                        velocity_x = 0
                    elif event.key == pygame.K_w:
                        velocity_y = -8
                        velocity_x = 0
                        
                    elif event.key == pygame.K_DOWN:
                        velocity_y = 8
                        velocity_x = 0
                    elif event.key == pygame.K_s:
                        velocity_y = 8
                        velocity_x = 0
                    elif event.key == pygame.K_LSHIFT:
                        score+=10

                        
            snake_x+=velocity_x
            snake_y+=velocity_y
            
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=10
                food_x = random.randint(30,screen_width/2)
                food_y = random.randint(40,screen_height/2)
                snk_length+=5
            
            
            if score>int(high_score):
                high_score = score
                    
            gameWindow.fill(white)
            gameWindow.blit(img,(0,0))
            screen_score("Score: "+ str(score) + "  High Score: "+ str(high_score), PURPLE, 5, 5)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if head in snk_list[:-2]:
                game_over = True
                pygame.mixer.music.load("DemoGames//end.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("DemoGames//end.mp3")
                pygame.mixer.music.play()

            
            if len(snk_list) > snk_length:
                del snk_list[0]
        
            plot_snake(gameWindow, black, snk_list, snake_size)
            
            pygame.draw.circle(gameWindow,red,(food_x,food_y),5)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()