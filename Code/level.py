import pygame
from player import Player
from tiles import Tile
from settings import tileSize, screenWidth


class Level:
    # The level needs the level data to know what it has to draw and it need the surface that it has to draw on
    def __init__(self, levelData, screen):
        # Set the attribute for the suface the level will be displayed on
        self.screen = screen
        self.worldShift = 0

        self.setupLevel(levelData)  # Set the attribute for the level data

    # This function is going to draw the level onto the screen
    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

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

    # This function stops the player waling though walls
    def hrzCollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            # If a sprite in the tiles group collides with the player than the following code happens
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # If the player is moving to the left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:  # if the player is moving to the right
                    player.rect.right = sprite.rect.left

    # This function stops the player from falling thougn the floor
    def vrtCollision(self):
        player = self.player.sprite
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

    # When the game starts this function is called
    def run(self):

        # Level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.screen)
        self.scrollX()

        # Player
        self.player.update()
        self.hrzCollision()
        self.vrtCollision()
        self.player.draw(self.screen)
