#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int user_input(){
    int x;
    char input[50];
    char dummy;
    while(1){
        if(fgets(input, sizeof(input), stdin) == NULL){
            exit(1);
        }
        else{
            if(sscanf(input, "%d %1s", &x, &dummy) == 1){
                if (x > 100 || x < 1){
                    printf("Please enter a number between 1 and 100\n");
                }
                else{
                return x;
                }
            }
            else{
                printf("Please enter a valid number between 1 and 100\n");
                }
            }
    }
}


char get_choice(){
    char input[50];
    char real;
    char dummy;
    while(1){
        if(fgets(input, sizeof(input), stdin) == NULL){
            exit(1);
        }
        else{
            if(sscanf(input," %c %1s", &real, &dummy) == 1 && (real == 'x' || real =='X' || real == 'o' || real == 'O')){
                return real;
            }
            else{
                printf("Error! You can only enter X or O\n");
            }
        }
    }
}


int main(){
    int guess, target;
    int attempt = 0;
    char choice;
    srand(time(NULL));
    target = (rand() % 100) + 1;
    printf("Welcome to number guessing game\n");
    printf("----Instructions----\n 1. You have to guess a number(integer) between 1 and 100\n 2. You have unlimited attempts\n 3. After every incorrect attempt you can choose to continue or exit the game\n");
    while(1){
        attempt++;
        printf("Guess a number between 1 and 100\n");
        guess = user_input();
        if (guess == target){
            printf("Congratulations you cleared the game in %d attempts\n",attempt);
            break;
        }
        else if (guess > target){
            printf("The number was too high\n");
        }
        else {
            printf("The number was too low\n");
        }
        printf("You have attempted %d times\n",attempt);
        printf("Do you want to continue the game ?\n If Yes enter O\n If No enter X\n");
        choice = get_choice();
        if (choice == 'o' || choice =='O'){
            continue;
        }
        else{
            printf("The number you had to guess was %d\n Thank you for playing the game\n",target);
            break;
        }
    }
return 0;
}