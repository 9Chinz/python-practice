# วาดรูปทรง
import pygame

pygame.init()

# สร้าง display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# กรณีที่ต้องการ caption
pygame.display.set_caption("Image")

# กำหนดค่าคงที่ของสี เป็น Tuple ของ RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# กำหนด background color
display_surface.fill(BLUE)
dragon_left_image = pygame.image.load("week8/lecture/pygame_tutorial/asset/dragon_left.png")
dragon_left_ract = dragon_left_image.get_rect()
dragon_left_ract.topleft = (0,0)
print(dragon_left_ract)


running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.blit(dragon_left_image, dragon_left_ract)

    pygame.draw.line(display_surface, WHITE, (0, 75), (WINDOW_WIDTH, 75), 4)
    pygame.display.update()

pygame.quit()