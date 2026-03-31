import tkinter as tk
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == "Rock" and computer_choice == "Scissors") or \
       (player_choice == "Paper" and computer_choice == "Rock") or \
       (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create the buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", width=20, command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=20, command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="Make your choice!")
result_label.pack(pady=20)

root.mainloop()