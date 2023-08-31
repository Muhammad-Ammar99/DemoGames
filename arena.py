import pygame
import random

from colors import WHITE,PURPLE

pygame.init()

# Creating game window
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(("Galaxy Stars"))

# Bg img
bg_img = pygame.image.load("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\bg.jpg").convert()
#  Player img
User_img = pygame.image.load("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\user.png").convert_alpha()
# Coin img
Coin_img = pygame.image.load("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\coin.png").convert_alpha()
# Bomb img
Bomb_img = pygame.image.load("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\tnt.png").convert_alpha() 

# Game Variables

speed_ac = 0.3
speed = 0.2
ac_x_cord = 240
ac_y_cord = 525
bombx = random.randint(20, 570)
bomby = -10
coinx = random.randint(20, 570)
coiny = -10
coinx2 = random.randint(20, 570)
coiny2 = -10
score = 0
font = pygame.font.SysFont(None, 30) 
   

def welcome():
    run = True
    while run:
        screen.fill((255,255,0))
        font = pygame.font.SysFont(None, 30)
        score_text = font.render("Welcome to Galaxy stars",True,PURPLE)
        screen.blit(score_text, (180, 230))
        score_text = font.render("Press Spacebar to Continue",True,PURPLE)
        screen.blit(score_text, (180, 260))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()

# Game loop
def gameloop():
    # Game Variables

    speed_ac = 0.3
    speed = 0.2
    ac_x_cord = 240
    ac_y_cord = 525
    bombx = random.randint(20, 570)
    bomby = -10
    coinx = random.randint(20, 570)
    coiny = -10
    coinx2 = random.randint(20, 570)
    coiny2 = -10
    bombx2 = random.randint(20, 570)
    bomby2 = -10
    score = 0
    font = pygame.font.SysFont(None, 30) 
    exitgame = False
    gameover = False
    
    with open("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\highscore2.txt", "r") as f:
        highscore = f.read().strip()
   
    
    while not exitgame:
        if gameover:
            with open("C:\\Users\Muhammad Ali Ahmer\OneDrive\Desktop\Python\PyGame_Demo\galaxy_arena\DemoGames\\highscore2.txt", "w") as f:
                f.write(str(highscore))
                
            screen.fill(WHITE)
            font = pygame.font.SysFont(None, 30)
            screen_text = font.render("Game Over! Press any key to Continue",True,PURPLE)
            screen.blit(screen_text, [180, 230])
            
                                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    event.key == pygame.K_RETURN
                    gameloop()    
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

            # Updating bomb img and coin img
            bomby+=speed
            bomby2+=speed
            coiny+=speed
            coiny2+=speed
            
            # Reseting the pos of bomb and coin
            if bomby>screen_height:
                bombx = random.randint(20, 570)
                bomby = -10
            
            if bomby2>screen_height:
                bombx2 = random.randint(20, 570)
                bomby2= -10
            
            if coiny>screen_height:
                    coinx = random.randint(20, 570)
                    coiny = -10
                
            if coiny2>screen_height:
                coinx2 = random.randint(20, 570)
                coiny2 = -10

            # Controlling AirCraft 
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                ac_x_cord -= speed_ac
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                ac_x_cord += speed_ac
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                ac_y_cord -= speed_ac
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                ac_y_cord += speed_ac

            # Collision Detection Using Distance Formula
            if ((ac_x_cord - bombx)**2 + (ac_y_cord - bomby)**2)**0.5 < 40: #0.5 is the root so we r removing the root and writing it with 0.5                gameover = True
                gameover =True
                
            if ((ac_x_cord - bombx2)**2 + (ac_y_cord - bomby2)**2)**0.5 < 40: #0.5 is the root so we r removing the root and writing it with 0.5                gameover = True
                gameover =True
                
            if ((ac_x_cord - coinx)**2 + (ac_y_cord - coiny)**2)**0.5 < 50:
                score += 1
                coinx = random.randint(20, 570)
                coiny = -10
                
            if ((ac_x_cord - coinx2)**2 +(ac_y_cord - coiny2)**2)**0.5 < 40:
                score +=1
                coinx2 = random.randint(20,570)
                coiny2 = -10
                
            
            # Bg background
            scaled_img = pygame.transform.scale(bg_img,(screen_width,screen_height))
            screen.blit(scaled_img,(0,0))
            
            # User img
            scaled_User_img = pygame.transform.scale(User_img,(screen_width//8,screen_height//8))
            screen.blit(scaled_User_img,(ac_x_cord,ac_y_cord))
            
            # Tnt img Random pos
            
            scaled_tnt_img = pygame.transform.scale(Bomb_img,(screen_width//15,screen_height//15))
            screen.blit(scaled_tnt_img,(bombx,bomby))
            
        
            # Coin img Random pos    
            scaled_coin_img = pygame.transform.scale(Coin_img,(screen_width//20,screen_height//20))
            screen.blit(scaled_coin_img,(coinx,coiny))
            
            
            #Coin img Random pos 2
            if score>=5:
                scaled_coin_img2 = pygame.transform.scale(Coin_img,(screen_width//20,screen_height//20))
                screen.blit(scaled_coin_img2,(coinx2,coiny2))
            
            # Tnt img Random pos 2
            if score>=5:
                scaled_tnt_img2 = pygame.transform.scale(Bomb_img,(screen_width//15,screen_height//15))
                screen.blit(scaled_tnt_img2,(bombx2,bomby2))
                
            # Check if player goes out of screen boundaries
            if ac_x_cord < 0:
                ac_x_cord = 0
            elif ac_x_cord > screen_width - scaled_User_img.get_width():
                ac_x_cord = screen_width - scaled_User_img.get_width()
            if ac_y_cord < 0:
                ac_y_cord = 0
            elif ac_y_cord > screen_height - scaled_User_img.get_height():
                ac_y_cord = screen_height - scaled_User_img.get_height()
            
            
            # Checking If Highscore is greater Than score
                if score>int(highscore):
                    highscore = score
                
            
            font = pygame.font.SysFont(None, 30)
            score_text = font.render("Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
            highscore = font.render("Highscore: " + str(highscore), True,WHITE)
            screen.blit(highscore, (450, 10))
            pygame.display.update()
           
    # Exit Game
    pygame.quit()
    quit()

welcome()