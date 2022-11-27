import pygame

try:
    w, h = [int(i) for i in input().split()]

    def draw():
        screen.fill('black')
        pygame.draw.rect(screen, 'red', (1, 1, w - 1, h - 1))

    if __name__ == '__main__':
        pygame.init()
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('прямоугольник')

        while pygame.event.wait().type != pygame.QUIT:
            draw()
            pygame.display.flip()
    pygame.quit()
except Exception:
    print('Неправильный формат ввода')
    quit()


