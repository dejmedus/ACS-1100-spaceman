import random
import os


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    # get the word file
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    # split the file into a list of words
    words_list = words_list[0].split(' ')

    # choose a random word from the list to return
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, guessed_letters):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        guessed_letters (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in guessed_letters, False otherwise
    '''

    # check each character to see if it is in the list of letters guessed
    for char in secret_word:

        # if a character is not in the list, return false
        if char not in guessed_letters:
            return False

    # if we make it to the end, return true
    return True


def get_guessed_word(secret_word, guessed_letters):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        guessed_letters (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    guessed_string = ""

    # iterate through all the characters in the secret word
    for char in secret_word:

        # if the character is in the list of guessed letters, add it to our string
        if char in guessed_letters:
            guessed_string += char
        # if the character is not in the list of guessed letters, add an underscore
        else:
            guessed_string += "_"

    # return the string we've built
    return guessed_string


def display_intro_message(chances):
    '''
    A function that displays the intro message including the amount of letters in the secret word and total incorrect guesses.

    Args:
        chances (number): the amount of chances left to guess the word.
    '''

    os.system('clear')

    intro_message = f"""
Welcome to Spaceman! 👽🚀
The secret word contains: {len(secret_word)} letters
You get {chances} incorrect guesses.

            """
    print(intro_message)


def display_guess_message(guess, guessed_letters, unguessed_letters, chances):
    '''
    A function that displays feedback to user on game loop

    Args:
        guess (string): the guessed character
        guessed_letters (list): list of already guessed characters
        unguessed_letters (string): characters that have not been guessed by user
        chances (number): the amount of chances left to guess the word
    '''

    guess_message = ""

    # check if the guessed letter is in the secret or not
    if guess in secret_word:
        guess_message += "Your guess appears in the word!\n"
    else:
        guess_message += f"""
Your guess doesn't appears in the word
You have {chances} incorrect guesses left
"""
    # show the guessed word so far
    current_guess = get_guessed_word(secret_word, guessed_letters)
    guess_message += f"Guessed word so far: {current_guess}"

    # show the letters that haven't been guessed words so far
    unguessed_letters = unguessed_letters.replace(guess, "")
    guess_message += f"""
These letters haven't been guessed yet: {unguessed_letters}

"""
    print(guess_message)


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    guessed_letters = []
    unguessed_letters = "abcdefghijklmnopqrstuvwxyz"
    chances = len(secret_word)

    # show the player information about the game according to the project spec
    display_intro_message(chances)

    # if game hasn't been lost, continue the game loop
    while chances > 0:
        # ask the player to guess one letter per round and check that it is only one letter
        guess = input("Enter a letter: ").lower().strip()

        # if the guess is more than one character, re-prompt the user
        if len(guess) > 1:
            print("Please enter a valid letter")
            continue

        # if the guess has already been tried, re-prompt the user
        if guess in guessed_letters:
            print(f"""You've already tried the letter {guess}
These letters haven't been guessed yet: {unguessed_letters}

""")
            continue

        guessed_letters.append(guess)

        # if the guess is incorrect, remove a chance
        if guess not in secret_word:
            chances = chances - 1

        display_guess_message(guess, guessed_letters,
                              unguessed_letters, chances)

        # check if the game has been won or lost and display to user
        is_game_won = is_word_guessed(secret_word, guessed_letters)

        if is_game_won:
            print("You won!")
            os.system("exit")

    print(f"You lost, the secret word was: {secret_word}")


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
