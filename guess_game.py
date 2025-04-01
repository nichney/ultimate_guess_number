#!/usr/bin/python
# An ultimate CLI guessing number game
import cmd, time, random, json, enum

class Difficulty(enum.Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3

class Guesser(cmd.Cmd):
    intro = f'Welcome to the Ultimate Number Guessing Game!\nI\'m thinking of a number between 1 and 100' \
            '\nTo change game difficulty - use "difficulty [easy|medium|hard]"'
    prompt = "Enter your guess: "

    def __init__(self):
        self.difficulty = Difficulty.MEDIUM
        self.reset() # set default values
        super().__init__()

    def do_difficulty(self, line):
        if line == 'easy': self.difficulty = Difficulty.EASY 
        elif line == 'medium': self.difficulty = Difficulty.MEDIUM 
        elif line == 'hard': self.difficulty = Difficulty.HARD 
        else: return False # exit program if wrong option
        self.reset()

    def default(self, guess):
        """Method called when user just enter a number"""
        try:
            guess = int(guess)
            self.guesses_remain -= 1
            if self.guesses_remain == 0:
                self.lost()
                self.prompt = "Do you wanna play other round? [y/N] "
            if guess == self.secret:
                self.won()
                self.prompt = "Do you wanna play other round? [y/N] "
            print("Incorrect!", end=' ')
            if self.secret < guess:
                print(f"The number is less than {guess}. Remain {self.guesses_remain} guesses") 
            else:
                print(f"The number is greater than {guess}. Remain {self.guesses_remain} guesses")
        except ValueError:
            if guess == 'y':
                self.reset()
                self.prompt = "Enter your guess: "
            else:
                return True
            
    def won(self):
        print(f"Congragulations! You guessed the correct number in {self.difficulty.value - self.guesses_remain} attempts")
        print(f"You spent {round(time.monotonic() - self.start_time)} sec. to solve it.")

    def lost(self):
        print(f"You lost! The number was {self.secret}")
        print(f"You spent {round(time.monotonic() - self.start_time)} sec. to solve it.")

    def reset(self):
        """ Reset the guessing number, remain guesses and start time """
        self.guesses_remain = self.difficulty.value
        self.secret = random.randint(1, 100)
        self.start_time = time.monotonic()


    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Guesser().cmdloop()

