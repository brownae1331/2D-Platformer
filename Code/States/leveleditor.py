import pygame
from pygame.math import Vector2 as vector
from settings import *
from States.state import State


class LevelEditor(State):
    def __init__(self, game):
        self.game = game

        # navigation
        self.origin = vector()
        self.panActive = False
        self.panOffset = vector()

    def update(self, actions):
        self.moveScreen(actions)

    def render(self, display):
        display.fill('white')
        pygame.draw.circle(display, 'red', self.origin, 10)

    def moveScreen(self, actions):
        # Check middle mouse
        if actions['middlemouseclick']:
            self.panOffset = vector(pygame.mouse.get_pos()) - self.origin

        self.panActive = actions['middlemouse']

        # Move screen
        if self.panActive:
            self.origin = vector(pygame.mouse.get_pos()) - self.panOffset
