# Hangman Game

Welcome to the Hangman game! In this game, the computer will randomly choose a word, and you will try to guess what the word is. Good luck and have fun playing!

## How to Play

1. **Starting the Game:**
   - The computer will randomly select a word from a list of animals.
   - You will choose the difficulty level: Easy or Hard.

2. **Guessing the Word:**
   - The word will be displayed as a series of asterisks (`*`), with each asterisk representing a letter in the word.
   - You will guess letters one at a time, or you can try to guess the whole word.

3. **Making a Guess:**
   - If you guess a letter that is in the word, it will be revealed in its correct position(s).
   - If you guess a letter that is not in the word, a part of the hangman will be drawn.
   - You have a maximum of 7 incorrect guesses before the game ends.

4. **Winning or Losing:**
   - You win if you guess the word before the hangman is fully drawn.
   - You lose if the hangman is fully drawn before you guess the word.

## Difficulty Levels

- **Easy:** The word is chosen from a list of common animals.
- **Hard:** The word is chosen from a list of less common animals.

## Rules
- The computer selects a random word from the chosen difficulty level.
- Guess letters one at a time or try to guess the whole word.
- Each incorrect guess results in a part of the hangman being drawn.
- You have up to 7 incorrect guesses before the game ends.

## Enjoy the Game!
Test your guessing skills and try to save the hangman by figuring out the word as quickly as possible. *Good luck!*

---

## Example

```plaintext
Welcome to Hangman
The computer will randomly choose a word and you will try to guess what the word is
Good Luck! Have fun playing

please choose between:
(1) Easy
(2) Hard
1

       O       
You have 7 attempts left.
********

Guess a letter in the word or enter the full word: e
You input e, Great! That letter exists in the word!

       O       
You have 7 attempts left.
*e*e***e

Guess a letter in the word or enter the full word: r
Sorry, that letter is not part of the word.

       O       
+------|       
You have 6 attempts left.
*e*e***e

...

Congratulations!!! You guessed the word correctly!
It is in fact "elephant"
You won!
Do you want to play again? (y/n): n
End Game.
Hope you had fun playing the game. See you next time
