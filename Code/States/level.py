import pygame
from States.state import State
from States.pausemenu import PauseMenu
from States.deathscreen import DeathScreen
from States.winscreen import WinScreen
from settings import *
from player import Player
from enemy import Enemy, Slime
from tiles import Tile, StaticTile, Crate, Fruit, Checkpoint, Bullet


class Level(State):
    def __init__(self, game, levelData):
        self.game = game
        self.time = 0

        self.levelData = levelData
        self.worldShift = 0

        self.setupWorld(self.levelData)

    def setupWorld(self, levelData):
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

        # crates
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

        self.bulletSprites = pygame.sprite.Group()

        self.score = 0
        self.startTime = pygame.time.get_ticks()

    def update(self, actions):
        self.time = pygame.time.get_ticks()

        self.terrainSprites.update(self.worldShift)
        self.crateSprites.update(self.worldShift)
        self.fruitSprites.update(self.worldShift)
        self.enemySprites.update(self.worldShift)
        self.constrainSprites.update(self.worldShift)
        self.checkpointSprites.update(self.worldShift)
        self.start.update(self.worldShift)
        self.goal.update(self.worldShift)
        self.bulletSprites.update(self.worldShift)

        self.enemyCollision()
        self.fruitCollision()
        self.playerEnemyCollision()

        self.player.update()
        self.createBullet(actions)
        self.bulletCollision()
        self.goalCollision()

        self.hrzCollision()
        self.vrtCollision()
        self.vrtCrateCollision()
        self.scrollX()
        self.fallOffWorld()

        self.openMenu()

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
        self.bulletSprites.draw(display)

        self.displayScore(self.score, display)
        self.displayTimer(display)
        self.powerUpTimer(display)
        self.powerUpIcon(display)

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
                        playerSprite = Player((x, y), self.game)
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

        for sprite in self.terrainSprites.sprites() + self.crateSprites.sprites() + self.goal.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    # This function stops the player from falling thougn the floor
    def vrtCollision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.terrainSprites.sprites() + self.goal.sprites():
            # If the player collides with a tile
            if sprite.rect.colliderect(player.rect):
                # If the player is falling / is standing on a tile
                if player.direction.y > 0:
                    # The postion of the bottom of the player become the position of the top of the tile
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.onGround = True
                    player.jumps = 0
                # If the player is jumping / the player hits a tile on their head
                elif player.direction.y < 0:
                    # The postion of the top of the player becomes the position of the bottom of the tile
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

            if player.onGround and player.direction.y < 0:
                player.onGround = False

    def vrtCrateCollision(self):
        player = self.player.sprite

        for sprite in self.crateSprites.sprites():
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
                    sprite.kill()
                    player.powerUp()

    def enemyCollision(self):
        for enemy in self.enemySprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constrainSprites, False):
                enemy.reverse()

    def fruitCollision(self):
        player = self.player.sprite
        collision = pygame.sprite.spritecollide(
            player, self.fruitSprites, True)
        if collision:
            self.score += 1

    def playerEnemyCollision(self):
        player = self.player.sprite
        enemyCollisions = pygame.sprite.spritecollide(
            player, self.enemySprites, False)

        if enemyCollisions:
            for enemy in enemyCollisions:
                if enemy.rect.top < player.rect.bottom < enemy.rect.centery and player.direction.y >= 0:
                    enemy.kill()
                    self.score += 5
                else:
                    if player.isInvincible == False:
                        self.killPlayer()

    def goalCollision(self):
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.goal, False):
            self.exitState()
            newState = WinScreen(self.game)
            newState.enterState()

    def bulletCollision(self):
        for bullet in self.bulletSprites.sprites():
            if pygame.sprite.spritecollide(bullet, self.enemySprites, True):
                bullet.kill()
                self.score += 5

    def killPlayer(self):
        self.exitState()
        newState = DeathScreen(self.game)
        newState.enterState()

    def displayScore(self, score, display):
        font = pygame.font.Font('Assets/Fonts/PixelColeco-4vJW.ttf', 30)
        scoreImage = font.render(str(score), False, '#33323d')
        scoreRect = scoreImage.get_rect(topleft=(50, 61))
        display.blit(scoreImage, scoreRect)

    def displayTimer(self, display):
        self.gameTime = self.time - self.startTime
        seconds = int((self.gameTime // 1000) % 60)
        minutes = int(seconds // 60)

        font = pygame.font.Font('Assets/Fonts/PixelColeco-4vJW.ttf', 30)
        timerImage = font.render((str(minutes) + ':' + str(
            seconds)), False, '#33323d')
        timerRect = timerImage.get_rect(topright=(screenWidth - 50, 61))
        display.blit(timerImage, timerRect)

    def powerUpTimer(self, display):
        player = self.player.sprite
        if player.isInvincible or player.runDoubleJump or player.runBullets:
            seconds = (player.time - player.startTime) // 1000
            font = pygame.font.Font('Assets/Fonts/PixelColeco-4vJW.ttf', 30)
            timerImage = font.render(str(10 - seconds), False, '#b08f26')
            timerRect = timerImage.get_rect(topright=(screenWidth - 50, 100))
            display.blit(timerImage, timerRect)

    def powerUpIcon(self, display):
        player = self.player.sprite
        if player.isInvincible:
            invincibleImage = pygame.image.load(
                'Assets/PowerUps/Invincible.png').convert_alpha()
            invincibleRect = invincibleImage.get_rect(
                topright=(screenWidth - 90, 100))
            display.blit(invincibleImage, invincibleRect)
        elif player.runDoubleJump:
            jumpImage = pygame.image.load(
                'Assets/PowerUps/DoubleJump.png').convert_alpha()
            jumpRect = jumpImage.get_rect(
                topright=(screenWidth - 90, 100))
            display.blit(jumpImage, jumpRect)
        elif player.runBullets:
            bulletImage = pygame.image.load(
                'Assets/PowerUps/Bullet.png').convert_alpha()
            bulletRect = bulletImage.get_rect(
                topright=(screenWidth - 90, 100))
            display.blit(bulletImage, bulletRect)

    def createBullet(self, actions):
        player = self.player.sprite
        if actions['z'] and player.runBullets:
            if player.direction.x >= 0:
                self.bulletSprites.add(
                    Bullet((player.rect.centerx, player.rect.centery), 1))
            else:
                self.bulletSprites.add(
                    Bullet((player.rect.centerx, player.rect.centery), -1))

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

    def fallOffWorld(self):
        player = self.player.sprite
        if player.rect.top > screenHeight:
            self.killPlayer()
