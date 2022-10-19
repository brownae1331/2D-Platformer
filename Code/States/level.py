from ast import Pass
import pygame
from States.pausemenu import PauseMenu
from settings import *
from player import Player
from tiles import Tile
from States.leveleditor import LevelEditor
from States.state import State
from enemy import Enemy
from powerup import PowerUp


class Level(State):
    def __init__(self, game, levelData):
        self.game = game

        terrainLayout = importCSVLayout(levelData['terrain'])
        self.terrainSprites = self.createTileGroup(terrainLayout, 'terrain')

        self.worldShift = 0

    def update(self):
        pass
        # self.tiles.update(self.worldShift)

        # self.player.update()
        # self.hrzCollision()
        # self.vrtCollision()

        # self.enemy.update(self.worldShift)
        # self.moveEnemy()
        # self.playerEnemyCollision()

        # self.powerUp.update(self.worldShift)
        # self.playerBoxCollision()

        # self.scrollX()

        # self.openMenu()

    def render(self, display):
        display.fill('black')
        self.terrainSprites.draw(display)
        # self.player.draw(display)
        # self.enemy.draw(display)
        # self.powerUp.draw(display)

    def createTileGroup(self, layout, type):
        spriteGroup = pygame.sprite.Group()

        for rowIndex, row in enumerate(layout):
            for colIndex, val in enumerate(row):
                if val != '-1':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize

                    if type == 'terrain':
                        terrainTileList = importTilesets(
                            'Assets/Terrain/Terrain.png')
                        tileSurface = terrainTileList[int(val)]
                        sprite = Tile((x, y), tileSize, tileSurface)
                        spriteGroup.add(sprite)

        return spriteGroup

    def moveEnemy(self):
        player = self.player.sprite

        for enemy in self.enemy.sprites():
            if player.rect.x > enemy.rect.x:
                enemy.direction.x = 1
            elif player.rect.x < enemy.rect.x:
                enemy.direction.x = -1

    def openMenu(self):
        if self.game.actions["escape"]:
            newState = PauseMenu(self.game)
            newState.enterState()
        self.game.resetKeys()

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
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

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

    def playerEnemyCollision(self):
        player = self.player.sprite
        collision = pygame.sprite.spritecollide(
            self.player.sprite, self.enemy, False, pygame.sprite.collide_mask)
        for enemy in collision:
            if player.rect.bottom < enemy.rect.top+25:
                enemy.kill()
            else:
                self.setupLevel(levelMap)

    def playerBoxCollision(self):
        player = self.player.sprite
        collision = pygame.sprite.spritecollide(
            player, self.powerUp, False, pygame.sprite.collide_mask)
        for powerUp in collision:
            if player.direction.y < 0:
                player.rect.top = powerUp.rect.bottom
                player.direction.y = 0
                powerUp.kill()
            else:
                if player.direction.x < 0:
                    player.rect.left = powerUp.rect.right
                elif player.direction.x > 0:
                    player.rect.right = powerUp.rect.left

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
