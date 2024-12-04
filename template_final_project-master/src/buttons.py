import tkinter as tk
from tkinter import *


class Buttons:
    def __init__(self, root, controller):
        """
        initializes the title and buttons on the GUI
        
        There are buttons to record and stop recording
        the first and second recordings, select the 
        backing track, save the combined audio file, 
        and provide instructions on how to use the program
        
        args: root, controller
        """
        
        self.controller = controller
        self.root = root

        title_label = Label(self.root, text="Duet Recording")
        title_label.grid(row=0)

        self.select_button = tk.Button(root, text="Select Backing Track", command=self.controller.select_file)
        self.select_button.grid(row=1,column=0)

        self.record_button = tk.Button(root, text="Record First", command=self.controller.start_recording1)
        self.record_button.grid(row=2,column=0)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.controller.stop_recording1)
        self.stop_button.grid(row=3,column=0)

        # self.overlay_button = tk.Button(root, text="Save", command=self.controller.save_first)
        # self.overlay_button.grid(row=4,column=0)
        
        self.record_button = tk.Button(root, text="Record Second", command=self.controller.start_recording2)
        self.record_button.grid(row=2,column=1)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.controller.stop_recording2)
        self.stop_button.grid(row=3,column=1)

        self.overlay_button = tk.Button(root, text="Save", command=self.controller.save_overlay)
        self.overlay_button.grid(row=4,column=1)
        
        self.info_button = tk.Button(root, text="Need help?", command = self.controller.game_info)
        self.info_button.grid(row=0,column=3)