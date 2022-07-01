import pygame
import spritesheet
from settings import *

pygame.init()

screen = pygame.display.set_mode([screenWidth, screenHeight])


spriteSheetImage = pygame.image.load(
    'Assests/Enemies/Bat/Idle (46x30).png').convert_alpha()
spriteSheet = spritesheet.SpriteSheet(spriteSheetImage)

# Create animation list
animationList = []
animationSteps = 12
lastUpdate = pygame.time.get_ticks()
animationCooldown = 75
frame = 0

for i in range(animationSteps):
    animationList.append(spriteSheet.getImage(i, 46, 30, 3, 'black'))


done = False
clock = pygame.time.Clock()

while not done:

    screen.fill('grey')

    # update animation
    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate >= animationCooldown:
        frame += 1
        lastUpdate = currentTime
        if frame >= len(animationList):
            frame = 0

    screen.blit(animationList[frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()

pygame.quit()
