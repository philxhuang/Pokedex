import math
import string
import copy

from tkinter import *

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
('#022', 'Fearow', ('Normal', 'Flying')),
('#023', 'Ekans', ('Poison')),
('#024', 'Arbok', ('Poison')),
('#025', 'Pikachu', ('Electric')),
('#026', 'Raichu', ('Electric')),
('#027', 'Sandshrew', ('Ground')),
('#028', 'Sandslash', ('Ground')),
('#029', 'Nidoran (F)', ('Poison')),
('#030', 'Nidorina', ('Poison')),
('#031', 'Nidoqueen', ('Poison', 'Ground')),
('#032', 'Nidoran (M)', ('Poison')),
('#033', 'Nidorino', ('Poison')),
('#034', 'Nidoking', ('Poison', 'Ground')),
('#035', 'Clefairy', ('Fairy')),
('#036', 'Clefable', ('Fairy')),
('#037', 'Vulpix', ('Fire')),
('#038', 'Ninetails', ('Fire')),
('#039', 'Jigglypuff', ('Normal', 'Fairy')),
('#040', 'Wigglytuff', ('Normal', 'Fairy')),
('#041', 'Zubat', ('Poison', 'Flying')),
('#042', 'Golbat', ('Poison', 'Flying')),
('#043', 'Oddish', ('Grass', 'Poison')),
('#044', 'Gloom', ('Grass', 'Poison')),
('#045', 'Vileplume', ('Grass', 'Poison')),
('#046', 'Paras', ('Bug', 'Grass')),
('#047', 'Parasect', ('Bug', 'Grass')),
('#048', 'Venonat', ('Bug', 'Poison')),
('#049', 'Venomoth', ('Bug', 'Poison')),
('#050', 'Diglett', ('Ground')),
('#051', 'Dugtrio', ('Ground')),
('#052', 'Meowth', ('Normal')),
('#053', 'Persian', ('Normal')),
('#054', 'Psyduck', ('Water')),
('#055', 'Golduck', ('Water')),
('#056', 'Mankey', ('Fighting')),
('#057', 'Primeape', ('Fighting')),
('#058', 'Growlithe', ('Fire')),
('#059', 'Arcanine', ('Fire')),
('#060', 'Poliwag', ('Water')),
('#061', 'Poliwhirl', ('Water')),
('#062', 'Poliwrath', ('Water', 'Fighting')),
('#063', 'Abra', ('Psychic')),
('#064', 'Kadabra', ('Psychic')),
('#065', 'Alakazam', ('Psychic')),
('#066', 'Machop', ('Fighting')),
('#067', 'Machoke', ('Fighting')),
('#068', 'Machamp', ('Fightin')),
('#069', 'Bellsprout', ('Grass', 'Poison')),
('#070', 'Weepinbell', ('Grass', 'Poison')),
('#071', 'Victreebel', ('Grass', 'Poison')),
('#072', 'Tentacool', ('Water', 'Poison')),
('#073', 'Tentacruel', ('Water', 'Poison')),
('#074', 'Geodude', ('Rock', 'Ground')),
('#075', 'Graveler', ('Rock', 'Ground')),
('#076', 'Golem', ('Rock', 'Ground')),
('#077', 'Ponyta', ('Fire')),
('#078', 'Rapidash', ('Fire')),
('#079', 'Slowpoke', ('Water', 'Psychic')),
('#080', 'Slowbro', ('Water', 'Psychic')),
('#081', 'Magnemite', ('Electric', 'Steel')),
('#082', 'Magneton', ('Electric', 'Steel')),
('#083', 'Farfetch\'d', ('Normal', 'Flying')),
('#084', 'Doduo', ('Normal', 'Flying')),
('#085', 'Dodrio', ('Normal', 'Flying')),
('#086', 'Seel', ('Water')),
('#087', 'Dewgong', ('Water', 'Ice')),
('#088', 'Grimer', ('Poison')),
('#089', 'Muk', ('Poison')),
('#090', 'Shellder', ('Water')),
('#091', 'Cloyster', ('Water', 'Ice')),
('#092', 'Gastly', ('Ghost', 'Poison')),
('#093', 'Haunter', ('Ghost', 'Poison')),
('#094', 'Gengar', ('Ghost', 'Poison')),
('#095', 'Onix', ('Rock', 'Ground')),
('#096', 'Drowzee', ('Psychic')),
('#097', 'Hypno', ('Psychic')),
('#098', 'Krabby', ('Water')),
('#099', 'Kingler', ('Water')),
('#100', 'Voltorb', ('Electric')),
('#101', 'Electrode', ('Electric')),
('#102', 'Exeggcute', ('Grass', 'Psychic')),
('#103', 'Exeggutor', ('Grass', 'Psychic')),
('#104', 'Cubone', ('Ground')),
('#105', 'Marowak', ('Ground')),
('#106', 'Hitmonlee', ('Fighting')),
('#107', 'Hitmonchan', ('Fighting')),
('#108', 'Lickitung', ('Normal')),
('#109', 'Koffing', ('Poison')),
('#110', 'Weezing', ('Poison')),
('#111', 'Rhyhorn', ('Ground', 'Rock')),
('#112', 'Rhydon', ('Ground', 'Rock')),
('#113', 'Chansey', ('Normal')),
('#114', 'Tangela', ('Grass')),
('#115', 'Kangaskhan', ('Normal')),
('#116', 'Horsea', ('Water')),
('#117', 'Seadra', ('Water')),
('#118', 'Goldeen', ('Water')),
('#119', 'Seaking', ('Water')),
('#120', 'Staryu', ('Water')),
('#121', 'Starmie', ('Water', 'Psychic')),
('#122', 'Mr. Mime', ('Psychic', 'Fairy')),
('#123', 'Scyther', ('Bug', 'Flying')),
('#124', 'Jynx', ('Ice', 'Psychic')),
('#125', 'Electabuzz', ('Electric')),
('#126', 'Magmar', ('Fire')),
('#127', 'Pinsir', ('Bug')),
('#128', 'Tauros', ('Normal')),
('#129', 'Magikarp', ('Water')),
('#130', 'Gyarados', ('Water', 'Flying')),
('#131', 'Lapras', ('Water', 'Ice')),
('#132', 'Ditto', ('Normal')),
('#133', 'Eevee', ('Normal')),
('#134', 'Vaporeon', ('Water')),
('#135', 'Jolteon', ('Eletric')),
('#136', 'Flareon', ('Fire')),
('#137', 'Porygon', ('Normal')),
('#138', 'Omanyte', ('Rock', 'Water')),
('#139', 'Omastar', ('Rock', 'Water')),
('#140', 'Kabuto', ('Rock', 'Water')),
('#141', 'Kabutops', ('Rock', 'Water')),
('#142', 'Aerodactyl', ('Rock', 'Flying')),
('#143', 'Snorlax', ('Normal')),
('#144', 'Articuno', ('Ice', 'Flying')),
('#145', 'Zapdos', ('Electric', 'Flying')),
('#146', 'Moltres', ('Fire', 'Flying')),
('#147', 'Dratini', ('Dragon')),
('#148', 'Dragonair', ('Dragon')),
('#149', 'Dragonite', ('Dragonite', 'Flying')),
('#150', 'Mewtwo', ('Psychic')),
('#151', 'Mew', ('Psychic'))
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
('Pupa Pokémon'),
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
('It flaps its small wings busily to fly. \n Using its beak, it searches in grass for prey.'),
('It sneaks through grass without making a sound \n and strikes unsuspecting prey from behind.'),
('The pattern on its belly is for intimidation. \n It constricts foes while they are frozen in fear.'),
('It occasionally uses an electric shock to recharge \n a fellow Pikachu that is in a weakened state.'), #25
('Its tail discharges electricity into the ground, \n protecting it from getting shocked.'),
('It digs deep burrows to live in. When in danger, \n it rolls up its body to withstand attacks.'),
('The spikes on its body are made up of its hardened hide. \n It rolls up and attacks foes with its spikes.'),
('While it does not prefer to fight, even one drop of \n the poison it secretes from barbs can be fatal.'),
('When it senses danger, it raises all the barbs on its body. \n These barbs grow slower than Nidorinos.'),#30
('Its entire body is armored with hard scales. n\ It will protect the young in its burrow with its life.'),
('It scans its surroundings by raising its ears out \n of the grass. Its toxic horn is for protection.'),
('It has a violent disposition and stabs foes \n with its horn, which oozes poison upon impact.'),
('One swing of its mighty tail can snap a \n telephone pole as if it were a matchstick.'),
('On nights with a full moon, Clefairy gather \n from all over and dance. Bathing in moonlight makes them float.'),#35
('Their ears are sensitive enough to hear a pin \n drop from over a mile away, so theyre usually found in quiet places.'),
('As each tail grows, its fur becomes more lustrous. \n When held, it feels slightly warm.'),
('Each of its nine tails is imbued with supernatural power, \n and it can live for a thousand years.'),
('Looking into its cute, round eyes makes it start singing \n a song so pleasant listeners cant help but fall asleep.'),
('Its fine fur feels so pleasant, those who accidentally \n touch it cannot take their hands away.'),#40
('It does not need eyes, because it emits ultrasonic \n waves to check its surroundings while it flies.'),
('Flitting around in the dead of night, it sinks its fangs \n into its prey and drains a nearly fatal amount of blood.'),
('It often plants its root feet in the ground during the day \n and sows seeds as it walks about at night.'),
('The honey it drools from its mouth smells so atrocious, \n it can curl noses more than a mile away.'),
('Its petals are the largest in the world. As it walks, \n it scatters extremely allergenic pollen.'),#45
('Mushrooms named tochukaso grow on its back. \n They grow along with the host Paras.'),
('A mushroom grown larger than the hosts body controls Parasect. \n It scatters poisonous spores.'),
('Its big eyes are actually clusters of tiny eyes. \n At night, its kind is drawn by light.'),
('It flutters its wings to scatter dustlike scales. \n The scales leach toxins if they contact skin'),
('A Pokémon that lives underground. Because of its dark habitat, \n it is repelled by bright sunlight.'),#50
('Its three heads move alternately, driving it through \n tough soil to depths of over 60 miles.'),
('It is nocturnal in nature. If it spots something \n shiny, its eyes glitter brightly.'),
('A very haughty Pokémon. Among fans, the size of \n the jewel in its forehead is a topic of much talk.'),
('When headaches stimulate its brain cells, which are \n usually inactive, it can use a mysterious power.'),
('When its forehead shines mysteriously, \n Golduck can use the full extent of its power.'),#55
('It lives in treetop colonies. If one becomes enraged, \n the whole colony rampages for no reason.'),
('It grows angry if you see its eyes and gets angrier \n if you run. If you beat it, it gets even madder.'),
('Extremely loyal to its Trainer, it will bark at those \n who approach the Trainer unexpectedly and run them out of town.'),
('The sight of it running over 6,200 miles in a single \n day and night has captivated many people.'),
('Its skin is so thin, its internal organs are visible. \n It has trouble walking on its newly grown feet.'),#60
('The spiral pattern on its belly subtly undulates. \n Staring at it gradually causes drowsiness.'),
('With its extremely tough muscles, it can keep \n swimming in the Pacific Ocean without resting.'),
('Using its psychic power is such a strain on its \n brain that it needs to sleep for 18 hours a day.'),
('It stares at its silver spoon to focus its mind. \n It emits more alpha waves while doing so.'),
('The spoons clutched in its hands are said to \n have been created by its psychic powers.'),#65
('Though small in stature, it is powerful enough to \n easily heft and throw a number of Geodude at once.'),
('It happily carries heavy cargo to toughen up. \n It willingly does hard work for people.'),
('Its four muscled arms slam foes with powerful \n punches and chops at blinding speed.'),
('It prefers hot and humid environments. \n It is quick at capturing prey with its vines.'),
('A Pokémon that appears to be a plant. It captures \n unwary prey by dousing them with a toxic powder.'),#70
('It pools in its mouth a fluid with a honey-like scent, \n which is really an acid that dissolves anything.'),
('Because its body is almost entirely composed of water, \n it shrivels up if it is washed ashore.'),
('It extends its 80 tentacles to form an encircling \n poisonous net that is difficult to escape.'),
('At rest, it looks just like a rock. Carelessly stepping \n on it will make it swing its fists angrily.'),
('It rolls on mountain paths to move. Once it builds momentum, \n no Pokémon can stop it without difficulty.'),#75
('Even dynamite cant harm its hard, boulder-like body. \n It sheds its hide just once a year.'),
('As a newborn, it can barely stand. However, \n through galloping, its legs are made tougher and faster.'),
('When at an all-out gallop, its blazing mane sparkles, \n enhancing its beautiful appearance.'),
('Although slow, it is skilled at fishing with its tail. \n It does not feel pain if its tail is bitten.'),
('Though usually dim witted, it seems to become inspired \n if the Shellder on its tail bites down.'),#80
('The electromagnetic waves emitted by the units at the \n sides of its head expel antigravity, which allows it to float.'),
('The stronger electromagnetic waves from the three linked \n Magnemite are enough to dry out surrounding moisture.'),
('It cant live without the stalk it holds. Thats why it \n defends the stalk from attackers with its life.'),
('The brains in its two heads appear to communicate \n emotions to each other with a telepathic power.'),
('When Doduo evolves into this odd breed, one of \n its heads splits into two. It runs at nearly 40 mph.'),#85
('The colder it gets, the better it feels. It joyfully \n swims around oceans so cold that they are filled with floating ice.'),
('Its streamlined body has low resistance, and it swims \n around cold oceans at a speed of eight knots.'),
('Born from sludge, these Pokémon now gather in polluted \n places and increase the bacteria in their bodies.'),
('Its so stinky! Muks body contains toxic elements, \n and any plant will wilt when it passes by.'),
('It swims backward by opening and closing its two shells. \n Its large tongue is always kept hanging out.'),#90
('It fights by keeping its shell tightly shut for \n protection and by shooting spikes to repel foes.'),
('Born from gases, anyone would faint if engulfed \n by its gaseous body, which contains poison.'),
('It likes to lurk in the dark and tap shoulders \n with a gaseous hand. Its touch causes endless shuddering.'),
('The leer that floats in darkness belongs to a \n Gengar delighting in casting curses on people.'),
('Opening its large mouth, it ingests massive \n amounts of soil and creates long tunnels.'),#95
('It can tell what people are dreaming by sniffing \n with its big nose. It loves fun dreams.'),
('Seeing its swinging pendulum can induce sleep in \n three seconds, even in someone who just woke up.'),
('It lives in burrows dug on sandy beaches. Its pincers \n fully grow back if they are broken in battle.'),
('The larger pincer has 10,000- horsepower strength. \n However, it is so heavy, it is difficult to aim.'),
('It looks just like a Pok Ball. It is dangerous \n because it may electrocute or explode on contact.'),#100
('It is known to drift on winds if it is bloated \n to bursting with stored electricity.'),
('Its six eggs converse using telepathy. \n They can quickly gather if they become separated.'),
('It is called The Walking Jungle. If a head grows too big, \n it falls off and becomes an Exeggcute.'),
('When it thinks of its dead mother, it cries. \n Its crying makes the skull it wears rattle hollowly.'),
('From its birth, this savage Pokémon constantly holds bones. It is skilled in using them as weapons.'),#105
('Its legs can stretch double. First-time \n foes are startled by its extensible reach.'),
('The arm-twisting punches it throws pulverize even concrete. \n It rests after three minutes of fighting.'),
('Being licked by its long, saliva-covered tongue leaves a \n tingling sensation. Extending its tongue retracts its tail.'),
('Toxic gas is held within its thin, balloon-shaped body, \n so it can cause massive explosions.'),
('Inhaling toxic fumes from trash and mixing them \n inside its body lets it spread an even fouler stench.'),#110
('Its powerful tackles can destroy anything. \n However, it is too slow witted to help people work.'),
('Standing on its hind legs freed its forelegs \n and made it smarter. It is very forgetful, however.'),
('A kindly Pokémon that lays highly nutritious eggs \n and shares them with injured Pokmon or people.'),
('Many writhing vines cover it, so its true identity \n remains unknown. The blue vines grow its whole life long.'),
('It raises its offspring in its belly pouch. \n It lets the baby out to play only when it feels safe.'),#115
('It makes its nest in the shade of corals. \n If it senses danger, it spits murky ink and flees.'),
('Its spines provide protection. Its fins and \n bones are prized as traditional-medicine ingredients.'),
('Though it appears very elegant when swimming with \n fins unfurled, it can jab powerfully with its horn.'),
('In autumn, its body becomes more fatty in preparing \n to propose to a mate. It takes on beautiful colors.'),
('As long as its red core remains, it can regenerate \n its body instantly, even if its torn apart.'),#120
('Its core shines in many colors and sends radio \n signals into space to communicate with something.'),
('It shapes an invisible wall in midair by minutely \n vibrating its fingertips to stop molecules in the air.'),
('The sharp scythes on its forearms become \n increasingly sharp by cutting through hard objects.'),
('Its cries sound like human speech. However, \n it is impossible to tell what it is trying to say.'),
('Research is progressing on storing lightning \n in Electabuzz so this energy can be used at any time.'),#125
('The scorching fire exhaled by Magmar forms heat \n waves around its body, making it hard to see the Pokémon clearly.'),
('It grips prey with its powerful pincers and will \n not let go until the prey is torn in half.'),
('Once it takes aim at its foe, it makes a headlong \n charge. It is famous for its violent nature.'),
('A Magikarp living for many years can leap \n a mountain using Splash. The move remains useless, though.'),
('Once it begins to rampage, a Gyarados will burn \n everything down, even in a harsh storm.'),#130
('Able to understand human speech and very intelligent, \n it loves to swim in the sea with people on its back.'),
('It can reconstitute its entire cellular structure \n to change into what it sees, but it returns to normal when it relaxes.'),
('Thanks to its unstable genetic makeup, this special Pokémon \n conceals many different possible evolutions.'),
('Its cell composition is similar to water molecules. \n As a result, it cant be seen when it melts away into water.'),
('By storing electricity in its body, it can shoot its \n bristlelike fur like a barrage of missiles.'),#135
('Inhaled air is carried to its flame sac, heated, \n and exhaled as fire that reaches over 3,000 degrees F.'),
('A man-made Pokémon created using advanced scientific means. \n It can move freely in cyberspace.'),
('A Pokémon that was resurrected from a fossil using modern science. \n It swam in ancient seas.'),
('It is thought that this Pokémon became extinct \n because its spiral shell grew too large.'),
('It is thought to have inhabited beaches 300 million \n years ago. It is protected by a stiff shell.'),#140
('It is thought that this Pokémon came onto land \n because its prey adapted to life on land.'),
('A Pokémon that roamed the skies in the dinosaur era. \n Its teeth are like saw blades.'),
('When its belly is full, it becomes too lethargic to \n even lift a finger, so it is safe to bounce on its belly.'),
('A legendary bird Pokémon. It can create \n blizzards by freezing moisture in the air.'),
('A legendary Pokémon that is said to live in thunderclouds. \n It freely controls lightning bolts.'),#145
('One of the legendary bird Pokémon. It is said \n that its appearance indicates the coming of spring.'),
('It is called the Mirage Pokémon because so \n few have seen it. Its shed skin has been found.'),
('If its body takes on an aura, the weather changes instantly. \n It is said to live in seas and lakes.'),
('It is said to make its home somewhere in the sea. \n It guides crews of shipwrecks to shore.'),
('A Pokémon created by recombining Mews genes. \n Its said to have the most savage heart among Pokmon.'),#150
('So rare that it is still said to be a mirage by many experts. \n Only a few people have seen it worldwide.'),
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
