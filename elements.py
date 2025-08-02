import pygame


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255) 


screen.fill(WHITE)

rect_width, rect_height = 100, 60
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, (0, 0, 0))  # Black text
text_rect = text.get_rect(center=(320, 50))
screen.blit(text, text_rect)


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
