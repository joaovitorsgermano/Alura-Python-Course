import Guess
import hangman

print("*****************************")
print("Escolha o Jogo")
print("*****************************")

print("(1) Guess Game (2)  Hangman Game ")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Guess Game")
    Guess.game()
elif(jogo == 2):
    print("Hagman Game")
    hangman.game()
