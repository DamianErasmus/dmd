#INDEX
#--------------------------------------------
# 1) Imports
# 2) Rooms

from sys import exit
from textwrap import dedent
from random import randint
from battle_stuff import *
from bosses import *
import webbrowser



#  Rooms:
#---------------------------------------------------

# Base object class of Room
# Each room is but an object that runs different functions, so doesn't need configuration yet
class Room(object):
    
    def enter(self):
        print("Not yet configured, implement later")
        exit(1)

# Sorting Room is the first room players enter, used to determine the human and ghosts
# Call the battle function using the player names
class SortingRoom(Room):
    
    def enter(self):
        webbrowser.open('https://www.youtube.com/watch?v=mIrt5MkGpy0&ab_channel=AdrianvonZiegler', new=0)
        player_names = players.get_names()
        input("<Enter>\n")
        # THIS IS THE INTRO FOR THE ROOM
        #--------------------------------------
        print("READ THIS:")
        input("<Enter>\n")

        for names in player_names:
            print(names),   
        
        print (dedent("""
            You wake up in a moist cave. 
            All you can remember is 
            you did a ritual to obtain power, 
            you became powerful, 
            you blacked out. 

            ...

            When you awoke 
            you saw something/one precious to you
            ...
            completely destroyed 
            ...
            and you went on a drinking binge...

            As you look around, what you should be seeing are totally ordinary human beings, like anyone you would just pass by on the street...

            However, 
            as things are currently, 
            you see beings that have lived for way too long, 
            and it is about time someone does something about it.

            ...

            Also... You feel strong, REALLY strong. 

            But of course you do! 
            I mean, how else are you to teach these wastes of space-s a proper lesson?
        """))
        input("<Enter>\n")
        print("Tell the players that they want nothing more than to kill each other")
        input("<Enter>\n")
        print("Players roll iniative")
        input("<Enter>\n")

        fighters = []
        for names in player_names:
            fighters.append(names)

        battle(fighters)
        players.humanity_check(player_names)  

# Monster Room is the room where the ghosts are monsters
# Will use the Human's first action to determine whether the ghosts have a surprise round or not
# Then call the battle function using the human and the monster names
class MonsterRoom(Room):
    
    def enter(self):
        webbrowser.open('https://www.youtube.com/watch?v=OKlEcZ_2dsI&ab_channel=MichaelGhelfi-RPGAmbiences%26Music', new=0)
        ghosts = players.get_ghosts()
        player_names = players.get_names()
        human = players.get_human()

        print (human)

        print("Monster Room")
        input("<Enter>\n")

        print (dedent("""
            You enter a room, but from where again? 
            Around you you hear the dishearting sounds of 
            something creeping out the shadows of the room... 
            At the far end of the room you see a door...
        """))

        door = False
        monsters = True
        options = ["Nothing", "Run Away", "Fighto", "Use door"]
        choice = ""

        print("The human can:")

        while door == False:
            selection = 0
            print("Just type the number of the option")
            #options are different if monsters are dead
            if not monsters:

                while True:
                    try:
                        count = 0
                        for option in options:                            
                            if option == "Fighto":
                                pass
                            else:
                                count = count+1
                                print("%i) %s" % (count, option))

                        selection = int(input())
                        
                        if selection not in (1,2,3):
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("You made a mistake, here are your ONLY options")
                
                if selection == 1:
                    choice = "Nothing"
                elif selection == 2:
                    choice = "Run Away"
                elif selection == 3:
                    print("The door squeaks... and opens.")
                    door = True
                    break

                if choice == "Nothing":
                    print("Wow! How inovative of you. You just did fokol")
                elif choice == "Run Away":
                    print("HAHAHAHA!!! YES!!! RUN!!!")
                elif choice == "Use door":
                    print("The door creeeeeeeeaks... and opens")
                else:
                    print("I don't believe you can do that.")
                input()
            else:
                while True:
                    try:
                        for option in options:
                            place = options.index(option) + 1
                            print("%i) %s" % (place, option))
                        
                        selection = int(input())
                        
                        if selection not in (1,2,3,4):
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("You made a mistake, here are your ONLY options")
            
                if selection == 1:
                    choice = "Nothing"
                elif selection == 2:
                    choice = "Run Away"
                elif selection == 3:
                    choice = "Fighto"
                elif selection == 4:
                    choice = "Use door"

                if choice == "Fighto":
                    print("Okay, so beasts start appearing from the shadows, no surprises there.")
                else:
                    if choice == "Nothing":
                        print("Wow! How inovative of you. You just did fokol")
                    elif choice == "Run Away":
                        print("HAHAHAHA!!! YES!!! RUN!!!")
                    elif choice == "Use door":
                        print("The door seems to have a faint red glow. How to open it is beyond you.")
                    else:
                        print("I don't believe you can do that.")
                    input()
                    print("Also, it seems you are surrounded by beasts.")
                    print("All ghosts have a free turn with advantage."            )
                    input()
                
                print("Oh yeah, the beasts.")
                input("<Enter>\n")
                num_of_ghosts = len(ghosts)

                fighters = []
                fighters.append(human)
                

                if num_of_ghosts == 1:
                    print("The ghost can choose 6 monsters")
                    input("<Enter>\n")
                    for x in range(6):
                        while True:
                            try: 
                                print("Please type %s's monster #%i" % ((ghosts[0]), x+1))
                                monster = input()
                                if not monster:
                                    raise ValueError
                                fighters.append(monster)
                                break
                            except ValueError as e:
                                print("Type in the NAME OF THE MONSTER, not fokol... poes")
                        
                elif num_of_ghosts == 2:
                    print("Each ghost can choose 3 monsters")
                    input("<Enter>\n")
                    for x in range(2):
                        for y in range(3):
                            while True:
                                try: 
                                    print("Please type %s's monster #%i" % ((ghosts[x]), y+1))
                                    monster = input()
                                    if not monster:
                                        raise ValueError
                                    fighters.append(monster)
                                    break
                                except ValueError as e:
                                    print("Type in the NAME OF THE MONSTER, not fokol... poes")
                elif num_of_ghosts == 3:
                    print("Each ghost can choose 2 monsters")
                    for x in range(3):
                        for y in range(2):
                            while True:
                                try: 
                                    print("Please type %s's monster #%i" % ((ghosts[x]), y+1))
                                    monster = input()
                                    if not monster:
                                        raise ValueError
                                    fighters.append(monster)
                                    break
                                except ValueError as e:
                                    print("Type in the NAME OF THE MONSTER, not fokol... poes")
                elif num_of_ghosts == 4:
                    print("Two ghosts can choose 2 monsters.")
                    for x in range(2):
                        for y in range(2):
                            while True:
                                try: 
                                    print("Please type %s's monster #%i" % ((ghosts[x]), y+1))
                                    monster = input()
                                    if not monster:
                                        raise ValueError
                                    fighters.append(monster)
                                    break
                                except ValueError as e:
                                    print("Type in the NAME OF THE MONSTER, not fokol... poes")
                    for x in range(2, 4):
                        while True:
                            try: 
                                print("Please type %s's monster " % ghosts[x])
                                monster = input()
                                if not monster:
                                    raise ValueError
                                fighters.append(monster)
                                break
                            except ValueError as e:
                                print("Type in the NAME OF THE MONSTER, not fokol... poes")
                elif num_of_ghosts == 5:
                    print("One ghost can choose 2 monsters.")
                    for x in range(2):
                        while True:
                            try: 
                                print("Please type %s's monster #%i" % ((ghosts[0]), x+1))
                                monster = input()
                                if not monster:
                                    raise ValueError
                                fighters.append(monster)
                                break
                            except ValueError as e:
                                print("Type in the NAME OF THE MONSTER, not fokol... poes")
                    for x in range(1, 5):
                        while True:
                            try: 
                                print("Please type %s's monster" % (ghosts[x]))
                                monster = input()
                                if not monster:
                                    raise ValueError
                                fighters.append(monster)
                                break
                            except ValueError as e:
                                print("Type in the NAME OF THE MONSTER, not fokol... poes")
                else:
                    print("Each ghost can choose 1 monster.")
                    for x in range(len(ghosts)):
                        while True:
                            try: 
                                print("Please type %s's monster" % (ghosts[x]))
                                monster = input()
                                if not monster:
                                    raise ValueError
                                fighters.append(monster)
                                break
                            except ValueError as e:
                                print("Type in the NAME OF THE MONSTER, not fokol... poes")

                input("<Enter>\n")

                
                print("All players roll initiative")
                battle(fighters)
                players.humanity_check(player_names)
                monsters = False
            
        input()

# Trap Room is the room where the ghosts are traps
# Will keep trap of the Human's movement and ghosts trap-placing turns
# Uses the amount of ghosts to determine the amount of traps each can lay
class TrapRoom(Room):
    
    def enter(self):
        webbrowser.open('https://www.youtube.com/watch?v=Jr9JVhr4R5Q&ab_channel=Fantasy%26WorldMusicbytheFiechters', new=0)
        player_names = players.get_names()
        ghosts = players.get_ghosts()
        print("Trap Room")
        input()

        print (dedent("""
            READ THIS:
            The player enters a room that only has dim light in the room is around the two doors. 
            The rest is pitch black darkness.

            15ft h x 60ft l x 40ft w
        """))
        input()

        print("The ghosts can each choose a place to place their traps.")

        num_of_ghosts = len(ghosts)
        if num_of_ghosts == 1:
            print("The ghost can place 6 traps per turn.")
        elif num_of_ghosts == 2:
            print("Each ghost can place 3 traps per turn.")
        elif num_of_ghosts == 3:
            print("Each ghost can place 2 traps per turn.")
        elif num_of_ghosts == 4:
            print("Two ghosts can place 2 traps per turn.")
        elif num_of_ghosts == 5:
            print("One ghost can place 2 traps per turn.")
        else:
            print("Each ghost can place 1 trap per turn.")
        input()

        done = False 
        while done == False:
            print("Let the ghosts place their traps. ")
            input()
            print("Now let the player move. " )
            input()
            
            check = input("Is it done? y/n ")
            if check == "y":
                done = True

        players.humanity_check(player_names)

# Restore Room is the room where the human becomes restored
# Will just print a message of how many dice the human can throw 
# And which stats it can restore
class RestoreRoom(Room):
    
    def enter(self):
        webbrowser.open('https://www.youtube.com/watch?v=phbQDW0XrdQ&ab_channel=Qumu', new=0)

        print("Restoration Room")
        input()

        print("The human restores 1D10 of health and 1D6 of all charges.")
        input()

# Treasure Rom is the room where the human can obtain treasure
# Will determine whether the chest and the door are mimics
# If neither, will randomly generate a treasure for the human
# If either, will print the rules for the ghosts, the call the battle function
# using the Human's name and a Mimic
class TreasureRoom(Room):
    
    def enter(self):
        webbrowser.open('https://www.youtube.com/watch?v=TfdXgKdogTM&ab_channel=MichaelGhelfi-RPGAmbiences%26Music', new=0)
        player_names = players.get_names()
        human = players.get_human()

        print("READ THIS:")
        input("<Enter>\n")

        print (dedent("""
            You see a treasure chest in the middle of a square room, 
            the walls made of rock that doesn't (and probably won't ever)
            seem to be damaged. It's solid. The room is well lit... With...
            I dunno, light... And right at the end of the room, and seeming
            to be the only exit out of here, is an open, inviting door...
        """))

        input("<Enter>\n")
        chest  = randint(1,6)
        input("creak...creak...")
        input("<Enter>\n")
        if chest == 1:
            print("The chest is a mimic")
            input()
            print("MIMIC BATTLE")
            print("-------------------------")
            input("If all the ghosts choose the same action")
            input("It succeeds")
            input("If not, each ghost rolls a d12")
            input("The highest rolls happens")
            
            fighters = [human, "mimic"]
            battle(fighters)
            players.humanity_check(player_names)
        else:
            print("The chest is, well... a chest")
            input()
            print("And inside is...")
            treasure = randint(1,6)

            if treasure == 1:
                print("Chain Mail: Afdah-Chain Mail")
                input()
                print (dedent("""
                    A completely iced out chain mail 
                    includes a layer of quilted fabric
                    worn underneath the mail to prevent chafing
                    and to cushion the impact of blows. 
                    The suit includes gauntlets with a knuckle
                    buster look.
                """))
                input()
                print (dedent("""
                    1st Level: 16 AC, stealth disad
                    2nd Level: 16 AC
                    3rd Level: 18 AC, movement -5
                    4th Level: 18 AC,
                    5th Level: 18 AC, resistance to 1 element
                """))
            elif treasure == 2:
                print("Cloak: Cloak of the Cool Breeze")
                input()
                print (dedent("""
                    A cloak with a strange shimmer and soft texture
                    You'd slip into it like a well shaped glove
                    You feel good, you move good
                """))
                input()
                print (dedent("""
                    1st Level: 1st atk: disadv to and from
                    2nd Level: 1st atk: disadv from
                    3rd Level: 1-2 atks: disadv from atks, movement slowed to and from
                    4th Level: 1-2 atk: atks from disadv & slowed
                    5th Level: 1-2 atk: atk from disadv & slowed, 14 DC chance to stun
                """))
            elif treasure == 3:
                print("Potion: Good Juice")
                input()
                print (dedent("""
                    Its got that sweet, sweet aroma. Hmmmmmm mhhh!
                    Silky, smooth, soft and juicy
                    Yeah mayn
                    Gotta have that good juice.
                """))
                input()
                print (dedent("""
                    1st Level: HP increases by 1d4 
                    2nd Level: HP increases by 1d6
                    3rd Level: HP increases by 1d8
                    4th Level: HP increases by 1d10
                    5th Level: All ability scores decrease by 1d12. 
                    - Don't drink that much good juice now.
                """))
            elif treasure == 4:
                print("Bow: Gattling")
                input()
                print (dedent("""
                    Its a really nice bow.
                    Mmmm it draws really nicely.
                    Hey honey, look, if I had an arrow now
                    You'd be... Ffffpt!
                    NOOOOOOOOOOOOO!!!!!!!!!!!!
                """))
                input()
                print (dedent("""
                    1st Level: Just aim and shoot. 
                    2nd Level: Damage +3, take 1 piercing damage per shot
                    3rd Level: Damage +3
                    4th Level: Damage +5, take 1d4 fire damage
                    5th Level: Damage +5, deal 1d4 (chaos elements)
                    CHAOS ELEMENTS
                    1- fire
                    2- ice
                    3- poison
                    4- force
                    5- psychic
                    6- thunder
                    7- lightning
                    8- acid
                """))
            elif treasure ==  5:
                print("Sword: X")
                input()
                print (dedent("""
                    It's adorned with only an X in its hilt
                    Dull black and grey, this sword doesn't
                    really look like much...
                    But why doesn't it...
                    And why does it feel like this?
                """))
                input()
                print (dedent("""
                    1st Level: 1d6, 1d4 extra dam (and to the player)
                    2nd Level: 1d6, 1d4 extra dam (and half to the player)
                    3rd Level: 1d8, 1d4 extra dam (and half to the player)
                    4th Level: 1d10, 1d4 extra dam (and to the player)
                    5th Level: Player can choose a dice for damage.
                    The enemy and the player must each take an attack from that dice
                """))
            elif treasure ==  6:
                print("Staff: Madeline")
                input()
                print (dedent("""
                    A sleek, slim, jet black staff with a dark, violet
                    large gem stone at the top.
                    It looks cool. "Yeah it does."
                    Hey who said that?
                """))
                input()
                print (dedent("""
                    1st Level: DC 12 Wis save, to blast arcane energy of 
                                power 1D10
                    2nd Level: DC 14 Wis save, to blast arcane energy of 
                                power 1D10+2
                    3rd Level: DC 16 Wis save, to blast arcane energy of 
                                power 1D12 + 2
                    4th Level: DC 18 Wis save, to blast arcane energy of 
                                power 2 D8
                    5th Level: Roll for 1 type of permanent madness.
                                The damage is always 3D10
                """))
        
        door  = randint(1,6)
        input("creak...creak...")
        if door == 1:
            print("The door is a mimic")
            input()
            print("MIMIC BATTLE")
            print("-------------------------")
            input("If all the ghosts choose the same action")
            input("It succeeds")
            input("If not, each ghost rolls a d12")
            input("The highest rolls happens")
            
            fighters = [human, "mimic"]
            battle(fighters)
            players.humanity_check(player_names)
        else:
            print("Eeeeeeeek the door opens")



#  Players
#---------------------------------------------------

# This method/function (whatever) keeps track of all things player related
# Has multiple get functions for the players', human's and ghosts' names
# Also runs the humanity check function
class Players(object):
    

    def __init__(self, player_names):
        self.player_names = player_names
    
    
    def get_names(self):
        return self.player_names

    def humanity_check(self, player_names):
        human = ""
        ghosts = []
        self.player_names = player_names

        print('Who is... "alive"?')

        for player in player_names:
            place = player_names.index(player) + 1
            print("%i) %s" % (place, player))



        while True:
            try:
                winner_number = (int(input("Type only the number "))-1)
                if winner_number >= len(player_names):
                    raise ValueError
                else:
                    winner = player_names[winner_number]
                    break
            except ValueError as e:
                print("That wasn't one of the player numbers... dumbass")

        for name in self.player_names:
            if winner == name:
                human = name
            else:
                ghosts.append(name)

        print("The human is %s" % human)
        input()

        print("The ghosts are: ")

        for y in range(len(ghosts)):
            print("%s" % ghosts[y])
        input()

        self.human = human
        self.ghosts = ghosts
    
    def get_human(self):
        return self.human
    
    def get_ghosts(self):
        return self.ghosts



#  Engine
#---------------------------------------------------

# The do all and end all of the game, literally
# Captures and executes the length of the game
# Randomly generates and enters rooms, making sure not to 
# repeat rooms soon after it's previous occurance.
# After going through all the room, randomly generates
# and enters the Boss Room
class Engine(object):
    
    def __init__(self, dungeon):
        self.dungeon = dungeon

    def play(self):
        
        # Setting and running the beginning room
        start_room = self.dungeon.next_room(0)
        start_room.enter()

        print("Now")
        input("<Enter>")

        # Elicits and records the length of the game
        print (dedent("""
            Would the players like:
            (1) a short or
            (2) long game?
        """))
        
        game_length = int(input("Type only the number "))
        while True:
            try:
                if game_length == 1:
                    num_of_rooms = randint(4,8)
                    break
                elif game_length == 2:
                    num_of_rooms = randint(8,12)
                    break
                else:
                    raise ValueError
            except ValueError as e:
                print("That's not an option... imbescile")
            
            
        # Uses the amount of rooms as a variable for a loop
        # Keeps track of rooms enterred to avoid frequent repetitions
        print("Building Dungeon")
        input("<Enter>\n")
        previous_room = start_room
        room_before = self.dungeon.next_room(3)

        for x in range(num_of_rooms):
            print("Generating Next room")
            input("<Enter>\n")
            random_room_num = randint(1, 4)
            current_room = self.dungeon.next_room(random_room_num)

            while True:
                if current_room == previous_room or current_room == room_before:
                    random_room_num = randint(1, 4)
                    current_room = self.dungeon.next_room(random_room_num)
                else:
                    break

            print("Get ready to enter the next Room")
            input("<Enter>\n")

            # # Uncomment this to test a room
            # #-------------------------------------------
            # #Test Function
            # #-------------------------------------------
            # test_room = dungeon.next_room(4)
            # test_room.enter()
            # #-------------------------------------------

            current_room.enter()
            room_before = previous_room
            previous_room = current_room

        # Generates a number to determine the boss room
        # Then Enters the boss room
        input("Well done")#This must be a message once all the rooms have been completed
        boss_number = randint(1,3)
        
        if boss_number == 1:
            bossroom = Minitaurs()
        elif boss_number == 2:
            bossroom = Hydrank()
        elif boss_number == 3:
            bossroom = Boneniknaks()
    
        human = players.get_human()
        ghosts = players.get_ghosts()
        bossroom.enter(human, ghosts)



# Dungeon
#----------------------------------------------------

# The methodunction keeping the names of the rooms
# Contains the functod that returns the name of the next room
class Dungeon(object):
    rooms = {
        0 : SortingRoom(),
        1 : MonsterRoom(),
        2 : TrapRoom(),
        3 : RestoreRoom(),
        4 : TreasureRoom()
    }

    def __init__(self, start_room):
        self.start_room = start_room
    
    def next_room(self, room_number):
        val = Dungeon.rooms.get(room_number)
        return val


# STARTUP
#----------------------------------------------------

# This is what happens when the app is first started.
# 1) It prints a welcome message
# 2) Elicits the amount of players and their names
# 3) Initialises the Players function with the player names
# 4) Initialises the Dungeon function
# 5) Initialises the Engine function with the Dungeon
# 6) Plays the game
# 7) Elicits the winner of the game
# 8) Prints and ending message


webbrowser.open('https://www.youtube.com/watch?v=VBlFHuCzPgY&ab_channel=AntoineB', new=0)
print("Welcome Message")
input()
print("How many players?")
while True:
    try:
        num_of_players = int(input())
        break
    except ValueError:
        print("'How many' means put in a number... idiot.")
        print("Try again:")

player_names = []

for x in range(num_of_players):
            while True:
                try: 
                    print("What is player %i's name" % (x+1))
                    name = input()
                    if not name:
                        raise ValueError
                    
                    player_names.append(name)
                    break
                except ValueError as e:
                    print("A name is not empty... please try again.")

players = Players(player_names)
dungeon = Dungeon(0)
game = Engine(dungeon)
game.play()

# At the end some really sad music plays, and the players get like a horrible game over song
webbrowser.open('https://www.youtube.com/watch?v=RYf-QgpZXaA&t=652s&ab_channel=SoulCandle', new=0)
print (dedent("""
    Who won?
    1. The Human
    2. The Ghosts
    Type only the number
"""))
while True:
    try:
        winner = int(input())
        if winner == 1:
            print ("You have successfully conquered the dungeon...")
            print ("And now... here you are... Powerful. But in the middle of nowhere.")
        elif winner == 2:
            print ("You have successfully prevented the human from conquering the dungeon.")
            print ("And now.. here you are... A ghost in an evil dungeon.")
            print ("All alone. Just you. Alone.")
        else:
            raise ValueError
            
        break
    except ValueError:
        print("Fkn read! Thats not '1' or '2'.")
        print("Try again:")

