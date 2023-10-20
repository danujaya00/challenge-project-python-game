#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

import random

def play_game():
    elements = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("\nChoose rock, paper, or scissors: ").lower()

        if player_choice not in elements:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(elements)
        print(f"\nComputer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Your score: {player_score}, Computer score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        # If the player doesn't enter "yes" or "no", show them invalid input message and ask again
        while play_again != 'yes' and play_again != 'no':
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
        
        if play_again != 'yes':
            print("\nGame over. Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()



@app.route("/")
def hello():
    return app.send_static_file("index.html")
