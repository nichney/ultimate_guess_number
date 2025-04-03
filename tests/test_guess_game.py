import unittest, os, json
from unittest.mock import patch
import ultimate_guess_number

class TestGuessNumber(unittest.TestCase):

    def setUp(self):
        self.instance = ultimate_guess_number.Guesser()
        self.instance.record_filename = "test_record.json"  # test records to not corrupt the existing data
        self.instance.record = self.instance.load_record()

    def test_load_default_record(self):
        """Test loading a default record when file does not exist"""
        record = self.instance.load_record()
        self.assertIn("EASY", record)
        self.assertIn("MEDIUM", record)
        self.assertIn("HARD", record)

    def test_update_record(self):
        """Test updating game records for best/worst attempts & times"""
        self.instance.update_record(2, 30)
        self.assertEqual(self.instance.record["MEDIUM"]["best_attempts"], 2)
        self.assertEqual(self.instance.record["MEDIUM"]["worst_attempts"], 2)
        self.assertEqual(self.instance.record["MEDIUM"]["best_time"], 30)
        self.assertEqual(self.instance.record["MEDIUM"]["worst_time"], 30)

    def test_do_difficulty(self):
        with patch('builtins.print') as mock_print:
            self.instance.do_difficulty("Wrong value")
            mock_print.assert_called_with("Error: There is no such difficulty.")

        self.assertIsNone(self.instance.do_difficulty("easy"))
        self.assertEqual(self.instance.difficulty, ultimate_guess_number.Difficulty.EASY)

        self.assertIsNone(self.instance.do_difficulty("medium"))
        self.assertEqual(self.instance.difficulty, ultimate_guess_number.Difficulty.MEDIUM)

        self.assertIsNone(self.instance.do_difficulty("hard"))
        self.assertEqual(self.instance.difficulty, ultimate_guess_number.Difficulty.HARD)
    
    def test_correct_guess(self):
        """Test if game end after a correct guess """
        self.instance.secret = 1
        self.assertFalse(self.instance.default('1'))

    def test_incorrect_guess(self):
        self.instance.secret = 1
        # todo: chech

    def test_winning_condition(self):
        """Test if game correctly recognizes a win"""
        self.instance.secret = 25
        with patch("builtins.print") as mock_print:
            self.assertFalse(self.instance.default("25")) 
            mock_print.assert_any_call("Congragulations! You guessed the correct number in 1 attempts")

    def test_losing_condition(self):
        """Test losing the game when out of guesses"""
        self.instance.secret = 10
        self.instance.guesses_remain= 1
        with patch("builtins.print") as mock_print:
            self.assertFalse(self.instance.default('9')) 
            mock_print.assert_any_call(f"You lost! The number was {self.instance.secret}")

    def test_restart_game(self):
        """Test restarting the game when user enters 'y'"""
        self.instance.default("y")
        self.assertEqual(self.instance.prompt, "Enter your guess (or command): ")


    def test_eof_command(self):
        """Test EOF command (Ctrl+D)"""
        with patch("builtins.print"):
            self.assertTrue(self.instance.do_EOF(""))

if __name__ == '__main__':
    unittest.main()
