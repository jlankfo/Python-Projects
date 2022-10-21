print("Welcome to the game!")
SCORE = 0
playing = input("Would you like to play? ")

if playing.lower() == "yes":
    print("Awesome! Let's begin.")
else:
    quit()

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    SCORE+=1
    print("Correct! Your Score is now " + str(SCORE) + ".") 
else:
    print("This is incorrect. Your score is now " + str(SCORE) + ".")

answer = input("What is the most northern state? ")

if answer.lower() == "alaska":
    SCORE+=1
    print("Correct! Your Score is now " + str(SCORE) + ".") 
else:
    print("This is incorrect. Your score is now " + str(SCORE) + ".")

answer = input("Who was the first president? ")

if answer.lower() == "george washington":
    SCORE+=1
    print("Correct! Your Score is now " + str(SCORE) + ".") 
else:
    print("This is incorrect. Your score is now " + str(SCORE) + ".")

answer = input("What is the squart root of a negative number? ")

if answer.lower() == "imaginary":
    SCORE+=1
    print("Correct! Your Score is now " + str(SCORE) + ".") 
else:
    print("This is incorrect. Your score is now " + str(SCORE) + ".")

answer = input("Is John the coolest? ")

if answer.lower() == "yes":
    SCORE+=1
    print("Correct! Your Score is now " + str(SCORE) + ".") 
else:
    print("This is incorrect. Your score is now " + str(SCORE) + ".")

print("Your final score is " + str(SCORE) + " out of 5")