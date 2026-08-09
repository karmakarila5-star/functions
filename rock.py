import random
while True:
    user = input("choose rock, paper, or scissors:")
    computer = random.choice(["rock","paper","scissors"])
    print("you chose:",user, "computer chose:",computer)
    if user == computer:
        print("it is a tie!")
    elif user == "rock":
        print("you win!" if computer == "scissors" else "you lose!")
    elif user == "paper":
        print("you win!" if computer == "rock" else "you lose!")
    elif user == "scissors":
         print("you win!" if computer == "paper" else "you lose!")
    if input("play again? (y/n): ") != "y":
        break