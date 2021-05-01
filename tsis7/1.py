import pygame
from math import pi, cos,sin

pygame.init()


WIDTH =800
HEIGHT =600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

#def get_points(f, xrange, step ,kx, ky, center):
    #определить сколько точек
#    num = math.ceil(xrange[1] - xrange[0] / step)
    #как найти точки
#    x_values = (x *step + xrange[0] for x in range(num +1))
    #массив который будет хранит тупл,кх и ку чтобы растягивать на нужные коэф
#    func = ((kx * x ,ky * f(x)) for x in x_values)
    #создаем точки, пробегаемся по массиву и прибавляем к центру
#    points = tuple(map(lambda x: (x[0] + center[0], -x[1]+ center[1]),func))
#    return points

#xrange = (-3 * math.pi, 3* math.pi)
#step = 0.1
#kx = WIDTH / (3 * math.pi)
#ky = 200 
#center = (WIDTH //2 , HEIGHT // 2)

#sin_points = get_points(math.sin, xrange, step, kx, ky, center)
#cos_points = get_points(math.cos, xrange, step, kx, ky, center)

isDone = False

while not isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
    screen.fill((255,255,255))

    for x in range(50,750):
        sin_y1 = 240 * sin((x-100)/ 100 *pi)
        sin_y2 = 240 * sin((x-99) / 100 *pi)
        pygame.draw.aalines(screen, (255,0,0), True, [(x,280 + sin_y1), ((x+1), 280 + sin_y2)])
    
    for x in range(50,750, 5):
        cos_y1 = 240 * cos((x-100)/ 100 *pi)
        cos_y2 = 240 * cos((x-99) / 100 *pi)
        pygame.draw.aalines(screen, (0,0,255), True, [(x,280 + cos_y1), ((x+1), 280 + cos_y2)])

    pygame.display.update()
pygame.quit()