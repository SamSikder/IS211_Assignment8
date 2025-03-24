import time
from game import Game

class TimedGameProxy:
    def __init__(self, player1, player2):
        self.game = Game(player1, player2)
        self.start_time = time.time()

    def play(self):
        while True:
            if time.time() - self.start_time > 60:
                print("Time's up! Determining the winner...")
                self.determine_winner()
                break
            if self.game.play_turn():
                break

    def determine_winner(self):
        if self.game.player1.score > self.game.player2.score:
            print(f"{self.game.player1.name} wins!")
        elif self.game.player1.score < self.game.player2.score:
            print(f"{self.game.player2.name} wins!")
        else:
            print("It's a tie!")

import argparse
from player_factory import PlayerFactory
from timed_game_proxy import TimedGameProxy
from game import Game

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", choices=["human", "computer"], required=True)
    parser.add_argument("--player2", choices=["human", "computer"], required=True)
    parser.add_argument("--timed", action="store_true")
    args = parser.parse_args()

    player1 = PlayerFactory.create_player(args.player1, "Player 1")
    player2 = PlayerFactory.create_player(args.player2, "Player 2")

    if args.timed:
        game = TimedGameProxy(player1, player2)
    else:
        game = Game(player1, player2)

    game.play()

if __name__ == "__main__":
    main()
