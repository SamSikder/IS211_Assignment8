import unittest
from player import Player, ComputerPlayer

class TestPlayer(unittest.TestCase):
    def test_player_initial_score(self):
        player = Player("Player1")
        self.assertEqual(player.score, 0)

    def test_computer_strategy(self):
        computer = ComputerPlayer("AI")
        computer.score = 80
        self.assertFalse(computer.roll_or_hold())

if __name__ == "__main__":
    unittest.main()
