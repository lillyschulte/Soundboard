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

# Create a button to browse for audio files
def browse_audio():
    # Open a file dialog to select an audio file
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
    # Update the label with the selected file name
    label.config(text=file_path)

browse_button = tk.Button(window, text="Browse", command=browse_audio)
browse_button.pack()

# Create a button to play the selected audio file
def play_audio():
    # Load the selected audio file
    pygame.mixer.music.load(label.cget("text"))
    # Play the audio file
    pygame.mixer.music.play()

play_button = tk.Button(window, text="Play", command=play_audio)
play_button.pack()

def stop_audio():
    # Fade out the audio over 1000 milliseconds (1 second)
    pygame.mixer.music.fadeout(1000)

stop_button = tk.Button(window, text="Stop", command=stop_audio)
stop_button.pack()


# Run the main loop
window.mainloop()
