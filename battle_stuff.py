def battle(victims):

    players = victims
    iniatative = []
    turns = []

    for name in players:
        print("What was %s's iniative roll?" % name)

        while True:
            try:
                roll = int(input())
                break
            except ValueError:
                print("There are only numbers on a die, what was the NUMBER?!")
        
        
        iniatative.append(roll)
    
    
    print("Reordering the turns...")
    input("<Enter>\n")

    while iniatative:
        most = int(max(iniatative))
        for i in range(0, len(players)):
            if iniatative[i] == most:
                turns.append(players[i])
                players.pop(i)
                iniatative.pop(i)
                break

    print("Reordering complete.")
    input("<Enter>\n") 

    battle_over = "n"

    alight = False

    while battle_over != "y":

        for turn in turns:
            print("It is %s's turn." % turn)
            input()
            if turn == "hydrapult":
                blast = hydrapult(alight)
                alight = not alight
            
            print("Is it done?")

            while True:
                try:
                    battle_over = input("(Type y or n) ")
                    if battle_over == "y":
                        break
                    elif not battle_over:
                        raise ValueError
                    elif battle_over != "n":
                        raise ValueError
                    break
                except ValueError as e:
                    print("(Sigh) please only type y or n... as stated before")

            if battle_over == "y":
                break  
                
def hydrapult(alight):
    a = alight
    success = False
    if a == True:
        print("It's loaded with a fire boulder.")
            
        aim = input("Aim? y/n ")
        if aim == "y":
            print("Player rolls Intelligence to aim.")
            while True:
                try:
                    roll = int(input())
                    break
                except ValueError:
                    print("There are only numbers on a die, what was the NUMBER?!")
            
            
            if roll >= 12:
                input("Human aim good.")
                input("Human deal 1d8 bludgeoning and 1d6 fire damage")
                success = True
                return success
            else:
                print("The boulder goes off in the wrong direction")
        else:
            print("That was kinda a waste of time.")
            return success
    else:
        print("The catapult is unloaded.")
        return success    
    
        
