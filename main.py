numberToGuess = 18                      # Binary: 0b10010
turns = 5                               #Hexa: 0x5

print("\t\t\t ******************* Guess a number between 0 to 50 ******************* ")

while True:

    guess = int(input("Guess the number : "))
    if guess > numberToGuess:
        if guess > 50:
            print("your number can not be greater than 50.")
            continue
        else:
            print("greater value, plz think a smaller value.")
            turns = turns - 1
            print("turns left :", turns)

    elif guess < numberToGuess:
        if guess < 0:
            print("your number can not be less than 0.")
            continue
        else:
            print("lesser value, plz think a greater value.")
            turns = turns - 1
            print("turns left :", turns)

    else:
        numberOfGuessesToSolve = 6 - turns
        print("\n\n\t\t\t Congratulation! You have guessed in ", str(numberOfGuessesToSolve) + "th attemp.")
        print("\n\n\t\t\t ******************* you win! ******************* ")
        break

    if turns == 0:
        print("\n\n\t\t\t ******************* game over! ******************* ")
        break