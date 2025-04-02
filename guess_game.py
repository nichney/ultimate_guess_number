#!/usr/bin/python
# An ultimate CLI guessing number game
import cmd, time, random, json, enum

class Difficulty(enum.Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3

class Guesser(cmd.Cmd):
    intro = f'Welcome to the Ultimate Number Guessing Game!\nI\'m thinking of a number between 1 and 100' \
            '\nTo change game difficulty - use "difficulty [easy|medium|hard]"' \
            '\n "record" to print out your records'
    prompt = "Enter your guess: "

    def __init__(self):
        self.difficulty = Difficulty.MEDIUM
        self.record_filename = 'guesses_record.json'
        self.reset() # set default values
        self.record = self.load_record()
        super().__init__()

    def load_record(self) -> dict:
        """Record structure:
            {   'EASY': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0},
                'MEDIUM': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0},
                'HARD': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0}
            }
        """
        try:
            with open(self.record_filename, 'r') as f:
                return json.load(f)
        except Exception:
            return {   'EASY': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0},
                        'MEDIUM': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0},
                    'HARD': {'best_attempts': 100, 'worst_attempts': 0, 'best_time': 50000, 'worst_time': 0}
                    } # return default dict if no file or other error

    def update_record(self, attempts, game_time):
        self.record[self.difficulty.name]['best_attempts'] = min(self.record[self.difficulty.name]['best_attempts'], attempts)
        self.record[self.difficulty.name]['worst_attempts'] = max(self.record[self.difficulty.name]['worst_attempts'], attempts)
        self.record[self.difficulty.name]['best_time'] = min(self.record[self.difficulty.name]['best_time'], game_time)
        self.record[self.difficulty.name]['worst_time'] = max(self.record[self.difficulty.name]['worst_time'], game_time)

    def write_record(self):
        try:
            with open(self.record_filename, 'w') as f:
                json.dump(self.record, f)
        except Exception as e:
            print(f'Error! Cannot write the record to a file: {e}')

    def do_record(self, line):
        """Print out the currect record"""
        print('Your records are:')
        for d in self.record.keys():
            print(f"-- Records on {d} level:")
            for k, v in self.record[d].items():
                if k.endswith("_attempts") and v in (100, 0) or k.endswith("_time") and v in (50000, 0):
                    continue # skip if default values
                print(f"---- {k} is {v}")
        print('-'*25)
        print("Starting new game... done!")
        self.reset()

    def do_difficulty(self, line):
        if line == 'easy': self.difficulty = Difficulty.EASY 
        elif line == 'medium': self.difficulty = Difficulty.MEDIUM 
        elif line == 'hard': self.difficulty = Difficulty.HARD 
        else:
            print(f'Error: There is no such difficulty.')
            #return True # exit program if wrong option
        self.reset()

    def default(self, guess):
        """Method called when user just enter a number"""
        if guess.lower() == 'y':  # Restart game if user wants to play again
            self.reset()
            self.prompt = "Enter your guess: "
            return

        try:
            guess = int(guess)
        except ValueError:
            self.write_record()
            return True  # Exit if input is invalid and not 'y'

        if guess == self.secret:
            self.won()
            self.prompt = "Do you wanna play another round? [y/N] "
            return False  # End game

        self.guesses_remain -= 1
        if self.guesses_remain == 0:
            self.lost()
            self.prompt = "Do you wanna play another round? [y/N] "
            return False  # End game

        # Provide hint to user
        hint = "less" if self.secret < guess else "greater"
        print(f"Incorrect! The number is {hint} than {guess}. {self.guesses_remain} guesses remaining.")

            
    def won(self):
        spent = round(time.monotonic() - self.start_time)
        attempts = self.difficulty.value - self.guesses_remain + 1
        print(f"Congragulations! You guessed the correct number in {attempts} attempts")
        self.update_record(attempts, spent)
        print(f"You spent {spent} sec. to solve it.")

    def lost(self):
        spent = round(time.monotonic() - self.start_time)
        print(f"You lost! The number was {self.secret}")
        print(f"You spent {spent} sec. to solve it.")

    def reset(self):
        """ Reset the guessing number, remain guesses and start time """
        self.guesses_remain = self.difficulty.value
        self.secret = random.randint(1, 100)
        self.start_time = time.monotonic()


    def do_EOF(self, line):
        print() # just leave an empty line before finishing programm
        self.write_record()
        return True


if __name__ == '__main__':
    Guesser().cmdloop()

