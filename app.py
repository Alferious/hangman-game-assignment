import random
def choose(): 
    words = ["abyss","banjo","blitz","equip","funny","ivory","scratch","mnemonic"]
    return random.choice(words)  #the computer will choose the random word from the list

def show(word, guesses):

    display = ""

    for letter in word:
        if letter in guesses:
            display = display + letter
        else:
            display = display + '_'
    return display

def hangman_game():
    word = choose()
    guesses = []
    failed_attempts = 6

    while failed_attempts>0:
        print(show(word, guesses))
        guess = input("Guess a letter:")

        if len(guess) !=1:
            print("Enter one letter only")

            continue
        if guess in guesses:
            print("You have already guessed this, try again!")
            continue

        guesses.append(guess)

        if guess not in word:
            failed_attempts = failed_attempts - 1
            print(f"Wrong guesses, {failed_attempts} left")
        else:
            print("Correct guess")

        if all(guess in guesses for guess in word):
                print("You have won")

                break
    if failed_attempts == 0:
        print(f"You lost, this was the word, {word}")


hangman_game()