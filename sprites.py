import pygame
import screens
LAYER_FG = 3
LAYER_KUGEL = 2
LAYER_HG = 1
active_sprites:pygame.sprite.LayeredUpdates = pygame.sprite.LayeredUpdates() # Alle aktiven Sprites des Spiels selbst

def bewegung_erlaubt(rect:pygame.Rect, direction:str):
    pass