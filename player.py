import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_or_hold(self):
        choice = input(f"{self.name}, would you like to roll or hold? (r/h): ").strip().lower()
        return choice == 'r'

class ComputerPlayer(Player):
    def roll_or_hold(self):
        hold_threshold = min(25, 100 - self.score)
        print(f"{self.name}'s threshold to hold: {hold_threshold}")
        return self.score < hold_threshold
