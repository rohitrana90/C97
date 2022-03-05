import random
print("Number Guessing Game")
Number = random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")

while chances < 5:

    guess = int(input("Enter your guess: "))



    if guess == Number:
        print(" Congrulation! YOU WIN!!")
        break

    elif guess < Number:
        print("YOUR guess was to low")

    else :
        print( "Your guess was to low")

        chances =+1

        if not chances <5 :
            print("You lose!!")

