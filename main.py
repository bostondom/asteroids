 # this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        
        dt = (clock.tick(60)) / 1000.0
        
        for object in updatable:
            object.update(dt)
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):         
                    shot.kill()
                    asteroid.split()
                    break
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                return
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
    