import pygame
import os
import sys


pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('свой курсор мыши')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def show(image, coords):
    screen.blit(image, coords)


running = True
image = load_image("arrow.png")
while running:
    screen. fill('black')
    if pygame.mouse.get_focused() == True:
        pygame.mouse.set_visible(False)
        coods = pygame.mouse.get_pos()
        show(image, coods)
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()