import math
import string
import copy

from tkinter import *
    
def runWindow(winWidth = 800, winHeight = 800):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    scrollbar = Scrollbar(root, bd=0)
    pokelist = Listbox(root, yscrollcommand = scrollbar.set, selectmode=BROWSE)
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    pokelist.insert(END, "001", "Bulbasaur")
    scrollbar.config(command=pokelist.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    pokelist.pack(side=LEFT, fill=Y)
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack(side=RIGHT, fill=BOTH)
     
    
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()


'''
151 Pokemons
'''
