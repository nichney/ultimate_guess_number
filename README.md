# Ultimate CLI Number Guessing Game

## Description

https://roadmap.sh/projects/number-guessing-game

The **Ultimate CLI Number Guessing Game** is a command-line interface (CLI) game where the player attempts to guess a randomly generated number between 1 and 100. The game offers three difficulty levels, each with a different number of attempts allowed. Player records, including best and worst attempts and times, are saved for future reference.

## Features
- Three difficulty levels: **Easy (10 attempts), Medium (7 attempts), and Hard (4 attempts)**.
- Keeps track of player records, including best/worst attempts and times for each difficulty level.
- Provides hints after each incorrect guess.
- Allows players to restart the game after winning or losing.
- Saves game statistics in a JSON file.

## How to Play
1. Start the game by running the script.
2. The program will generate a random number between 1 and 100.
3. Enter a guess. The game will tell you if the number is **greater** or **less** than your guess.
4. You have a limited number of attempts based on the difficulty level.
5. If you guess correctly, you win! Otherwise, the game continues until you run out of attempts.
6. You can change the difficulty using the `difficulty` command.
7. View your past performance using the `record` command.
8. Press `CTRL+D` to exit the game.

## Available Commands
| Command       | Description |
|--------------|-------------|
| `difficulty` | Change the game difficulty. Options: `easy`, `medium`, `hard` |
| `record`     | Display the player's best and worst records |
| `help`       | Show available commands |
| `CTRL+D`     | Exit the game and save records |

## Game Records
The game maintains a record of your best and worst performances in `guesses_record.json`. The record includes:
- **Best Attempts**: The lowest number of attempts taken to win the game.
- **Worst Attempts**: The highest number of attempts taken to win the game.
- **Best Time**: The shortest time taken to win.
- **Worst Time**: The longest time taken to win.

## Example Gameplay
```
Welcome to the Ultimate Number Guessing Game!
I'm thinking of a number between 1 and 100
Type "help" to discover available commands
Press CTRL+D to exit

Enter your guess (or command): 50
Incorrect! The number is greater than 50. 6 guesses remaining.
Enter your guess (or command): 75
Incorrect! The number is less than 75. 5 guesses remaining.
Enter your guess (or command): 62
Congratulations! You guessed the correct number in 3 attempts!
You spent 10 sec. to solve it.
Do you wanna play again? [y/N]
```

