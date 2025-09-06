import pygame
import KugelQuest
import sprites
class Kugel(pygame.sprite.Sprite):
	def __init__(self):
		#Definition aller Sprites der Kugel
		super().__init__()
		self.image_0 = pygame.image.load(KugelQuest.DATA_DIR + "Kugel.png").convert_alpha()
		self.image_0.set_colorkey((255, 255, 255))
		self.image_dl = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_down_left.png").convert_alpha()
		self.image_dl.set_colorkey((255, 255, 255))
		self.image_dr = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_down_right.png").convert_alpha()
		self.image_dr.set_colorkey((255, 255, 255))
		self.image_d = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_down.png").convert_alpha()
		self.image_d.set_colorkey((255, 255, 255))
		self.image_l = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_left.png").convert_alpha()
		self.image_l.set_colorkey((255, 255, 255))
		self.image_r = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_right.png").convert_alpha()
		self.image_r.set_colorkey((255, 255, 255))
		self.image_ul = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_up_left.png").convert_alpha()
		self.image_ul.set_colorkey((255, 255, 255))
		self.image_ur = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_up_right.png").convert_alpha()
		self.image_ur.set_colorkey((255, 255, 255))
		self.image_u = pygame.image.load(KugelQuest.DATA_DIR + "Kugel_up.png").convert_alpha()
		self.image_u.set_colorkey((255, 255, 255))
		#Startsprite setzen
		self.image = self.image_0
		self.rect = self.image_0.get_rect()
		self.rect.center = (KugelQuest.SCREEN_WIDTH/2,KugelQuest.SCREEN_HEIGHT/2)
		self.speed = 5
		#self._layer = sprites.LAYER_KUGEL
	def update(self):
		keys = pygame.key.get_pressed()
		bewegung = "0"
		if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
			if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
				bewegung = "ul"
			elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
				bewegung = "dl"
			else:
				bewegung = "l"
		elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
			if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
				bewegung = "ur"
			elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
				bewegung = "dr"
			else:
				bewegung = "r"
		else: 
			if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
				bewegung = "u"
			elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
				bewegung = "d"
		self.image = eval(f"self.image_{bewegung}")
		current_speed = self.speed if len(bewegung) == 1 else self.speed - 2
		if 'l' in bewegung:
			if self.rect.left > current_speed: 
				self.rect.left -= current_speed
				if not sprites.bewegung_erlaubt(self.rect): self.rect.left += current_speed
		if 'r' in bewegung:
			if self.rect.right < KugelQuest.SCREEN_WIDTH - current_speed: 
				self.rect.left += current_speed
				if not sprites.bewegung_erlaubt(self.rect): self.rect.left -= current_speed
		if 'u' in bewegung:
			if self.rect.top > current_speed: 
				self.rect.top -= current_speed
				if not sprites.bewegung_erlaubt(self.rect): self.rect.top += current_speed
		if 'd' in bewegung:
			if self.rect.bottom < KugelQuest.SCREEN_HEIGHT - current_speed: 
				self.rect.top += current_speed
				if not sprites.bewegung_erlaubt(self.rect): self.rect.top -= current_speed