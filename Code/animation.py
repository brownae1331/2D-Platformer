import pygame


class Animation:
    def __init__(self):
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0

    def spriteSheet(self, sheet, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    def getAnimationAssests(self, path, status, animationSteps, width, heigth):
        self.animationList = []
        if status == 'None':
            spriteSheetImage = pygame.image.load(path).convert_alpha()
        else:
            spriteSheetImage = pygame.image.load(path + status).convert_alpha()
        for i in range(animationSteps):
            self.animationList.append(self.spriteSheet(
                spriteSheetImage, i, width, heigth, 1, 'black'))

    def animation(self, animationSteps):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate >= self.animationCooldown:
            self.frameIndex += 1
            self.lastUpdate = currentTime
            if self.frameIndex >= animationSteps - 1:
                self.frameIndex = 0

        return self.animationList[self.frameIndex]
