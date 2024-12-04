# import pygame
# #import your controller

# def main():
#     pygame.init()
#     #Create an instance on your controller object
#     #Call your mainloop
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == '__main__':
#     main()

import tkinter as tk
from src import controller


if __name__ == "__main__":
    root = tk.Tk()
    app = controller.Controller(root)
    root.mainloop()