from ctypes.wintypes import WORD


def game():
    print("*****************************")
    print("Welcome in Play the Hangman")
    print("*****************************")

    secret_word = "banana".upper()
    secret_letters = ["_" for letters in secret_word]

    hanged = False
    right = False
    errors = 0
    while (not hanged and not right):

        kick = input("Whats word?")
        kick = kick.strip().upper()
        if(kick in secret_word):
            index = 0
            for word in secret_word:
                if(kick == word):
                    secret_letters[index] = word
                index += 1
        else:
            errors += 1
        hanged = errors == 6
        right = "_" not in secret_letters
        print(secret_letters)

    if(right):
        print("Win")
    else:
        print("End of the game")


if(__name__ == "__main__"):
    game()
