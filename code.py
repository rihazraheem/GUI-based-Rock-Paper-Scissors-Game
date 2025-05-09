#import libraries

import tkinter as tk
from PIL import Image, ImageTk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Window size and position
width, height = 400, 500
x = root.winfo_screenwidth() // 2 - width // 2
y = root.winfo_screenheight() // 2 - height // 2
root.geometry(f"{width}x{height}+{x}+{y}")
root.configure(bg="white")
root.resizable(False, False)

# Load and resize images
def load_image(filename):
    img = Image.open(filename).resize((100, 100), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

# Keep image references globally
img_rock = load_image("rock.png")
img_paper = load_image("paper.png")
img_scissors = load_image("scissor.png")

# Image dictionary
images = {1: img_rock, 2: img_paper, 3: img_scissors}
names = {1: "Rock", 2: "Paper", 3: "Scissors"}

# Display computer choice
comp_label = tk.Label(root, text="Computer's Choice:", font=("Arial", 14), bg="white")
comp_label.pack(pady=10)

comp_img_label = tk.Label(root, bg="white")
comp_img_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="blue")
result_label.pack(pady=20)

# Game logic
def play(user_choice):
    computer_choice = random.randint(1, 3)
    comp_img_label.config(image=images[computer_choice])
    comp_img_label.image = images[computer_choice]  # Keep reference

    user = names[user_choice]
    computer = names[computer_choice]

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        result = f"You chose {user}, Computer chose {computer}\nYou win!"
    else:
        result = f"You chose {user}, Computer chose {computer}\nComputer wins!"

    result_label.config(text=result)

# Buttons
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, image=img_rock, command=lambda: play(1))
rock_btn.grid(row=0, column=0, padx=10)
rock_btn.image = img_rock  # Prevent GC

paper_btn = tk.Button(btn_frame, image=img_paper, command=lambda: play(2))
paper_btn.grid(row=0, column=1, padx=10)
paper_btn.image = img_paper

scissors_btn = tk.Button(btn_frame, image=img_scissors, command=lambda: play(3))
scissors_btn.grid(row=0, column=2, padx=10)
scissors_btn.image = img_scissors

# Exit button
exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_btn.pack(pady=20)

root.mainloop()

