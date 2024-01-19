from settings import *
import os
import itertools


class Card:
    def __init__(self, value, shape):
        self.value = value
        self.shape = shape
        self.image = pygame.image.load(os.path.join("img", "cards", f"{value}_of_{shape}.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))       
        self.rect = self.image.get_rect()
        self.in_hand = False
        self.is_clicked = False
        self.clicked = False
        self.touched = False
        self.rect.y = 420
        self.blit_y = 415
        self.raise_ = self.rect.y - 50
        self.drag = False

    def update(self, num):
        self.rect.x = 50 + 50 * num

        if self.touched:
            self.blit_y += (self.raise_ - self.blit_y) * 0.3

        else:
            self.blit_y += (self.rect.y - self.blit_y) * 0.3

        if self.clicked:
            self.blit_y = 370
            self.rect.y = 370
        else:
            self.rect.y = 420

        if self.drag:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()
            self.blit_y = self.rect.y

        screen.blit(self.image, (self.rect.x , self.blit_y))

        if self.clicked:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 5)

for v, s in itertools.product(values, shapes):
    cards[f"{v}_of_{s}"] = (Card(v, s))
