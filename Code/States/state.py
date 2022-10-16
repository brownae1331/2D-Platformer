class State():
    def __init__(self, game):
        self.game = game
        self.lastState = None

    def enterState(self):
        if len(self.game.stateStack) > 1:
            self.lastState = self.game.stateStack[-1]
        self.game.stateStack.append(self)

    def exitState(self):
        self.game.stateStack.pop()
