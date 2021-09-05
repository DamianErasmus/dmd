from textwrap import dedent
from battle_stuff import *
import webbrowser

#  Bosses
#---------------------------------------------------------
# The bosses are still unconstruction
# As soon as they are completed
# Comments will be completed
class Boss(object):

    def enter(self):
        exit(1)
        
class Minitaurs(Boss):

    def enter(self, human, ghosts):
        webbrowser.open('https://www.youtube.com/watch?v=OwiQwxaGN1k&ab_channel=Tensei017', new=0)
        self.human = human
        self.ghosts = ghosts
        print (self.human)
        print (self.ghosts)
        print("Minitaurs")
        print(dedent("""
            Minitaurs are minotaurs, but smaller, with less physical strength
            but the same kind of fury as their larger cousins.
        """))

        input("<Enter>\n")

        print(dedent("""
            Upon enterring this room, the human finds itself in a labyrinth
            Filled with cute, yet menacing bellows coming from multiple directions
            The human has to find its way out, before what ever adorable demons
            that lurk in the shadows find him.
        """))

        print("As for the ghosts")

        num_of_ghosts = len(self.ghosts)

        if num_of_ghosts == 1:
            print("The ghost is all eight minitaurs")
        elif num_of_ghosts == 2:
            print("Each ghost is 4 minitaurs")
        elif num_of_ghosts == 3:
            print("2 ghosts are 3 minitaurs, 1 ghost is 2 ea")
        elif num_of_ghosts == 4:
            print("Each ghost is 2 minitaurs")
        elif num_of_ghosts == 5:
            print("3 ghosts are 2 minitaurs, 2 ghosts are 1 ea")
        elif num_of_ghosts == 6:
            print("2 ghosts are 2 minitaurs, 4 ghosts are 1 ea")
        elif num_of_ghosts == 7:
            print("1 ghost is 2 minitaurs, 6 ghosts are 1 ea")
        else:
            print("Each ghost is a minitaur")
        
        fighters = []
        fighters.append(self.human)
        if num_of_ghosts <= 8:
            for x in range(8):
                minitaur = ("Minitaur #%i" % (x+1))
                fighters.append(minitaur)
        else:
            for x in range(num_of_ghosts):
                minitaur = ("Minitaur #%i" % (x+1))
                fighters.append(minitaur)
        
        battle(fighters)

class Hydrank(Boss):

    def enter(self, human, ghosts):
        webbrowser.open('https://www.youtube.com/watch?v=vDL6741wq7s&ab_channel=Ekmule', new=0)
        self.human = human
        self.ghosts = ghosts
        
        print("Hydrank")
        print (dedent("""
            The human finds themselves in a room 
            They see a sleeping hydra about 15ft away from you. 
            Behind it they see a catapult armed with a boulder.
            The room REEEEEEKS with alcohol. 
            The ghosts are each in a very... VERY good place.
            Elicit responses.
        """))

        print(dedent("""
            Hydrank Boss Battle:
            -------------------------------------
            The ghosts can possess parts of the hydra
            The less ghosts their are the more hydra parts
            each can possess.
        """))
        input()

        num_of_ghosts = len(self.ghosts)

        if num_of_ghosts == 1:
            print("The ghost is the whole hydra")
        elif num_of_ghosts == 2:
            print("One ghost is the legs and 2 heads")
            print("The other is 3 heads")
        elif num_of_ghosts == 3:
            print("One ghost is the legs and 1 head")
            print("One ghost is 2 heads")
            print("The other is 1 head")
        elif num_of_ghosts == 4:
            print("One ghost is the legs and 1 head")
            print("One ghost is 2 heads")
            print("The other ghosts are the other heads")
        elif num_of_ghosts == 5:
            print("One ghost is the legs and a head")
            print("The other ghosts are the other heads")
        elif num_of_ghosts == 6:
            print("One ghost is the legs")
            print("The other ghosts are the heads")
        else:
            print("The ghosts with the highest initiatives get dibs")
            print("The others have to share (rolling disadvantage on all rolls)")
        
        

        input("<Enter>\n")
        print(dedent("""
            If the hydra takes (25) damage or like 10ish
            directed to one head, it will lose a head.
            That head regrows as two at the start of the hydras 
            next turn.
            
            Unless that damage was fire damage.
        """))
        input()
        print(dedent("""
            Everytime the hydra grows a new head, the ghost
            with the least control gets dibs.
            Because the hydra is drunk, it has a disadvantage 
            on perception checks and any attack that requires aiming.
            And it needs to throw a constitution save of (13) when moving,
            or not go in the direction it intended.
        """))
        input()
        print(dedent("""
            As for the human.
            It must defeat the hydra.
            Or never see the light of day.
            If it hides behind a column, the hydra must first make
            a Perception check to see the human, then attack.
        """))

        completion = False
        
        while completion != True:
            alight = True
            print(dedent("""
                Now back to the human. It has two choices:
                1. Move towards the catapult.
                2. The wrong choice
            """))
            
            choice = int(input("What's the choice?" ))
            
            print("The player throws a stealth check.")
            print("What's the roll? ")
            while True:
                try:
                    stealth = int(input())
                    break
                except ValueError:
                    print("There are only numbers on a die, what was the NUMBER?!")
            
            if stealth >= 15:
                if choice == 1:
                    print("The player moves towards the catapult.")
                    input()
                    blast = hydrapult(alight)
                    
                    if blast == True:
                        print("The hydra loses half it's hp")
        
            input("<Enter>\n")
            print("The ghosts open their eyes, and they see the human.")
            print("Yes, they are the hydra")
            
            fighters = []
            fighters.append(self.human)

            for x in range(len(ghosts)):
                fighters.append(ghosts[x])

            fighters.append("hydrapult")

            battle(fighters)
            

            completion = True

class SlimeTime(Boss):

    def enter(self):
        print("Slime Time")
        #Will complete SlimeTime in the future

class Boneniknaks(Boss):
    #Boneniknaks is just a skeleton, on its own.
    #But it has multiple parts that the ghosts can possess
    #Each part has it's own hp, ac, actions, attacks and maybe abilities
    #Parts:
    #----------------------------------
    #1. Head
    #2. Neck and Shoulders
    #3. Abdomen
    #4. Waist
    #5. Right arm
    #6. Left arm
    #7. Mid arm
    #8. Right leg
    #9. Left leg
    #10. Hind leg
    #11. Tail
    #12. "Tongue"
    #-----------------------------------
    #When all of the parts are together, they form Boneniknaks
    #Packs a punch similar to a real strong skeleton
    #Has a similar AC
    #But less HP (equal to a multiple of the bones)
    #When dropped to zero, the human gets a chance to attack the bones
    #With enough damage, can destroy said bones
    #But on the next round, Boneniknaks reforms, but with less HP (equal to a multiple of the bones)
    #The tongue can only be revealed (its basically a blob of sentient death essence) on the last round
    #Then only destroyed

    def enter(self, human, ghosts):
        webbrowser.open('https://www.youtube.com/watch?v=_BaKgJcv9MA&ab_channel=Iemdeath', new=0)
        self.human = human
        self.ghosts = ghosts
        print("Boneniknaks")
        input("<Enter>\n")
        print(dedent("""
            Human...
            You find yourself, once again, in a room with no exits.

            Why do you keep doing this to yourself?

            And before you stands... kinda

            A very large... badly assembled... skeletal figure.

            It's got a head where the upper part is disproportionately bigger than the lower
            The arms are very long... well accept for the tummy arm
            Shoulders are narrow... but thick! So is the chest plate, the ribs and the back plate
            The waist is very... circular. But quite sturdy
            The three legs are long, and near right angular, keeping the Boneniknaks nice and low
            And nice and mobile
        """))
        input("<Enter>\n")
        print(dedent("""
            Ghosts...

            The wonderful being you see in front of you

            This souless being, with multiple spaces for you to "relax"

            Its so... empty

            It's like a fully staffed mansion, free of charge to any who'd like to stay there
            Is uninhabited.

            It would be wrong to not atleast try to make use of the wonderful facilities

            OF THIS NECROTIC MACHINE OF DEATH!
        """))
        input("<Enter>\n")
        print(dedent("""
            Boneniknaks Info
            ----------------------------------------------
            Initiative works as normal
            On each of the humans turns it should first try to "burst" BNKS 
            Then destroy as many bones as possible before it reassembles

            Display the possession rules.
        """))
        input("<Enter>\n")

        print("Let the battle begin!")
        
        fighters = []
        fighters.append(human)

        for ghost in ghosts:
            fighters.append(ghost)
        
        battle(fighters)