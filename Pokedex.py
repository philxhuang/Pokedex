import math
import string
import copy

from tkinter import *
    
<<<<<<< HEAD
def runWindow(winWidth = 500, winHeight = 500):
=======
def runWindow(winWidth = 800, winHeight = 800):
>>>>>>> 93d8e70385b43c35023aa1ca12fb54c5713ce99e
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()
<<<<<<< HEAD
=======


'''
151 Pokemons
'''
>>>>>>> 93d8e70385b43c35023aa1ca12fb54c5713ce99e
