import random

#define rolling function
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

#define the game function
def play_game():
    roll1, roll2 = roll_dice()
    roll_sum = roll1 + roll2
   #the case of instant win by rolling 7 or 11
    if roll_sum == 7 or roll_sum == 11:
        print(roll_sum, "You win!")
   #the case of instant loss by rolling 2, 3, or 12
    elif roll_sum:
        roll_sum == 2 or roll_sum == 3 or roll_sum == 12;
        print(roll_sum, "You lose!")
   #the case of victory or loss after setting up a goal by youself
    else:
        goal = roll_sum
        print("Your goal is", goal)
        #setting the goal
        while True:
            roll1, roll2 = roll_dice()
            roll_sum = roll1 + roll2
            #rolling for the seconf time to determine whether the perosn won or lost
            print("You rolled", roll_sum)
            if roll_sum == goal:
                print(roll_sum, "You win!")
                break
            elif roll_sum == 7:
                print(roll_sum, "You lose!")
                break

play_game()
