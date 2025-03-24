import argparse
import random
from player_factory import PlayerFactory

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_turn(self):
        for player in [self.player1, self.player2]:
            print(f"{player.name}'s turn. Current score: {player.score}")
            if player.roll_or_hold():
                roll = random.randint(1, 6)
                print(f"{player.name} rolled a {roll}")
                if roll == 1:
                    print(f"{player.name} loses their turn!")
                else:
                    player.score += roll
                    if player.score >= 100:
                        print(f"{player.name} wins with {player.score} points!")
                        return True
            else:
                print(f"{player.name} chose to hold.")
        return False
