import random
def secret_number(low, high):
    return random.randint(low,high)

def user_input(low, high):
    while True:
        try:
            x = int(input(f"Enter a number between {low} and {high} \n"))
            if x < low or x > high:
                print(f"Please enter a number between {low} and {high}")
                continue
            return x
        except ValueError:
            print("Enter a valid number")

def game_continuation():
    
    print(" If yes enter O \t If no enter X \n")
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in ("x", "o"):
            return choice
        print("Invalid choice! Please enter O or X only")

def show_difference(a, b):
    difference = abs(a - b)
    if difference <= 5:
        print("You are too close to the target")
    elif difference <= 10:
        print("You are close to the target")
    else:
        print("You are far from the target")

def play_again():
    print("Do you want to play again? ")
    return game_continuation()

def choose_level():
    while True:
        print("For easy level: enter 'e'\nFor medium level: enter 'm'\nFor Hard level: enter 'h'\n\n")
        level = input("Enter your choice: ").strip().lower()  
        if level in ("e", "m", "h"):
            return level
        else:
            print("Enter a valid choice")

def instructions(low, high, level):
    if level == "e":
        print(f"1. You have to guess a number between {low} to {high}\n2. You have 12 attempts left")
    elif level == "m":
        print(f"1. You have to guess a number between {low} to {high}\n2. You have only 10 attmepts left")
    else:
        print(f"1. You have to guess a number between {low} to {high}\n2. You have only 8 attempts left")

def main():
    print("----------Welcome to number guessing game---------")
    #print("----------Instructions:--------- \nFor Easy level:--\n1. You have to guess a number between 1 and 50\n2. You have only 12 attempts\nFor medium level:--\n1. You have to guess a number between 1 and 100\n2. You have only 10 attempts\nFor hard level:--\n1. You have to guess a number between 1 and 200\n2. You have only 8 attempts\n\nAfter every attempt you can choose whether to continue or exit\n")
    
    while True:
        level = choose_level()
        low = 1
        if level == "e":
            high = 50
            max_attempts = 12
        elif level == "m":
            high = 100
            max_attempts = 10
        else:
            high = 200
            max_attempts = 8
        instructions(low, high, level)
        print(f"You can choose to exit or continue the game after every attempt")
        target = secret_number(low, high)
        attempt = 0
        
        

        while True:
            user_num = user_input(low, high)
            
            attempt += 1
            if user_num == target:
                print(f"Congratulations you have cleared the game in {attempt} attempts")
                break
            elif user_num > target:
                print("The number you guessed was higher than the target")
            else:
                print("The number you guessed was lower than the target")

            if attempt == max_attempts:
                print("You could not clear the game.")
                print(f"The number you had to guess was {target}")
                break
            
            show_difference(user_num, target)
            print(f"You have attempted {attempt} times\n you have only {max_attempts - attempt} attempts left")
            print("Do you want to continue the game?")
            choice = game_continuation()
            if choice == "o":
                continue
            else:
                print(f"The number you had to guess was {target}\nThank you for playing ")
                return
          
        if play_again() == "o":
            continue
        else:
            break
    
if __name__ == "__main__":
    main()