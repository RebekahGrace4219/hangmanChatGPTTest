# User Can you make it so that a little stick figure man gets printed in ascii in the terminal as the person loses?

def hangman(word, max_guesses):
    guessed_letters = []
    tries = max_guesses

    print("Let's play Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess! You have", tries, "tries left.")
            draw_hangman(tries)
        else:
            print("Correct guess!")

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You won!")
            return

    print("Game over! The word was:", word)
    draw_hangman(0)

def draw_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        '''
    ]
    print(stages[tries])

hangman("hangman", 6)
