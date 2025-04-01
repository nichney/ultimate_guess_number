import unittest
import guess_game

class TestGuessNumber(unittest.TestCase):
    
    def assertNotFalse(self, x: bool):
        if x == False:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_do_difficulty(self):
        instance = guess_game.Guesser()
        self.assertFalse(instance.do_difficulty("some wrong value"))

        self.assertIsNone(instance.do_difficulty("easy"))
        self.assertEqual(instance.difficulty, guess_game.Difficulty.EASY)

        self.assertIsNone(instance.do_difficulty("medium"))
        self.assertEqual(instance.difficulty, guess_game.Difficulty.MEDIUM)

        self.assertIsNone(instance.do_difficulty("hard"))
        self.assertEqual(instance.difficulty, guess_game.Difficulty.HARD)

