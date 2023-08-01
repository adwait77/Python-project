import tkinter as tk
from tkinter import messagebox
import pygame
import sys

def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to quit?"):
        pygame.quit()
        sys.exit()

root = tk.Tk()
root.title("Game Options")
root.configure(bg="black")  

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        pygame.quit()
        sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text="Select a game to play:", font=("Arial bold", 20), fg="white", bg="black")  
label.pack(pady=20)

def play_tic_tac_toe():
    from tic_tac_toe import play_tic_tac_toe
    play_tic_tac_toe()

tic_tac_toe_button = tk.Button(root, text="Tic-Tac-Toe", font=("Arial bold", 16), command=play_tic_tac_toe, bg="blue", fg="white")
tic_tac_toe_button.pack(pady=10)

def play_snakegame():
    from snake import play_snakegame
    play_snakegame()

snake_button = tk.Button(root, text="Snake Game", font=("Arial bold", 16), command=play_snakegame, bg="green", fg="white")
snake_button.pack(pady=10)

def play_hangman():
    from hangman import play_hangman
    play_hangman()

hangman_button = tk.Button(root, text="Hangman", font=("Arial bold", 16), command=play_hangman, bg="pink", fg="white")
hangman_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial bold", 16), command=exit_program, bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()
