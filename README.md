# Spaceman

## Description

Spaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time. A placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word. If the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders. Guess the word before you run out of guesses!

Users win if they can guess the mystery word before the spaceman is drawn. The spaceman is made up of seven parts, and each part is drawn for each incorrect guess. If all seven parts get drawn before the user guesses the word, then they lose.

Check out an [example demo of winning the game](https://drive.google.com/file/d/1BkhVQoLoqaI4rb9OM8nP6Kb-UzxQfCwO/view?usp=sharing)
Check out an [example demo of losing the game](https://drive.google.com/file/d/1NkUsr-tVsLW8vBhuexZYb7ABwKftrEAY/view?usp=sharing)


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

### Stretch Requirements/Challenges (Optional)

- Alert the user if they guessed a letter they already guessed, and don’t have it count as an incorrect guess
- Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
- Prompt  the user to play again after a game ends. If they say yes, then start a new game.
- Change the number of incorrect guesses allowed to match the length of the mystery word
- Show the user the mystery word when they lose
- Use [ASCII art](https://en.wikipedia.org/wiki/ASCII_art) to draw the spaceman with each incorrect guess
- Add error handling to your Spaceman project and improve code quality using the feedback you gained from the previous activity.
- Sinister Spaceman: After the user guesses a correct letter, change the mystery word to be a new mystery word that is the same word length and uses the same correctly guessed letters
	- Example: mystery word is "car”, user guesses "a”, the user is shown "_a_”, but the word is now changed to "bar”
		- User guesses "c”, which results in an incorrect guess.
		- They then guess "b”, the user is shown "ba_”, but the word is now changed to "bat”
		- User guesses "r”, which results in an incorrect guess.
		- User guesses "t”, which results in a correct guess, and the user wins
