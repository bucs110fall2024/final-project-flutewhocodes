
class Controller:
  
  def __init__(self):
    #setup pygame data
    """
    display screen and menu.
    waits for the user to press a button to start the tuner
    """
  def mainloop(self):
    #select state loop
    while True:
      if self.state == "menu":
        self.menuloop()
        #print(self.state)
      elif self.state == "tuner":
        self.tuneloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      
  def tuneloop(self):
    """
    keeps displaying frequency on screen and
    message that says whether the sound is in tune or not,
    until the user ends the program
    """
      #event loop

      #update data

      #redraw
    
  # def gameoverloop(self):
      #event loop

      #update data

      #redraw
