#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int user_input(int low, int high){
    int x;
    char input[50];
    char dummy;
    while(1){
        if(fgets(input, sizeof(input), stdin) == NULL){
            exit(1);
        }
        else{
            if(sscanf(input, "%d %1s", &x, &dummy) == 1){
                if (x > high || x < low){
                    printf("Please enter a number between %d and %d\n",low, high);
                }
                else{
                return x;
                }
            }
            else{
                printf("Please enter a valid number between %d and %d\n", low, high);
                }
            }
    }
}

char choose_level(){
    while(1){
        char input[50];
        char level;
        char dummy;
        printf("For easy level: enter 'e'\nFor medium level: enter 'm'\nFor Hard level: enter 'h'\n\n");
        if(fgets(input, sizeof(input), stdin) == NULL){
            exit(1);
        }
        else{
            if(sscanf(input, " %c %1s", &level, &dummy) == 1 && (level == 'e' || level =='E' || level == 'm' || level == 'M' || level == 'h' || level == 'H')){
                return level;
            }
            else{
                printf("You can only enter e, m, h\n");
            }
        }
    }
}

void instructions(char level, int low, int high){
    if (level == 'e' || level == 'E'){
        printf("1. You have to guess a number between %d and %d\n2. You have only 12 attempts\n", low,high);
    }
    else if (level == 'm' || level == 'M'){
        printf("1. You have to guess a number between %d and %d\n2. You have only 10 attempts\n", low, high);
    }
    else{
        printf("1. You have to guess a number between %d and %d\n2. You have only 8 attempts\n", low, high);
    }
}

char get_choice(){
    char input[50];
    char choice;
    char dummy;
    while(1){
        if(fgets(input, sizeof(input), stdin) == NULL){
            exit(1);
        }
        else{
            if(sscanf(input," %c %1s", &choice, &dummy) == 1 && (choice == 'x' || choice =='X' || choice == 'o' || choice == 'O')){
                return choice;
            }
            else{
                printf("Error! You can only enter X or O\n");
            }
        }
    }
}

void show_difference(int a, int b){
    int difference = abs(a - b);
    if(difference <=5){
        printf("You are too close\n");
    }
    else if(difference <= 10){
        printf("You are close\n");
    }
    else{
        printf("You are far from the target\n");
    }
}

char play_again(){
    printf("Do you want to play again\n Enter o if yes\t Enter x if no\n");
    return get_choice();
}

int main(){
        printf("Welcome to number guessing game\n");
        //printf("----Instructions----\n 1. You have to guess a number(integer) between 1 and 100\n 2. You have only 10 attempts\n 3. After every attempt you can choose to continue or exit the game\n");
        srand(time(NULL));
        while(1){


        char level;
        level = choose_level();
        int max_attempts;
        int low = 1;
        int high;
        if (level == 'e' || level == 'E'){
            max_attempts = 12;
            high = 50;
        }
        else if (level == 'm' || level == 'M'){
            max_attempts = 10;
            high = 100;
        }
        else{
            high = 200;
            max_attempts = 8;
        }
        instructions(level, low, high);
        printf("You can choose to continue or exit the game after every incorrect attempt\n");


        int guess, target;
        
        char choice;
        int attempt = 0;
        

        
        target = (rand() % high) + 1;
        
        while(1){
            attempt++;
            printf("Guess a number between 1 and %d\n", high);
            guess = user_input(low, high);
            if (guess == target){
                printf("Congratulations you cleared the game in %d attempts\n",attempt);
                break;
            }
            else if (guess > target){
                printf("The number was higher than the target\n");
            }
            else {
                printf("The number was lower than the target\n");
            }

            if(attempt == max_attempts){
                printf("You could not clear the game\n");
                printf("The number you had to guess was %d\n",target);
                break;
            }

            show_difference(target, guess);
            printf("You have attempted %d times\n",attempt);
            printf("Now you have only %d attempts\n",max_attempts - attempt);
            printf("Do you want to continue the game ?\n If Yes enter O\n If No enter X\n");
            choice = get_choice();
            if (choice == 'o' || choice =='O'){
                continue;
            }
            else{
                printf("The number you had to guess was %d\n Thank you for playing the game\n",target);
                return 0;
            }
        }
        char again = play_again();
        if (again == 'o' || again == 'O'){
            continue;
        }
        else{
            printf("Thank you for playing\n");
            break;
        }
    
    }
return 0;
}