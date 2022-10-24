import pygame
from States.pausemenu import PauseMenu
from settings import *
from player import Player
from tiles import Tile, StaticTile, Crate, Fruit, Checkpoint
from States.leveleditor import LevelEditor
from States.state import State
from enemy import Enemy, Slime


class Level(State):
    def __init__(self, game, levelData):
        self.game = game

        # checkpoints and player
        checkpointLayout = importCSVLayout(levelData['checkpoints'])
        self.checkpointSprites = self.createTileGroup(
            checkpointLayout, 'checkpoints')
        self.start = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.createSingleGroup(checkpointLayout)

        # terrain
        terrainLayout = importCSVLayout(levelData['terrain'])
        self.terrainSprites = self.createTileGroup(terrainLayout, 'terrain')

        # creates
        crateLayout = importCSVLayout(levelData['crates'])
        self.crateSprites = self.createTileGroup(crateLayout, 'crates')

        # fruits
        fruitLayout = importCSVLayout(levelData['fruits'])
        self.fruitSprites = self.createTileGroup(fruitLayout, 'fruits')

        # enemies
        enemyLayout = importCSVLayout(levelData['enemies'])
        self.enemySprites = self.createTileGroup(enemyLayout, 'enemies')

        # constraints
        constraintLayout = importCSVLayout(levelData['constraints'])
        self.constrainSprites = self.createTileGroup(
            constraintLayout, 'constraints')

        self.worldShift = 0

    def update(self):
        self.terrainSprites.update(self.worldShift)
        self.crateSprites.update(self.worldShift)
        self.fruitSprites.update(self.worldShift)
        self.enemySprites.update(self.worldShift)
        self.constrainSprites.update(self.worldShift)
        self.checkpointSprites.update(self.worldShift)
        self.start.update(self.worldShift)
        self.goal.update(self.worldShift)

        self.enemyCollision()

        self.player.update()

        self.hrzCollision()
        self.vrtCollision()
        self.scrollX()

        # self.moveEnemy()
        # self.playerEnemyCollision()

        # self.playerBoxCollision()

        # self.openMenu()

    def render(self, display):
        display.fill('grey')
        self.terrainSprites.draw(display)
        self.crateSprites.draw(display)
        self.fruitSprites.draw(display)
        self.enemySprites.draw(display)
        self.checkpointSprites.draw(display)
        self.start.draw(display)
        self.player.draw(display)
        self.goal.draw(display)

    def createTileGroup(self, layout, type):
        spriteGroup = pygame.sprite.Group()

        for rowIndex, row in enumerate(layout):
            for colIndex, val in enumerate(row):
                if val != '-1':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize

                    if type == 'terrain':
                        terrainTileList = import_cut_graphics(
                            'Assets/Terrain/Terrain.png')
                        tileImage = terrainTileList[int(val)]
                        sprite = StaticTile((x, y), tileSize, tileImage)

                    if type == 'crates':
                        sprite = Crate((x, y), tileSize)

                    if type == 'fruits':
                        if val == '0':
                            sprite = Fruit(
                                (x, y), tileSize, 'Assets/Items/Fruits/Bananas.png', 17, 32, 32)
                        if val == '1':
                            sprite = Fruit(
                                (x, y), tileSize, 'Assets/Items/Fruits/Apple.png', 17, 32, 32)
                        if val == '2':
                            sprite = Fruit(
                                (x, y), tileSize, 'Assets/Items/Fruits/Pineapple.png', 17, 32, 32)

                    if type == 'enemies':
                        if val == '0':
                            sprite = Enemy(
                                (x, y), tileSize, 'Assets/Enemies/Chicken/', 'Idle (32x34).png', 13, 32, 34)
                        if val == '1':
                            sprite = Slime((x, y), tileSize)

                    if type == 'constraints':
                        sprite = Tile((x, y), tileSize)

                    if type == 'checkpoints':
                        if val == '1':
                            checkpointImage = pygame.image.load(
                                'Assets/Items/Checkpoints/Checkpoint/Checkpoint (No Flag).png')
                            sprite = Checkpoint(
                                (x, y), tileSize, checkpointImage)

                    spriteGroup.add(sprite)

        return spriteGroup

    def createSingleGroup(self, layout):
        for rowIndex, row in enumerate(layout):
            for colIndex, val in enumerate(row):
                if val != '-1':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize
                    if val == '0':
                        # player
                        playerSprite = Player((x, y))
                        self.player.add(playerSprite)

                        # start goal
                        startImage = pygame.image.load(
                            'Assets/Items/Checkpoints/Start/Start (Idle).png')
                        sprite = Checkpoint(
                            (x, y), tileSize, startImage)
                        self.start.add(sprite)
                    if val == '2':
                        goalImage = pygame.image.load(
                            'Assets/Items/Checkpoints/End/End (Idle).png')
                        sprite = Checkpoint(
                            (x, y), tileSize, goalImage)
                        self.goal.add(sprite)

    def openMenu(self):
        if self.game.actions["escape"]:
            newState = PauseMenu(self.game)
            newState.enterState()
        self.game.resetKeys()

    # This function stops the player waling though walls

    def hrzCollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrainSprites.sprites() + self.crateSprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    # This function stops the player from falling thougn the floor
    def vrtCollision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.terrainSprites.sprites() + self.crateSprites.sprites():
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

    def enemyCollision(self):
        for enemy in self.enemySprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constrainSprites, False):
                enemy.reverse()

    # def playerEnemyCollision(self):
    #     player = self.player.sprite
    #     collision = pygame.sprite.spritecollide(
    #         self.player.sprite, self.enemy, False, pygame.sprite.collide_mask)
    #     for enemy in collision:
    #         if player.rect.bottom < enemy.rect.top+25:
    #             enemy.kill()
    #         else:
    #             self.setupLevel(levelMap)

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
