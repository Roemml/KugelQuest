import pygame
# import pygame._sdl2.controller
import logging
import sys
import os
import Roemdules.utils as rd_utils
import sprites
import Kugel
GAME_DIR = rd_utils.get_exepath(__file__)
DATA_DIR:str = os.path.join(GAME_DIR, "data", "")
SCREEN_WIDTH:int = 1200 # Breite des Spiel Fensters
SCREEN_HEIGHT:int = 900 # Höhe des Spiel Fensters


if __name__ == "__main__":
    logging.basicConfig(
        # filename=f"{GAME_DIR}KugelQuest.log", filemode='w',
        format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.DEBUG)
    logging.debug("Start!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(pygame.image.load(f"{DATA_DIR}Kugel.png"))
    pygame.display.set_caption("KugelQuest")
    # pygame.display.toggle_fullscreen()
    # pygame.init()
    # pygame._sdl2.controller.init()
    timer = pygame.time.Clock()
    ende = False
    sprites.active_sprites.add(Kugel.Kugel(), layer=sprites.LAYER_KUGEL
                       )
    while ende == False:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or (keys[pygame.K_LALT] and keys[pygame.K_q]): 
            ende = True
        for event in events:
            if event.type == pygame.QUIT:
                ende=True
        sprites.active_sprites.update()
        screen.fill((125, 125, 125))
        sprites.active_sprites.draw(screen)
        pygame.display.flip()
        timer.tick(60)
    logging.debug("Ende!")