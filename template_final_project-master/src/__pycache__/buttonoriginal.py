from tkinter import *
import threading


class Buttons():
    root = Tk()
    
    
    def start_recording_thread():
        threading.Thread(target=start_recording).start()

    def recordFirstPartClick(firstPartStatusLabel, firstPartStopButton, ):
        firstPartStatusLabel.config(text="Recording in progress")
        firstPartStopButton.config(fg="blue", state="normal")
        start_recording_thread

    def stopFirstPartClick(firstPartStatusLabel, secondPartRecordButton):
        firstPartStatusLabel.config(text="First Part recorded")
        secondPartRecordButton.config(fg="blue",state="normal")
        stop_recording 

    def recordSecondPartClick(secondPartStatusLabel, secondPartStopButton):
        secondPartStatusLabel.config(text="Recording in progress")
        secondPartStopButton.config(fg="blue", state="normal")

    def stopSecondPartClick(secondPartStatusLabel):
        secondPartStatusLabel.config(text="Second Part recorded")

    # set up our widgets
    def grid(firstPartLabel, secondPartLabel, firstPartRecordButton, secondPartRecordButton, firstPartStatusLabel,
             secondPartStatusLabel, firstPartStopButton, secondPartStopButton):
        # Position the widgets on the grid
        firstPartLabel.grid(row=2,column=0)
        secondPartLabel.grid(row=2,column=1)

        firstPartRecordButton.grid(row=3,column=0)
        secondPartRecordButton.grid(row=3,column=1)

        firstPartStatusLabel.grid(row=4,column=0)
        secondPartStatusLabel.grid(row=4,column=1)

        firstPartStopButton.grid(row=5,column=0)
        secondPartStopButton.grid(row=5,column=1)
    firstPartLabel = Label(root, text="Record First Part")
    secondPartLabel = Label(root, text="Record Second Part")

    firstPartRecordButton = Button(root, text="Record First",command=recordFirstPartClick, fg="blue")
    firstPartStopButton = Button(root, text="Stop First",command=stopFirstPartClick, fg="green", state="disabled")
    firstPartStatusLabel = Label(root, text="")

    secondPartRecordButton = Button(root, text="Record Second",command=recordSecondPartClick, fg="green", state="disabled")
    secondPartStopButton = Button(root, text="Stop Second",command=stopSecondPartClick, fg="green", state="disabled")
    secondPartStatusLabel = Label(root, text="")