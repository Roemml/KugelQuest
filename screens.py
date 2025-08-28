import pygame
import KugelQuest
import Roemdules.utils as rd_utils
HG00 = KugelQuest.DATA_DIR + "HG00.png"
HGM00 = HG00
class Hintergrund(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(HG00).convert()
        self.rect = self.image.get_rect()
        self.map = rd_utils.get_Surface_map(pygame.image.load(HGM00))