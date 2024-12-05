import threading
from src import audio
from src import buttons
from tkinter import filedialog
from tkinter import *


class Controller:
    def __init__(self, root):
        """
        initializes audio and buttons
        args: root
        """
        self.audio = audio.Audio()
        self.view = buttons.Buttons(root, self)

    def select_file(self):
        """
        allows user to select a wav file
        args: none
        return: none
        """
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file_path:
            selected_file_path = self.audio.select_file(file_path)
            print(f"Selected file: {selected_file_path}")

    def start_recording1(self):
        """
        threads first audio recording
        when the first record button is hit, text displays
        "Recording in progress"
        args: none
        return: none
        """
        print("Recording started...")
        recording_label = Label(text="")
        recording_label.config(text="Recording in progress")
        recording_label.grid(row=5,column=0)
        threading.Thread(target=self.audio.start_recording1).start()
        
    def stop_recording1(self):
        """
        calls stop recording function from Audio class
        ends the first recording
        adds label "Recording stopped" 
        args: none
        return: none
        """
        print("Recording stopped.")
        recording_stop_label = Label(text="")
        recording_stop_label.config(text="Recording stopped")
        recording_stop_label.grid(row=6,column=0)
        self.audio.stop_recording1()
        
    def start_recording2(self):
        """
        threads second audio recording
        when the second record button is hit, text displays
        "Recording in progress"
        args: none
        return: none
        """
        print("Recording started...")
        recording_label = Label(text="")
        recording_label.config(text="Recording in progress")
        recording_label.grid(row=5,column=1)
        threading.Thread(target=self.audio.start_recording2).start()
        
    def stop_recording2(self):
        """
        calls stop recording function from Audio class
        ends the second recording
        adds label "Recording stopped" 
        args: none
        return: none
        """
        print("Recording stopped.")
        recording_stop_label = Label(text="")
        recording_stop_label.config(text="Recording stopped")
        recording_stop_label.grid(row=6,column=1)
        self.audio.stop_recording2()
        
    # def save_first(self):
    #     first_record_file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
    #     self.audio.set_output_file(first_record_file_path)
        
    def save_overlay(self):
        """
        combines recorded audio with a selected audio file
        args: none
        return: none
        """
        output_file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
        if output_file_path:
            self.audio.set_output_file(output_file_path)
            combined_file_path = self.audio.overlay_audio()
            if combined_file_path:
                print(f"Combined audio saved to: {combined_file_path}")
            else:
                print("Failed to overlay audio.")
                
    def game_info(self):
        """
        adds instructions on how to use the function
        args: none
        return: none
        """
        self.msg = """
        This program lets you record and overlay 2 audio tracks.
        
        To begin, select 'Record First', then 'Stop Recording' when you 
        are done recording your audio. This recording will be saved as 
        'recorded_audio1.wav' in this project's folder.
        
        To overlay your first recording, press 'Select Backing Track' and open your first recording
        ('recorded_audio1.wav')
        
        To record your second audio track, press 'Record Second' and 'Stop Recording'
        when you are done.
        
        To combine both recordings, press 'Save' to save your combined audio file.
        """
        input(self.msg)