import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

w=800;
h=600;
display = pygame.display.set_mode((w, h))

pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)
textRect = text.get_rect()

textRect.center = (w // 2, h // 2)
while True:
    display.fill(white)
    display.blit(text, textRect) ##Copio el texto el en display

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
