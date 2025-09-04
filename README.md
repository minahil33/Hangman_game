# Hangman Game 🎮 (Python)
Overview

This is a simple Hangman game implemented in Python. The computer randomly selects a word from a predefined list, and the player has to guess it letter by letter. The player has six chances to make wrong guesses before the game ends. With every incorrect guess, the hangman figure progresses until either the player wins by finding the word or loses when all attempts are used.

Features

Random word selection from a list.

One-letter input system for guesses.

Tracks and prevents repeated guesses.

Displays the current progress of the guessed word.

Shows hangman drawing after each wrong attempt.

Ends with a clear win or loss message.

How It Works

A word is chosen randomly from a stored list.

The chosen word is hidden with underscores.

The player enters one letter at a time to guess the word.

If the letter is correct, it is revealed in the hidden word.

If the letter is wrong, the number of attempts decreases and the hangman figure updates.

The game continues until the word is fully guessed or no attempts are left.

Gameplay Flow

Start: The game shows the hidden word as underscores.

Input: The player types a letter.

Correct Guess: The letter appears in the word.

Wrong Guess: An attempt is lost, and the hangman drawing updates.

Win Condition: All letters are guessed before attempts run out.

Lose Condition: Six wrong attempts lead to game over, and the correct word is revealed.

Sample Playthrough

Hidden word: _ _ _ _ _

Player guesses “o” → Revealed: _ o o _ _

Player guesses “z” → Wrong guess, hangman figure updates.

Game continues until the player wins or loses.

Future Enhancements

Add difficulty levels such as Easy, Medium, and Hard.

Option for custom words input by the user.

Scoring system to track multiple rounds.

Graphical version using Tkinter or Pygame.
