import random
def secret_number():
    return random.randint(1,100)

def user_input():
    while True:
        try:
            x = int(input("Enter a number between 1 and 100 \n"))
            if x < 1 or x > 100:
                print("Please enter a number between 1 and 100")
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

def main():
    print("----------Welcome to number guessing game---------")
    print("----------Instructions:--------- \n1. You have to guess a number between 1 and 100\n2. You have only 10 attempts\n3. After every attempt you can choose whether to continue or exit\n")
    print("Let's Start the game")
    while True:
        
        target = secret_number()
        attempt = 0
        max_attempts = 10
        

        while True:
            user_num = user_input()
            
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