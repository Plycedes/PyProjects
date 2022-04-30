print("Welcome to Quiz Game!")

consent = input("Do you want to play? y/n ")

if consent.lower() != "y":
    quit()

print("Okay! Let's play this game")
score = 0

answer = input("What is the name of the tallest mountain in the world?")
if answer.lower() == "mount everest":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the first person to land on the moon?")
if answer.lower() == "neil armstrong":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which is the most populated country in the world?")
if answer.lower() == "china":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the USA stand for?")
if answer.lower() == "united states of america":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("When did India gain it's independence from imperialism?")
if answer.lower() == "1947":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Game Over!")
print("Your score: " + str(score))
print("Thank you for playing!")