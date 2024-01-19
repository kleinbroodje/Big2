import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("鋤大弟")

shapes = ["diamonds", "spades", "hearts", "clubs"]
values = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
cards = {}
scale = 0.2
font = pygame.font.Font("Nabla.ttf", 52)

