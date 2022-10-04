import random
while True:
 user_choice=input("enter your choice 'Rock','paper','scissors ")
 actions=['rock','paper','scissors']
 computer_choice=random.choice(actions)
 print("you chose the {user_choice} and the computer chose{computer_choice}")
 if user_choice==computer_choice:
    print("tie")
 elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print("the rock smashes the scissor ! you  win")
 elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print("the scissor cuts the paper ! you  win ")
 elif user_choice=='paper':
    if computer_choice=='scissors':
        print("computer wins! scissors cuts the paper ! you  loose")
 play_again=input("play again y or n")
 if play_again.lower() !='y':
     break
