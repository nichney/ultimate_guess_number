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

    def test_guess(self):
        instance = guess_game.Guesser()
        instance.do_difficulty("hard")

        self.assertTrue(instance.default(instance.secret))
        self.assertIsNone(instance.default(101))
        self.assertIsNone(instance.default(-1))
        self.assertFalse(instance.default(100))
