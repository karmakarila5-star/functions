import random
number = str(random.randint(0,9))
print("guess the number from 0 to 9!")
while True:
    guess = input("your guess:")
    if guess == number:
        print("you win! the number was", number)
        break
    else:
        print("wrong! try again,")
