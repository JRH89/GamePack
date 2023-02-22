import pygame
from pygame.locals import *
def start_game():
    
    import random
    import sys

    size = width, height = (800, 800)
    road_w = int(width/1.6)
    roadmark_w = int(width/80)
    right_lane = width/2 + road_w/4
    left_lane = width/2 - road_w/4
    speed = 1

    pygame.init()
    running = True
    screen = pygame.display.set_mode((size))
    pygame.display.set_caption("Racer")
    screen.fill((60, 150, 50))


    pygame.display.update()

    car = pygame.image.load("car.png")
    car_loc = car.get_rect()
    car_loc.center = right_lane, height*0.8

    car2 = pygame.image.load("car2.png")
    car2_loc = car.get_rect()
    car2_loc.center = left_lane, height*0.2


    score = 0
    font = pygame.font.Font(None, 36)
    start_text = font.render("Press 'Space' to Start", True, (255, 255, 255))
    screen.blit(start_text, (width/2 - start_text.get_width()/2, height/2 - start_text.get_height()/2))
    pygame.display.update()

    start = False

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if start:
            break

    counter = 0

    while running:
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(int(speed)), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        counter += 1
        if counter == 5000:
            speed += 0.6
            counter = 0
            print("level up", speed)
            pygame.display.update()

        car2_loc[1] += speed
        if car2_loc[1] > height:
            if random.randint(0,1) == 0:
                car2_loc.center = right_lane, -200
            else:
                car2_loc.center = left_lane, -200
        
        if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 200:
            font = pygame.font.Font(None, 72)
            gameover_text = font.render("Game Over, Loser!", True, (255, 0, 0))
            screen.blit(gameover_text, (width/2 - gameover_text.get_width()/2, height/2 - gameover_text.get_height()/2))
            pygame.display.update()
            
            break
            
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    car_loc = car_loc.move([-int(road_w/2), 0])
                if event.key in [K_d, K_RIGHT]:
                    car_loc = car_loc.move([+int(road_w/2), 0])
        
                
        pygame.draw.rect(
            screen,
            (50, 50, 50), (width/2-road_w/2, 0, road_w, height)
        )

        pygame.draw.rect(
            screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height)
        )

        pygame.draw.rect(
            screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
        )

        pygame.draw.rect(
            screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
        )
            
        screen.blit(car, car_loc)
        screen.blit(car2, car2_loc)
        pygame.display.update()

        
    pygame.quit()
    
if __name__ == "__main__":
    start_game()