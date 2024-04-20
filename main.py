import tkinter as tk
from tkinter import PhotoImage
import pygame
import os
import sys


def play_audio():
    if pygame.mixer.get_busy():
        label.config(text="Don't spam it doofus")
        return
    audio_file = os.path.join(sys._MEIPASS, "heavySings.mp3")
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


# Initialize Pygame mixer
pygame.mixer.init()

# Create the main application window
root = tk.Tk()
root.title("Happy Birthday Nerd :P")
root.geometry("500x450")

# Create a text label
label = tk.Label(root, text="Happy Birthday")
label.pack()

# Load and display an image
image_file = os.path.join(sys._MEIPASS, "John-Bday.png")
original_image = PhotoImage(file=image_file)
image = original_image.subsample(5, 5)
image_label = tk.Label(root, image=image)
image_label.pack()

# Create a button to play audio
play_button = tk.Button(root, text="Someone wants to wish you a Happy Birthday :D", command=play_audio)
play_button.pack()

# Start the Tkinter event loop
root.mainloop()
