#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

def play_game():
    #a default score value
    user_score = 0
    computer_score = 0
    user_name = input("What is your name: ").capitalize()
    should_continue = True
    while should_continue: 
        
        game_sign = ["rock", "paper", "scissors"]
        
        #user enters desired move
        user_choice = input(f"\nWhat do you choose?{game_sign}: ").lower()
        print(f"You Choose:{user_choice}")
        
        #computer randomly picks from the list of move available
        computer_choice = random.choice(game_sign)
        print(f"The Computer choose: {computer_choice}\n")
    
        #the rule of the game
        #rock beat scissors
        #scissors beat paper
        #paper beat rock
        # a tie when computer_choice and user_choice is the same
        
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie😤!")
            #since it's a tie, the score for both player is +0
            user_score +=0
            computer_score +=0
            print(f"{user_name} {user_score} : {computer_score} Computer")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win🎉!")
                #from the rule of the game, rock(user_choice) beat scissors(computer_choice)
                #since the user win, the user score is updated by 1
                user_score +=1
                computer_score +=0
                print(f"{user_name} {user_score} : {computer_score} Computer")
            elif computer_choice == "paper":
                print("Paper covers rock! You lose😔.")
                user_score +=0
                computer_score +=1
                print(f"{user_name} {user_score} : {computer_score} Computer")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win🎉!")
                user_score +=1
                computer_score +=0
                print(f"{user_name} {user_score} : {computer_score} Computer")
            elif computer_choice == "scissors":
                print("Scissors cuts paper! You lose😔.")
                user_score +=0
                computer_score +=1
                print(f"{user_name} {user_score} : {computer_score} Computer")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win🎉!")
                user_score +=1
                computer_score +=0
                print(f"{user_name} {user_score} : {computer_score} Computer")
            elif computer_choice == "rock":
                print("Rock smashes scissors! You lose😔.")
                user_score +=0
                computer_score +=1
                print(f"{user_name} {user_score} : {computer_score} Computer")
                
                
        if user_score == 5 or computer_score ==5:
            #first player to get a score of 5 is the winner
            play_again = input("Do you want to play again😉? (yes/no): ").lower()
            if play_again == "yes":
                user_score = 0
                computer_score = 0
                time.sleep(10)
                #a time function to sleep for 10secs so that the player can relax
                should_continue =True
            else:
                sure = input("Are you sure you want to exit the game? (yes/no)").lower()
                #a re-comfirmation if the user wants to end the game
                if sure == "yes":
                    print("\nThank you for playing!")
                    should_continue = False
                else:
                    #if not, runs the game again and start the scores from 0
                    user_score = 0
                    computer_score = 0
                    should_continue = True


# In[2]:


play_game()


# In[ ]:




