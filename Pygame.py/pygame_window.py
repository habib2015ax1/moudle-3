import pygame 
pygame.init()
screen = pygame.display.set_mode((1080,452))
done=False
image=pygame.image.load("Pygame/coolspacebackroung.png")
image=pygame.transform.scale(image,(1080,452))
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    screen.blit(image,(0,0))   

    pygame.display.flip()