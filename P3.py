import random

RandomIntiger = random.randint(1, 100)
GuessList = []
UserGuess = None

print("Welcome to Guess the Number game! Guess a number between 1 and 100.")

while True:
    try:
        UserGuess = int(input("Guess Your Number:\n"))
        GuessList.append(UserGuess)
        
        if UserGuess > RandomIntiger:
            print("Too High, Re Enter A Lower Number")
        elif UserGuess < RandomIntiger:
            print("Too Low, Re Enter A Higher Number")
        else:
            print(f"Congratulations, The Number Was {RandomIntiger}")
            print(f"It Took You {GuessList.__len__()} Guess To Guess This Number, Your Guesses Was:")
            print(GuessList)
            break
    except:
        print("Please Reguess Your Number And Enter Just Intiger Number")