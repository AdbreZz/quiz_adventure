health = 100
boss_health = 150
boss_damage = 0
your_damage = 0

def statusbar():

    global your_damage, health, boss_damage, boss_health
    health = health - your_damage
    boss_health = boss_health - boss_damage
    print("")
    print("You lose", your_damage, "health!")
    print("The dragon loses", boss_damage, "health!")

    if health <= 0:
        end1()

    if boss_health <= 0:
        end2()


def attack1():

    global health, your_damage, boss_health, boss_damage
    print("")
    print("You get word of a dragon flying around the castle,")
    print("You grab your sword and your bow and you head outside,")
    print("")
    print("The dragon spots you, and swoops down,")
    print("")
    print("Choose your first move:")
    print("A. Attack with bow")
    print("B. Block with your shield")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("The arrow pierces the dragon scaley skin!")
        boss_damage = 20
        your_damage = 0
        statusbar()
        attack2()

    if answer.lower() == "b":
        print("")
        print("Your shield reflects some damage onto the dragon,")
        print("But you absorb some of it yourself!")
        your_damage = 10
        boss_damage = 10
        statusbar()
        attack3()

def attack2():

    global health, your_damage, boss_health, boss_damage
    print("")
    print("Now it's the dragon's turn,")
    print("He wacks you with his tail,")
    print("You fall to the floor!")
    your_damage = 20
    boss_damage = 0
    statusbar()
    attack3()

def attack3():

    global health, your_damage, boss_health, boss_damage
    print("")
    print("---------------------------------------------------")
    print("")
    print("It's your turn again!")
    print("The dragon lands on the grass infront of you")
    print("Double sword damage this round!")
    print("")
    print("Do you attack or do you defend?")
    print("A. Block with your shield")
    print("B. Strike with your sword")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("You try to block with your shield,")
        print("But the dragon blasts right through it!")
        your_damage = 20
        boss_damage = 0
        statusbar()
        attack5()

    if answer.lower() == "b":
        print("")
        print("You strike the dragon with your sword,")
        print("Which stuns him,")
        print("Allowing you to attack again!")
        boss_damage = 40
        your_damage = 0
        statusbar()
        attack4()

def attack4():

    global health, boss_health, boss_damage, your_damage
    print("")
    print("----------------------------------------------")
    print("")
    print("Dragon's turn again, and he's mad!")
    print("He picks you up in his mouth,")
    print("Flies you high,")
    print("And drops on the cobblestone below!")
    print("Critical hit!")
    your_damage = 30
    boss_damage = 0
    statusbar()
    attack5()

def attack5():

    global health, boss_health, your_damage, boss_damage
    print("")
    print("---------------------------------------------------")
    print("")
    print("Note: Everytime you block, you get to attack or defend again!")
    print("" )
    print("The dragon charges towards you!")
    print("")
    print("You know how this works:")
    print("A. Sword strike (not double damage)")
    print("B. Shield the attack (you get another turn)")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("You try to attack the dragon,")
        print("But he just hits you with a burst of his fire breath!")
        your_damage = 20
        boss_damage = 0
        statusbar()
        attack6()

    if answer.lower() == "b":
        print("")
        print("Perfect block!")
        print("The dragon stumbles,")
        print("Allowing you to attack again!")
        boss_damage = 20
        your_damage = 0
        statusbar()
        attack7()

def attack6():

    global health, boss_health, boss_damage, your_damage
    print("")
    print("------------------------------------------------")
    print("")
    print("You've made a mistake,")
    print("And the dragon will punish you for it.")
    print("He strikes you with his razor sharp claws!")
    print("health =", (health - 20))
    your_damage = 20
    boss_damage = 0
    statusbar()
    attack7()

        

def attack7():

    global boss_health, boss_damage, health, your_damage
    print("")
    print("-----------------------------------------------")
    print("")
    print("Your turn again,")
    print("How do you approach this?")
    print("A. Use your sword")
    print("B. Shoot your bow")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("Success!")
        print("You pierce the dragon's skin!")
        your_damage = 0
        boss_damage = 20
        statusbar()
        

    if answer.lower() == "b":
        print("")
        print("Critical hit!")
        print("You pierce the dragon's skin!")
        your_damage = 0
        boss_damage = 40
        statusbar()

    attack8()

def attack8():

    global health, boss_health, boss_damage, your_damage
    print("")
    print("------------------------------------------------------------")
    print("")
    print("You are started to get tired,")
    print("So you have no choice but to let the dragon attack you!")
    your_damage = 10
    boss_damage = 0
    statusbar()
    attack9()

def attack9():

    global health, your_damage, boss_health, boss_damage
    print("")
    print("---------------------------------------------------")
    print("")
    print("You have regained you energy back,")
    print("You find an enchanted bow on the ground,")
    print("Bows do double damage this round!")
    print("A. Shoot your bow (double damage)")
    print("B. Go with the safe option, shield")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("You know how to listen to advice!")
        print("You hit the dragon and it falls to the ground!")
        print("Allowing you to shoot it again!")
        boss_damage = 50
        your_damage = 0
        statusbar()
        attack10()

        
    if answer.lower() == "b":
        print("")
        print("Got to be safe!")
        print("While you do reflects 10 points of damage back to the dragon,")
        print("You absorb 10 points yourself!")
        your_damage = 10
        boss_damage = 10
        statusbar()
        attack10()

def attack10():

    global health, boss_health, boss_damage, your_damage
    print("")
    print("----------------------------------------------")
    print("")
    print("The dragon is starting to lose stamina,")
    print("Looks like you get to attack again!")
    print("You find a sharpened axe on the floor!")
    print("Will you use it?")
    print("A. Use the axe")
    print("B. Keep your distance, use your bow!")
    answer = input("Answer: ")

    if answer.lower() == "a":
        print("")
        print("Critical hit!")
        print("You chopped off one of the dragon's legs!")
        print("Ultimate damage!")
        boss_damage = 60
        your_damage = 0
        statusbar()
        attack11()


    if answer.lower() == "b":
        print("")
        print("A smart option,")
        print("But maybe not the best pick this time around,")
        print("You move backwards and fire at the dragon,")
        your_damage = 0
        boss_damage = 20
        statusbar()
        attack11()


def attack11():

    pass


def end1():

    print("")
    print("You have been defeated by the dragon!")
    print("")
    print("------------------------------------------------")
    attack1()
        


def end2():

    print("")
    print("You have defeated the dragon!")
    

    

    

    
    



    

if __name__ == "__main__":
    attack1()
        
    

    
