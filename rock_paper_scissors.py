"""
Program: rock_paper_scissors.py
Author: Russ LaScala


"""
import random 

#computer choices
computer = ['rock', 'paper', 'scissors']

#valid user choices
USERCHOICES = ('rock', 'paper', 'scissors')

# user input for name and number of games to play
print("Welcome to the Rock Paper Scissors game")
player1 = input("Enter your name: ")
games = int(input("Enter the number of games you would like to play: "))

#counter to hold number of games played and number of wins
gamecount = 0
compWins = 0
userWins = 0

#counter to hold number of games played and number of wins per player
gamecount = 0
compWins = 0
userWins = 0
tieGames = 0

while True:
    if gamecount != games:
        #starts game by asking user what choice they want to pick
        userChoice = input("Enter a valid choice, rock, paper, scissors: ")
        #gets random choice for computer 
        compChoice = (random.choice(computer))
        if userChoice == compChoice:
            print("\nIT WAS A TIE!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            tieGames += 1
        elif userChoice == 'rock' and compChoice == 'paper':
            print("\nCOMPUTER WINS!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            compWins += 1
        elif userChoice == 'rock' and compChoice == 'scissors':
            print("\nYOU WIN!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            userWins += 1
        elif userChoice == 'paper' and compChoice == 'scissors':
            print("\nCOMPUTER WINS!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            compWins += 1
        elif userChoice == 'paper' and compChoice == 'rock':
            print("\nYOU WIN!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            userWins += 1
        elif userChoice == 'scissors' and compChoice == 'paper':
            print("\nYOU WIN!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            userWins += 1
        elif userChoice == 'scissors' and compChoice == 'rock':
            print("\nCOMPUTER WINS!\nThe computer picked", compChoice, ", you picked", userChoice)
            gamecount += 1
            compWins += 1
        else:
            print("ERROR: invalid choice")
            print(userChoice)
    else: 
        print("")
        print("Game Over!!")
        print("computer won:", compWins, "games")
        print(player1, "you won:", userWins, "games")
        print("Tie Games:", tieGames, "games")
        print("")
        if compWins > userWins: 
            print("The computer is the winner!")
        elif userWins > compWins:
            print("You are the winner!")
        else: 
            print("It was a tie game!")
        break

