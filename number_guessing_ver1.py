
import random
def secret_number():
    secret_num = random.randint(1,100)
    return secret_num

def user_input():
    while True:
        try:
            x = int(input("Enter a number between 1 and 100 \n"))
            if x < 1 or x > 100:
                print("please enter a number between 1 and 100")
                continue
            else:
                return x
        except ValueError:
            print("Enter a valid number")

def game_continuation():
    while True:
        
        choice = input().strip().lower()
        if choice in ("x", "o"):
            return choice
        else:
            print("Invalid choice! Please enter O or X only")
            continue

    

        

print("----------Welcome to number guessing game---------")
target = secret_number()
attempt = 0
print("Instructions:-- \n1. You have to guess a number between 1 and 100\n2. you have unlimited attempts\n3. After every attempt you can choose whether to continue or exit\n")
print("Let's Start the game")
while True:
    user_num = user_input()
    attempt += 1
    if user_num == target:
        print(f"Congratulations you have cleared the game in {attempt} attempts")
        break
    elif user_num > target:
        print("The number you guessed was too high")
    else :
        print("The number you guessed was too low")
    print(f"You have attempted {attempt} times")
    print("do you want to continue the game?\n If yes enter O \t If no enter X \n")
    choice = game_continuation()
    if choice == "o":
        continue
    else:
        print(f"the number you had to guess was {target}\nThank you for playing ")
        break
    
