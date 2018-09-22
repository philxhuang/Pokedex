import math
import string
import copy

from tkinter import *
    
def runWindow(winWidth = 800, winHeight = 800):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    root["bg"] = "SlateGray1"
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()


'''
151 Pokemons
'''
