import math
import string
import copy

from tkinter import *
from PIL import Image, ImageTk

#========================================================List
pokemonList = (
("#001", "Bulbasaur", ("Grass", "Poison")),
("#002", "Ivysaur", ("Grass", "Poison")),
("#003", "Venusaur", ("Grass", "Poison")),
("#004", "Charmander", ("Fire")),
("#005", "Charmeleon", ("Fire")),
("#006", "Charizard", ("Fire", "Flying")),
("#007", "Squirtle", ("Water")),
("#008", "Wartortle", ("Water")),
("#009", "Blastoise", ("Water")),
('#010', 'Caterpie', ('Bug')),
('#011', 'Metapod', ('Bug')),
('#012', 'Butterfree', ('Bug',	'Flying')),
('#013', 'Weedle', ('Bug', 'Poison')),
('#014', 'Kakuna', ('Bug', 'Poison')),
('#015', 'Beedrill', ('Bug', 'Poison')),
('#016', 'Pidgey', ('Normal', 'Flying')),
('#017', 'Pidgeotto', ('Normal', 'Flying')),
('#018', 'Pidgeot', ('Normal', 'Flying')),
('#019', 'Rattata', ('Normal')),
('#020', 'Raticate', ('Normal')),
('#021', 'Spearow', ('Normal', 'Flying')),
)


categoryList = (
('Seed Pokémon'),
('Seed Pokémon'),
('Seed Pokémon'),
('Lizard Pokémon'),
('Flame Pokémon'),
('Flame Pokémon'),
('Young Turtle \n Pokémon'),
('Turtle Pokémon'),
('Shell Pokémon'),
('Caterpillar Pokémon'), #10
('Chrysalis Pokémon'),
('Butterfly Pokémon'),
('Hairy Caterpillar \n Pokémon'),
('Cocoon Pokémon'),
('Poison Bee \n Pokémon'),
('Small Bird \n Pokémon'),
('Bird Pokémon'),
('Bird Pokémon'),
('Mouse Pokémon'),
('Mouse Pokémon'),#20
('Small Bird \n Pokémon'),
)

desList = (
('For some time after its birth, it grows by \n gaining nourishment from the seed on its back.'),
('When the bud on its back starts swelling, \n a sweet aroma wafts to indicate the flowers coming bloom.'),
('After a rainy day, the flower on its back \n smells stronger. The scent attracts other Pokémon.'), #3
('The fire on the tip of its tail is a measure \n of its life. If healthy, its tail burns intensely.'),
('In the rocky mountains where Charmeleon live, \n their fiery tails shine at night like stars.'),
('It is said that Charizards fire burns hotter \n if it has experienced harsh battles.'),
('It shelters itself in its shell then strikes \n back with spouts of water at every opportunity.'),
('It is said to live 10,000 years. Its furry \n tail is popular as a symbol of longevity.'),
('The jets of water it spouts from the rocket \n cannons on its shell can punch through thick steel.'),
('It releases a stench from its red antenna to \n repel enemies. It grows by molting repeatedly.'),#10
('A steel-hard shell protects its tender body. \n It quietly endures hardships while awaiting evolution.'),
('It loves the honey of flowers and can locate flower \n patches that have even tiny amounts of pollen.'),
('It eats its weight in leaves every day. \n It fends off attackers with the needle on its head.'),
('While awaiting evolution, it hides from \n predators under leaves and in nooks of branches.'),
('Its best attack involves flying around at high speed, \n striking with poison needles, then flying off.'),#15
('It is docile and prefers to avoid conflict. \n If disturbed, however, it can ferociously strike back.'),
('It flies over its wide territory in search of prey, \n downing it with its highly developed claws.'),
('It flies over its wide territory in search of prey, \n downing it with its highly developed claws.'),
('It searches for food all day. It gnaws on hard objects \n to wear down its fangs, which grow constantly during its lifetime.'),
('With its long fangs, this surprisingly violent Pokémon \n can gnaw away even thick concrete with ease.'),#20
('It flaps its small wings busily to fly. \n Using its beak, it searches in grass for prey.'),
)


def loadImages():
    global pokemonImages
    pokemonImages = []
    pokemonImages.append(PhotoImage(file = "bulbasaur.gif")) #1
    pokemonImages.append(PhotoImage(file = "ivysaur.gif"))
    pokemonImages.append(PhotoImage(file = "venusaur.gif"))
    pokemonImages.append(PhotoImage(file = "charmander.gif"))
    pokemonImages.append(PhotoImage(file = "charmeleon.gif")) #5
    pokemonImages.append(PhotoImage(file = "charizard.gif"))
    pokemonImages.append(PhotoImage(file = "squirtle.gif"))
    pokemonImages.append(PhotoImage(file = "wartortle.gif"))
    pokemonImages.append(PhotoImage(file = "blastoise.gif"))
    pokemonImages.append(PhotoImage(file = "caterpie.gif")) #10
    pokemonImages.append(PhotoImage(file = "metapod.gif"))
    pokemonImages.append(PhotoImage(file = "butterfree.gif"))
    pokemonImages.append(PhotoImage(file = "weedle.gif"))
    pokemonImages.append(PhotoImage(file = "kakuna.gif"))
    pokemonImages.append(PhotoImage(file = "beedrill.gif")) #15
    pokemonImages.append(PhotoImage(file = "pidgey.gif"))
    pokemonImages.append(PhotoImage(file = "pidgeotto.gif"))
    pokemonImages.append(PhotoImage(file = "pidgeot.gif"))
    pokemonImages.append(PhotoImage(file = "rattata.gif"))
    pokemonImages.append(PhotoImage(file = "raticate.gif")) #20
    pokemonImages.append(PhotoImage(file = "spearow.gif"))

#===============================================================
def runWindow(winWidth = 800, winHeight = 600):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    loadImages()

    scrollbar = Scrollbar(root, bd=0)
    Button(root, text = "EXTERMINATE ASAP", command=root.destroy).pack()
    pokelist = Listbox(root, yscrollcommand = scrollbar.set, selectmode=BROWSE)
    for i in pokemonList:
        pokelist.insert(END, i[0] + " " + i[1])
    scrollbar.config(command=pokelist.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    pokelist.pack(side=LEFT, fill=Y)

    root["bg"] = "SlateGray1"

#=================================================Aesthetics

    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack(side=RIGHT, fill=BOTH)
    
    canvas.create_rectangle(350, 50, 750, 550, fill = "CadetBlue1", outline = "turquoise1")
    canvas.create_rectangle(0, 0, 800, 600, fill = "#ccffcc", outline = "#DEB887") #color=lightgreen, outline=tan
    number = canvas.create_text(120, 35, font="Verdana 30 bold", text="#000")

    canvas.create_line(40, 60, 200, 60, width=4)
    canvas.create_line(300, 60, 700, 60, width=3)
    
    name = canvas.create_text(500, 35, font="Verdana 30 bold", text="Pokemon Name")

    category = canvas.create_text(130, 120, font="Verdana 14 bold", text='')

    canvas.create_text(60, 180, font="Verdana 12", text="Type")
    types = canvas.create_text(130, 180, font="Verdana 12", text="", anchor=W)
    
    canvas.create_text(70, 260, font="Verdana 12", text="Evolve\nLevel")
    canvas.create_text(70, 340, font="Verdana 12", text="Egg\nGroups")
    
    canvas.create_text(90, 530, font="Verdana 12", text="Pokedex\nDescription")
    des = canvas.create_text(430, 530, font="Verdana 12 italic", text='')
#================================================
    def displayinfo(event):
        current = pokelist.curselection()
        if len(current) > 0:
            nonlocal number
            nonlocal name
            nonlocal types
            canvas.delete(number)
            canvas.delete(name)
            canvas.delete(types)
            number = canvas.create_text(120, 35, font="Verdana 30 bold", text=pokemonList[current[0]][0])
            name = canvas.create_text(500, 35, font="Verdana 30 bold", text=pokemonList[current[0]][1])
            
            canvas.create_image(500, 120,anchor = N, image = pokemonImages[current[0]])
            
            typetext = ""
            if len(pokemonList[current[0]][2]) == 2:
                typetext = pokemonList[current[0]][2][0] + "/" + pokemonList[current[0]][2][1]
            else:
                typetext = pokemonList[current[0]][2]

            types = canvas.create_text(130, 180, font="Verdana 12", text=typetext, anchor=W)

            nonlocal category
            canvas.delete(category)
            category  = canvas.create_text(130, 120, font="Verdana 14 bold", text=categoryList[current[0]])
            
            nonlocal des
            canvas.delete(des)
            des = canvas.create_text(430, 530, font="Verdana 12 italic", text=desList[current[0]])
#================================================
    
    pokelist.bind("<<ListboxSelect>>", displayinfo)
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()
