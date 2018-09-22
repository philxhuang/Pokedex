import math
import string
import copy

from tkinter import *
    
def runWindow(winWidth = 800, winHeight = 600):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    root["bg"] = "SlateGray1"
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    
    canvas.create_rectangle(350, 50, 750, 550, fill = "CadetBlue1", outline = "turquoise1")
    
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()


'''
#001	Bulbasaur Grass	Poison
#002	Ivysaur Grass	Poison
#003	#003	Venusaur Grass	Poison
#004	#004	Charmander Fire
#005	#005	Charmeleon Fire
#006	#006	Charizard Fire	Flying
#007	#007	Squirtle Water
#008	#008	Wartortle Water
#009	#009	Blastoise Water
#010	#010	Caterpie Bug
#011	#011	Metapod	 Bug
#012	#012	Butterfree Bug	Flying
#013	#013	Weedle Bug	Poison
#014	#014	Kakuna Bug	Poison
#015	#015	Beedrill Bug	Poison
#016	#016	Pidgey Normal	Flying
#017	#017	Pidgeotto Normal	Flying
#018	#018	Pidgeot Normal	Flying
#019	#019	Rattata Normal
#020	#020	Raticate Normal
#021	#021	Spearow Normal	Flying
'''
