import pygame
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)
print(population.generation)

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10

    while True:
        quit_game()
         
        config.window.fill((0, 0, 0))
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render("generations  ==>"+str(population.generation), False, (244, 0, 0))
       
        # Spawn Ground
        config.ground.draw(config.window)
        config.window.blit(text_surface, (420,components.Ground.ground_level+50))
        # Spawn Pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
            text_surface2 = my_font.render("number of child=="+str(population.jinda), False, (244, 0, 0))
            config.window.blit(text_surface2, (680,components.Ground.ground_level+50))

        else:
            config.pipes.clear()
            population.natural_selection()

        clock.tick(60)
        pygame.display.flip()

main()