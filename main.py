import pygame

print('Setup Start')
pygame.init()
widow = pygame.display.set_mode(size=(600, 680))
print('Setup Start')

print('Setup Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()