import random


def rock_paper_scissors():

    # Welcome message and game instructions
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    choices = ["rock", "paper", "scissors"]

    # Variables to keep track of scores
    player_score = 0
    computer_score = 0

    # Game loop
    while True:
        # Accept user input
        player_choice = input("Your choice: ")

        # Generate random choice for the computer
        computer_choice = random.choice(choices)

        while player_choice not in choices:
            print(f"{player_choice} is not a valid choice!")
            player_choice = input("Your choice: ")

        # Compare the choices and determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            print(f"I chose {computer_choice}")
            player_score += 1
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
            print(f"I chose {computer_choice}")
            player_score += 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            print(f"I chose {computer_choice}")
            player_score += 1
        else:
            print("You lose!")
            print(f"I chose {computer_choice}")
            computer_score += 1
        # Add conditions for other winning scenarios: paper beats rock, scissors beats paper

        # Display the current score
        print("Score - You:", player_score, "Computer:", computer_score)

        # Ask if the player wants to play again
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing!")


rock_paper_scissors()
