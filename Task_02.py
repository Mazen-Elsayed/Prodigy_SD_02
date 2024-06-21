import tkinter as tk
import random

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        feedbackLabel.config(text="Please enter a valid number")
        return
    attempts += 1
    if guess < number:
        if number - guess <= 5:
            feedbackLabel.config(text="A bit low! Try again.")
        else:
            feedbackLabel.config(text="Too low! Try again.")
    elif guess > number:
        if guess - number <= 5:
            feedbackLabel.config(text="A bit high! Try again.")
        else:
            feedbackLabel.config(text="Too high! Try again.")
    else:
        feedbackLabel.config(text=f"Correct! The number was {number}. It took you {attempts} attempts.")
        guessButton.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x150")

number = random.randint(1, 100)
attempts = 0

instructionLabel = tk.Label(root, text="Guess a number between 1 and 100:")
instructionLabel.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

guessButton = tk.Button(root, text="Submit Guess", command=check_guess)
guessButton.pack(pady=5)

feedbackLabel = tk.Label(root, text="")
feedbackLabel.pack(pady=10)

root.mainloop()
