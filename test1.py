import random
# Prompt: Can you write me a python program to play the game hangman?
def hangman():
    words = ['python', 'hangman', 'game', 'openai', 'programming', 'computer']
    word = random.choice(words).lower()
    guessed_letters = []
    tries = 6

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

hangman()
