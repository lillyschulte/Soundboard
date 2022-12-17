import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame
pygame.init()

# Create the main window
window = tk.Tk()
window.title("Audio Player")

# Create a label to display the current audio file
label = tk.Label(window, text="No file selected")
label.pack()

def play_audio(file_path):
    # Load the specified audio file
    pygame.mixer.music.load(file_path)
    # Play the audio file
    pygame.mixer.music.play()

def create_play_button(file_path):
    # Create a button to play the audio file
    button = tk.Button(window, text=file_path, command=lambda: play_audio(file_path))
    button.pack()

def stop_audio():
    # Fade out the audio over 1000 milliseconds (1 second)
    pygame.mixer.music.fadeout(1000)

def browse_audio():
    # Open a file dialog to select multiple audio files
    file_paths = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3;*.wav")])
    # Update the label with the selected file names
    label.config(text=", ".join(file_paths))
    # Create a button for each selected audio file
    for file_path in file_paths:
        create_play_button(file_path)

browse_button = tk.Button(window, text="Browse", command=browse_audio)
browse_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_audio)
stop_button.pack()

# Run the main loop
window.mainloop()
