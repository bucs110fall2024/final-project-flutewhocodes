from tkinter import *
import pyaudio
import pydub
from pydub import AudioSegment
import wave
from tkinter import filedialog
import os
import threading

root = Tk()
title = Label(root, text="Duets")  

def audio():
    # Load the two audio files
    # audio1 = AudioSegment.from_file("audio1.wav")
    # audio2 = AudioSegment.from_file("audio2.wav")
    audio1 = wave.open("audio1.wav", "wb")
    audio1.setnchannels(CHANNELS)
    audio1.setsamplewidth(pyaudio.get_sample_size(FORMAT))
    audio1.setframerate(RATE)
    audio1.writeframes(b"".join(frames))
    audio1.close()
    audio2 = wave.open("audio2.wav", "wb")
    audio2.setnchannels(CHANNELS)
    audio2.setsamplewidth(pyaudio.get_sample_size(FORMAT))
    audio2.setframerate(RATE)
    audio2.writeframes(b"".join(frames))
    audio2.close()
    # Combine the two audio files
    combined = audio1.overlay(audio2)

    # Export the combined audio file
    combined.export("combined_audio.wav", format="wav")

    print("The audio files have been combined and saved as 'combined_audio.wav'.")
    
# def select_file():
#     root.withdraw()  # Hide the root window
#     file_path = filedialog.askopenfilename()
#     print(f"Selected file: {file_path}")
# if __name__ == "__main__":
#     select_file()
    
# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = os.path.normpath("C:\\Users\\aeaus\\Documents\\output.wav")

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = None
frames = []
recording = False

# Function to start recording audio
def start_recording():
    global stream, frames, recording
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    frames = []
    recording = True
    print("Recording...")
    record_audio()

# Function to record audio
def record_audio():
    global recording
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)
        
# def setup_file():
#     obj = wave.open("output.wav", "wb")
#     obj.setnchannels(CHANNELS)
#     obj.setsamplewidth(pyaudio.get_sample_size(FORMAT))
#     obj.setframerate(RATE)
#     obj.writeframes(b"".join(frames))
#     obj.close()

# Function to stop recording audio
def stop_recording():
    global recording
    recording = False
    stream.stop_stream()
    stream.close()
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    print("Finished recording.")
    print(f"Audio saved to {OUTPUT_FILENAME}")

# Function to start recording in a separate thread
def start_recording_thread():
    threading.Thread(target=start_recording).start()

def recordFirstPartClick():
    firstPartStatusLabel.config(text="Recording in progress")
    firstPartStopButton.config(fg="blue", state="normal")
    start_recording_thread

def stopFirstPartClick():
    firstPartStatusLabel.config(text="First Part recorded")
    secondPartRecordButton.config(fg="blue",state="normal")
    stop_recording 

def recordSecondPartClick():
    secondPartStatusLabel.config(text="Recording in progress")
    secondPartStopButton.config(fg="blue", state="normal")

def stopSecondPartClick():
    secondPartStatusLabel.config(text="Second Part recorded")

# set up our widgets
firstPartLabel = Label(root, text="Record First Part")
secondPartLabel = Label(root, text="Record Second Part")

firstPartRecordButton = Button(root, text="Record First",command=recordFirstPartClick, fg="blue")
firstPartStopButton = Button(root, text="Stop First",command=stopFirstPartClick, fg="green", state="disabled")
firstPartStatusLabel = Label(root, text="")

secondPartRecordButton = Button(root, text="Record Second",command=recordSecondPartClick, fg="green", state="disabled")
secondPartStopButton = Button(root, text="Stop Second",command=stopSecondPartClick, fg="green", state="disabled")
secondPartStatusLabel = Label(root, text="")

# Position the widgets on the grid
firstPartLabel.grid(row=2,column=0)
secondPartLabel.grid(row=2,column=1)

firstPartRecordButton.grid(row=3,column=0)
secondPartRecordButton.grid(row=3,column=1)

firstPartStatusLabel.grid(row=4,column=0)
secondPartStatusLabel.grid(row=4,column=1)

firstPartStopButton.grid(row=5,column=0)
secondPartStopButton.grid(row=5,column=1)

root.mainloop()

audio.terminate()


