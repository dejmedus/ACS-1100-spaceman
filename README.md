# Spaceman

#### Winning Game

https://github.com/user-attachments/assets/6a857bee-89e2-4864-bd16-8765d475c8df

#### Losing Game

https://github.com/user-attachments/assets/ce2c8cfe-9829-4eca-b7e3-0fa81026e89a


## Requirements

- User must be able to enter letters to guess
- The user must get accurate feedback on if they guessed a correct letter or an incorrect letter
- The user is always prompted to guess a letter until they win or lose
- The game must use the [provided list of words](#resources) as its source.
- User is allowed seven (7) incorrect guesses, and they should be told how many guesses they have left after each incorrect guess
- After guessing a letter, the user must be told the following:
	- Correct guess: the placeholder text with the correct letter filled in.
		- If the word is "dog" and they guess "g" as their first guess, they should see _ _ g
		- Incorrect guess: a message telling them their guess is incorrect, and then the number of guesses they have remaining
- If a guessed letter appears multiple times in the word, that guessed letter should appear in all valid blanks
- Correct Example (word is "apple”): p → _ pp_ _
- Incorrect Example (word is "apple”): p → _p_ _
- If a user successfully guesses all the letters, the game ends, and the user is shown a message notifying them that they won
- If a user guesses incorrectly seven (7) times, the game ends, and the user is shown a message notifying them that they lost

### Stretch Requirements

- Alert the user if they guessed a letter they already guessed, and don’t have it count as an incorrect guess
- Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
- Show the user the mystery word when they lose
- Use [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) to draw the spaceman with each incorrect guess
