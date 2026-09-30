import random

words = ["lecture", "library", "school", "basketball", "football"]
secret = random.choice(words)
guessed = ""
mistakes = 0

print("Word:", "_" * len(secret))

while mistakes < 6:
    letter = input("Your letter: ")
    
    if len(letter) != 1:
        print("you can only guess 1 letter at a time!")
        letter = input("Your letter dude: ") 
        

    guessed += letter

    if letter not in secret:
        mistakes += 1

    visible = ""
    for character in secret:
        if character in guessed:
            visible += character
        else:
            visible += "_"

    print("Word:", visible)
    print("Mistakes left: ", 6 - mistakes)

    if visible == secret:
        print("You won and guessed the correct word!")
        break

if mistakes == 6:
    print("The word was:", secret)    