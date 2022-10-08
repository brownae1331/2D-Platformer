import pygame
from menu import Menu
from settings import *
from player import Player
from tiles import Tile
from mainmenu import MainMenu
from leveleditor import LevelEditor
from enemy import Enemy


class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.Surface([screenWidth, screenHeight])
        self.window = pygame.display.set_mode([screenWidth, screenHeight])
        self.clock = pygame.time.Clock()

        self.running = True
        self.playing = False
        self.setupLevel(levelMap)

        self.worldShift = 0

        self.menu = Menu(self)
        self.mainMenu = MainMenu(self)
        self.levelEditor = LevelEditor(self)

    def gameLoop(self):
        while self.playing:
            self.checkEvent()

            self.display.fill('black')

            self.tiles.update(self.worldShift)
            self.tiles.draw(self.display)
            self.scrollX()

            self.player.update()
            self.hrzCollision()
            self.vrtCollision()
            self.player.draw(self.display)

            self.enemy.update(self.worldShift)
            self.enemy.draw(self.display)
            self.moveEnemy()
            self.playerEnemyCollision()

            self.clock.tick(60)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.mainMenu.runDisplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            self.playing = False
            self.levelEditor.runEditor = True

        elif keys[pygame.K_ESCAPE]:
            self.playing = False
            self.menu.runMenu = True

    # This function is going to draw the level onto the screen

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()

        # enumerate give the value of whats in each row and give the index of each row
        for rowIndex, row in enumerate(layout):
            # This  give the value of whats in each column and its index
            for colIndex, col in enumerate(row):
                # Find the coordinate where the tile needs to be placed
                x = colIndex * tileSize
                y = rowIndex * tileSize

                # If there is an X in the level data then a tile is place on the screen
                if col == 'X':
                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)
                # If there is a P in the level data the plater will be placed there
                if col == 'P':
                    player = Player((x, y))
                    self.player.add(player)
                if col == 'E':
                    enemy = Enemy((x, y))
                    self.enemy.add(enemy)

    # This function stops the player waling though walls
    def hrzCollision(self):
        player = self.player.sprite

        for enemy in self.enemy.sprites():
            enemy.rect.x += enemy.direction.x * enemy.speed

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left

        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.direction.x = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.lefts

    # This function stops the player from falling thougn the floor
    def vrtCollision(self):
        player = self.player.sprite

        for enemy in self.enemy.sprites():
            enemy.applyGravity()

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.onGround = True
                    elif enemy.direction.y < 0:

                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0

                if enemy.onGround and enemy.direction.y < 0:
                    enemy.onGround = False

        player.applyGravity()
        for sprite in self.tiles.sprites():
            # If the player collides with a tile
            if sprite.rect.colliderect(player.rect):
                # If the player is falling / is standing on a tile
                if player.direction.y > 0:
                    # The postion of the bottom of the player become the position of the top of the tile
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.onGround = True
                # If the player is jumping / the player hits a tile on their head
                elif player.direction.y < 0:
                    # The postion of the top of the player becomes the position of the bottom of the tile
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

            if player.onGround and player.direction.y < 0:
                player.onGround = False

    # This function scroll of the screen when the player get to the edge
    def scrollX(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x

        # If the player is close to the left side of the screen and moving to the left
        if playerX < screenWidth / 4 and directionX < 0:
            # Make the player stop moving and move the world to the right
            self.worldShift = 8
            player.speed = 0

        # If the player is close to the right side of the screen and moving to the right
        elif playerX > screenWidth - (screenWidth / 4) and directionX > 0:
            self.worldShift = -8
            player.speed = 0

        else:
            self.worldShift = 0
            player.speed = 8

    def moveEnemy(self):
        player = self.player.sprite

        for enemy in self.enemy.sprites():
            if player.rect.x > enemy.rect.x:
                enemy.direction.x = 1
            elif player.rect.x < enemy.rect.x:
                enemy.direction.x = -1

    def playerEnemyCollision(self):
        player = self.player.sprite
        collision = pygame.sprite.spritecollide(
            self.player.sprite, self.enemy, False, pygame.sprite.collide_mask)
        for enemy in collision:
            if player.rect.bottom < enemy.rect.top+25:
                enemy.kill()
            else:
                self.setupLevel(levelMap)
