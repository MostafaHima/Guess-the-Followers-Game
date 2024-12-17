# Higher Lower Game

This is a fun game where the player has to guess which account has more followers based on two randomly selected accounts. The game will display the names, descriptions, and countries of the accounts, and the player has to guess which one has more followers. The score is updated after each round, and the game continues until the player makes an incorrect guess.

## Requirements

To run this game, you'll need the following:

- Python 3.x
- The following Python modules:
  - `random` (standard library)
  - `art` (for displaying logos)
  - `data` (contains account data)

You can install the required modules using `pip` if necessary.

## Setup

1. Clone or download the repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install any required dependencies (if applicable).

## Game Instructions

1. The game will show two accounts with their follower counts.
2. You need to guess which account has more followers by typing `A` or `B`.
3. If you guess correctly, your score will increase.
4. If you guess incorrectly, the game ends, and your final score will be displayed.

## How to Play

1. Run the `main.py` file to start the game.
2. The game will randomly select two accounts and display the necessary information.
3. Type `A` if you think account A has more followers, or `B` if you think account B has more followers.
4. The game will provide feedback and continue until an incorrect guess is made.

## Example Output
```python
Followers of A: 123K vs Followers of B: 456K Compare A: Taylor Swift, a singer, from the USA

VS

Against B: Cristiano Ronaldo, a footballer, from Portugal

Who has more followers? Type A or B: B 🎉 Correct! Your current score is 1.

