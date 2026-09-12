import pygame 
pygame.init()
screen = pygame.display.set_mode((700,700))
done=False
image=pygame.image.load("Pygame/phone.jpg")
image=pygame.transform.scale(image,(200,150))
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
    screen.blit(image,(100,100))   

    pygame.display.flip()