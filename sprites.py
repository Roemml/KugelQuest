import pygame
import screens
LAYER_FG = 3
LAYER_KUGEL = 2
LAYER_HG = 1
active_sprites:pygame.sprite.LayeredUpdates = pygame.sprite.LayeredUpdates() # Alle aktiven Sprites des Spiels selbst

def bewegung_erlaubt(rect:pygame.Rect):
    hg = next((s for s in active_sprites if isinstance(s, screens.Hintergrund)), None)
    for height in range(rect.top,rect.bottom + 1):
        for width in range(rect.left,rect.right + 1):
            if hg.map[height][width] == (0, 0, 0): return False
    return True
    
    
