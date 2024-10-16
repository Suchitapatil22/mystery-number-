import random
target = random.randint(1,50)

while True: 
    userChoice = (input("Guess the number between 1 to 50 or Quite : "))
    
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("YOU WiN : Correct Guess !!")
        break
    elif(userChoice < target):
        print("Your guess is too small. Take a bigger guess...")
    else: 
        print("Your Guess is too big. Take a smaller Guess...")


print("-----GAME OVER-----")