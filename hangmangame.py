
import random

def hangman():
    words = ["python", "java", "kotlin", "hangman", "computer"]
    word = random.choice(words)  
    guessed_word = ["_"] * len(word)  
    
    attempts = 6  
    guessed_letters = []  

    print("Welcome to Hangman!")
    print("You have 6 chances to guess the word.\n")

    while attempts > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(guessed_letters))
        
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!\n")
        else:
            attempts -= 1
            print("Wrong guess!\n")

    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

hangman()
