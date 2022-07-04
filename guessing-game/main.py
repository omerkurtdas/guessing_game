
EASY = 10
HARD = 5
from art import logo
print(logo)
print("welcome to the guessing number game: \nI 'm thinking of a number somewhere between 1 and 100 ")
difficulty = input("choose a difficulty for the game 'hard' or 'easy'\n")


import random
def computer_guess ():
    """computer_guess function returns a int value between 1 and 100 """
    guess = random.randint(1,100)
    return guess
    
comp_guess = computer_guess() # calling the computer_guess func and return it to guess
print(f"Hint : the correct answer is {comp_guess}")


def compare(comp_guess, user_guess):
    if comp_guess < user_guess:
        return 1
    if comp_guess > user_guess:
        return 2
    if comp_guess == user_guess:
        return 0 #zero means our game is over
        

is_game_over = False
track = 0
while not is_game_over:
    if difficulty == "easy":       
        print(f"You have {EASY - track} remainings of attempts")
        track += 1
        
        if track == EASY:
            is_game_over = True
                  
    elif difficulty == "hard" :
        print(f"You have {HARD - track} remainings of attempts")
        track += 1
        if track == HARD:
            is_game_over = True
    user_guess = int(input("Make a guess : "))
    compare(comp_guess, user_guess)
    
  
    if compare(comp_guess, user_guess) == 0 :
        is_game_over = True
        print(f"Made it ! The correct answer is {comp_guess}")
        pass
    elif compare(comp_guess, user_guess) == 1 : 
        print("Lower.  ")
    elif compare(comp_guess, user_guess) == 2 : 
        print("Higher ")
    if compare(comp_guess, user_guess) != 0 and track == HARD : 
        print("you lose")
    if compare(comp_guess, user_guess) != 0 and track == HARD :    
        print("you lose")
    
    