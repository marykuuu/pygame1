import pygame

try:
    w, h = [int(i) for i in input().split()]

    def draw():
        screen.fill('black')
        pygame.draw.line(screen, 'white', (0, 0), (w, h), width=5)
        pygame.draw.line(screen, 'white', (w, 0), (0, h), width=5)

    if __name__ == '__main__':
        pygame.init()
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('крест')

        while pygame.event.wait().type != pygame.QUIT:
            draw()
            pygame.display.flip()
    pygame.quit()
except Exception:
    print('Неправильный формат ввода')
    quit()


