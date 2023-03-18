import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game():
    roll1, roll2 = roll_dice()
    roll_sum = roll1 + roll2
    if roll_sum == 7 or roll_sum == 11:
        print(roll_sum, "You win!")
    elif roll_sum:
        roll_sum == 2 or roll_sum == 3 or roll_sum == 12;
        print(roll_sum, "You lose!")
    else:
        goal = roll_sum
        print("Your goal is", goal)
        while True:
            roll1, roll2 = roll_dice()
            roll_sum = roll1 + roll2
            print("You rolled", roll_sum)
            if roll_sum == goal:
                print(roll_sum, "You win!")
                break
            elif roll_sum == 7:
                print(roll_sum, "You lose!")
                break

play_game()
