secret = 67
attempts = 5
guess = int(input("Guess the number: "))
for attempts in range (attempts-1 ,0,-1):
    if guess < secret:
        print ("too low\nattempts left:", attempts)
    elif guess > secret:
        print("too high\nattempts left:", attempts)     
    elif guess == secret:
        print("Congratulation!")
        break
    guess = int (input("guess again: "))
        
if guess != secret:
    print("Game Over!\nThe secret number was",secret)