secret = "4256"

print("Your goal is to guess the correct number")


while True:
    guess = input("Your number guess: ")
    bulls = 0    
    cows = 0

    for i in range(4):
        if guess [i] == secret[i]: 
            bulls += 1
        elif guess[i] in secret: 
            cows +=1
        
    print ("Bulls: ", bulls)
    print ("Cows: ", cows)  
    
    if bulls == 4: 
        print("Congratulations... you won")    
        break
        