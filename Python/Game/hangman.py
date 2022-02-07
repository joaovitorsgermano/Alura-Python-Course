from ctypes.wintypes import WORD
import random


def game():

    display()

    secret_word = jogar()
    secret_letters = initializes_letters_correct(secret_word)

    hanged = False
    right = False
    errors = 0
    while (not hanged and not right):

        kick = get_kick()

        if(kick in secret_word):

            mark_kick_correct(kick, secret_letters, secret_word, )

        else:
            errors += 1
            draw_gallows(errors)
        hanged = errors == 7
        right = "_" not in secret_letters
        print(secret_letters)

    if(right):
        get_message_wener()
    else:
        get_message_loser(secret_word)


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def get_message_wener():
    print("Congratulation, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def get_message_loser(secret_word):
    print("Gosh, you've been hanged!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mark_kick_correct(kick, secret_letters, secret_word, ):
    index = 0
    for word in secret_word:
        if(kick == word):
            secret_letters[index] = word
        index += 1


def get_kick():
    kick = input("Whats word?")
    kick = kick.strip().upper()
    return kick


def initializes_letters_correct(secret_word):
    return ["_" for letters in secret_word]


def display():

    print("*****************************")
    print("Welcome in Play the Hangman")
    print("*****************************")


def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


if(__name__ == "__main__"):
    game()
