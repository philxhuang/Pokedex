import math
import string
import copy

from tkinter import *

pokemonList = (
("#001", "Bulbasaur", ("Grass", "Poison")),
("#002", "Ivysaur", ("Grass", "Poison")),
("#003", "Venusaur", ("Grass", "Poison")),
("#004", "Charmander", ("Fire")),
("#005", "Charmeleon", ("Fire")),
("#006", "Charizarad", ("Fire", "Flying")),
("#007", "Squirtle", ("Water")),
("#008", "Wartotle", ("Water")),
("#009", "Blastoise", ("Water"))
)

def runWindow(winWidth = 800, winHeight = 600):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    scrollbar = Scrollbar(root, bd=0)
    pokelist = Listbox(root, yscrollcommand = scrollbar.set, selectmode=BROWSE)
    for i in pokemonList:
        pokelist.insert(END, i[0] + " " + i[1])
    scrollbar.config(command=pokelist.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    pokelist.pack(side=LEFT, fill=Y)

    root["bg"] = "SlateGray1"

    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack(side=RIGHT, fill=BOTH)
    
    canvas.create_rectangle(350, 50, 750, 550, fill = "CadetBlue1", outline = "turquoise1")
    canvas.create_rectangle(0, 0, 800, 600, fill = "#ccffcc", outline = "#DEB887") #color=lightgreen, outline=tan
    canvas.create_text(120, 40, font="Verdana 24 bold", text=pokemonList[0][0])
    canvas.create_text(500, 40, font="Verdana 24 bold", text=pokemonList[0][1])
    canvas.create_line(40, 60, 200, 60, width=4)
    canvas.create_line(300, 60, 700, 60, width=3)
    
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()


'''
151 Pokemons
=======
#001 Bulbasaur Grass	Poison
#002 Ivysaur Grass	Poison
#003 Venusaur Grass	Poison
#004 Charmander Fire
#005 Charmeleon Fire
#006 Charizard Fire	Flying
#007 Squirtle Water
#008 Wartortle Water
#009 Blastoise Water
#010 Caterpie Bug
#011 Metapod Bug
#012 Butterfree Bug	Flying
#013 Weedle Bug	Poison
#014 Kakuna Bug	Poison
#015 Beedrill Bug Poison
#016 Pidgey Normal Flying
#017 Pidgeotto Normal Flying
#018 Pidgeot Normal	Flying
#019 Rattata Normal
#020 Raticate Normal
#021 Spearow Normal	Flying
'''
