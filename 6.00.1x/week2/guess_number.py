low = 0
high = 100
guess = "50"
response =""

print("Please think of a number between 0 and 100!")


while True:
    print("Is your secret number " + guess + "?") 
    response = input("Enter 'h' to indicate the guess is too high. " \
        "Enter 'l' to indicate the guess is too low. " \
        "Enter 'c' to indicate I guessed correctly. ")
        

    if response in "chl":
        if response == "c":
            print("Game over. Your secret number was: " + guess)
            break
        else:
            if response == "h":
                high = int(guess)
            else:
                low = int(guess)
            
        guess = str(int((high + low)/2))
    else:
        print("Sorry, I did not understand your input.")
        
        