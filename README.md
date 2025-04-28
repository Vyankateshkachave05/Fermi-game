📒 Three-Digit Number Guessing Game

A fun Python-based number guessing game where players must guess a secret three-digit number.
Hints like "Fermi" and "Pico" are provided to guide the player toward the correct number.

🚀 Key Features

🎯 Guess a hidden three-digit number

🎲 Receive hints after each guess:

Fermi: Correct digit in the correct position

Pico: Correct digit but in the wrong position

🚫 Prevents invalid inputs (wrong length, duplicate numbers)

🏆 Win the game by guessing the correct number!

🛠 Technologies Used

Python 3

💻 How to Run

Make sure Python is installed on your machine.

Save the code in a .py file (e.g., number_guess_game.py).

Open Terminal (macOS/Linux) or Command Prompt (Windows).

Navigate to the directory where your file is saved.

Run the game:

bash

Copy

Edit
python number_guess_game.py

📂 Code Workflow

original_number is predefined (e.g., '123').

The program runs inside an infinite while loop until the player wins.

Input Validation:

The guess must have exactly three digits.

Duplicates are not allowed (each digit must be unique).

Gameplay Hints:

If a digit is correct and in the correct position, "Fermi" is added to the hint list.

If a digit is correct but in the wrong position, "Pico" is added.

If no digits match, an empty list is shown.

Winning Condition:

If the guessed number matches the original number exactly, the player is congratulated, and the game ends.

📢 Important Notes

The game uses the continue statement to re-prompt for input if the guess is invalid.

The game uses the break statement to exit the loop once the player guesses correctly.

The secret number (original_number) is currently hard-coded; you can enhance the game by generating it randomly.

📊 Example Game Flow

less

Copy

Edit

Enter a Three digit number : 124

['Fermi', 'Fermi']

Enter a Three digit number : 321

['Pico', 'Pico', 'Pico']

Enter a Three digit number : 123

Fermi

You Win
