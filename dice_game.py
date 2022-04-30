import random

tries = 1
score = 50

diceCount = random.randrange(1, 7)

while True:
    playerGuess = input("Enter your Guess: ")

    if playerGuess.isdigit():
        playerGuess = int(playerGuess)
    else:
        print("Please type a number.")
        continue  
    
    if playerGuess == diceCount:
        if tries == 1:
            print("Wow you guessed it in the first try!!")
            print("Your score is 50 points!")
            break        
        else:
            print("You took " + str(tries) + " tries to guess the number!")
            print("Your score is " + str(score) + " points!")
            break
        
    else:
        tries += 1
        score -= 10
        if playerGuess > diceCount:
            print("You were above the number!")
        elif playerGuess < diceCount:
            print("You were below the number!")
        continue        