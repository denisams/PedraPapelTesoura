# Rock, Paper, Scissors Game

This is a simple implementation of the classic "Rock, Paper, Scissors" game in Python. The game allows a user to play against the computer, with the computer randomly selecting its move. The game continues in a loop until the user decides to stop playing.

## How It Works

The game is built using the `random` module to generate the computer's move and the `IntEnum` class from the `enum` module to define the possible actions: Rock, Paper, and Scissors.

### Game Actions

The actions are defined as an enumeration (`Acoes`), which includes:
- `Rock` (0)
- `Paper` (1)
- `Scissors` (2)

### Winning Conditions

The winning conditions are stored in a dictionary called `vitorias`:
- Scissors defeat Paper
- Paper defeats Rock
- Rock defeats Scissors

### Game Flow

1. The user is prompted to select one of the actions.
2. The computer randomly selects an action.
3. The winner is determined based on the rules of the game.
4. The result (win, lose, or draw) is displayed.
5. The user is asked if they want to play again. The game continues until the user decides to stop.

## How to Use

To run the game, you need to have Python installed on your computer. Follow the steps below to play the game:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. **Run the Game:**
   Execute the game script with Python:
   ```sh
   python game.py
   ```

3. **Follow the On-Screen Prompts:**
   - You will be prompted to enter your choice (Rock, Paper, or Scissors) by typing the corresponding number (0 for Rock, 1 for Paper, and 2 for Scissors).
   - The computer will randomly select its move.
   - The result of the game will be displayed.
   - You will be asked if you want to play again. Type `y` to play again or `n` to stop.

### Example

```
Enter your choice (Rock[0], Paper[1], Scissors[2]): 0
You chose Rock.
Computer chose Scissors.
Rock beats Scissors! You win!

Play again? (y/n): y
Enter your choice (Rock[0], Paper[1], Scissors[2]): 1
You chose Paper.
Computer chose Rock.
Paper beats Rock! You win!

Play again? (y/n): n
Thank you for playing!
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
