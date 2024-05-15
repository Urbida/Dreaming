from FCL import *


def pause_menu():
    running = True
    while running:
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = button(event.pos)
        pygame.draw.rect(screen, (200, 200, 200), (760, 200, 400, 600))
        pygame.draw.rect(screen, (100, 100, 100), (780, 240, 360, 140))
        pygame.draw.rect(screen, (100, 100, 100), (780, 420, 360, 140))
        pygame.display.flip()
