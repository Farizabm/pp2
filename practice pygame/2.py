import pygame

pygame.init()

#RGB(255,255,255)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)

size =(400,500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame example")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
    screen.fill(white)
    pygame.draw.line(screen, green, [0,0], [100,100],5)

    for y in range(0,100,10):
        pygame.draw.line(screen, red, [0,10+y], [100,110+y], 2)
    pygame.display.flip()

pygame.quit()