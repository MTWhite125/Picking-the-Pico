from random import randint

num = randint(1,10) 
userGuess = None  

while(userGuess != num): 
    userGuess = int(input("Please enter a guess between 1 and 10: ")) 
    if userGuess > num: 
        print("Your guess is too high") 
    elif userGuess < num: 
        print("Your guess is too low") 
    elif userGuess == num: 
        print("You win") 