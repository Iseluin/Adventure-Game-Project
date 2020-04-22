import time
import random
import sys


companions = []
HPWarchief = 90
HPSigurdr = 45
HPTorag = 45


def delay_print(s):

    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)


def valid_input_ingame(narrate, player_choice, options):

    narrator(narrate, 2)
    while True:
        choice = input(player_choice).lower()
        for option in options:
            if option == choice:
                return str(choice)
        narrator("'DM say's : 'I can't let you do that, do something else,"
                 " something\nrelevant'\n\n", 2)


def valid_input_system(narrate, player_choice, options):
    #  when i use "in" instead of "==" game crashes when the player gives an
    #  input something like "1111111" instead of "1".
    narrator(narrate, 2)
    while True:
        choice = input(player_choice).lower()
        for option in options:
            if option == choice:  # <== here.
                return str(choice)
        narrator("Unknown command, please select one of the options.\n\n", 2)


def narrator(prompt, time_to_wait):

    delay_print(prompt)
    time.sleep(time_to_wait)


def die_roll_player():

    dieroll = random.randint(1, 20)
    narrator("'Die is ...'\n\n", 2)
    narrator("'" + str(dieroll) + "!'\n\n", 2)
    return dieroll


def die_roll_npc():

    dieroll = random.randint(1, 20)
    narrator("'And he rolls...'\n\n", 2)
    narrator("'" + str(dieroll) + "!'\n\n", 2)
    return dieroll


def pick_target():

    targets = ['Sigurdr', 'Torag']
    picked_target = random.choice(targets)
    return picked_target


def random_attacker():

    list = ['Sigurdr', 'Torag']
    attacker = random.choice(list)
    return attacker


def join_together():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag

    playerinput = valid_input_system("Do you want Torag to join you ?\n\n",
                                     "Y/N?\n\n", ["y", "n"])
    if "y" in playerinput:
        companions.append("Torag")
        narrator("'Torag joins you and you both run back to the hill\n\n"
                 "You see the warchief is about to break the line...'\n\n", 2)
        main()
    if "n" in playerinput:
        narrator("'He shrugs, wishes you good luck with the warchief and "
                 "rushes back into the fray'\n\n", 2)
        main()


def engage_alone():

    playerinput = valid_input_ingame("'You really think that you stand a "
                                     "chance against that brute alone ?\n\n",
                                     "Enter 1. To Attack\n"
                                     "Enter 2. To Go Back\n\n", ['1', '2'])
    if playerinput == '1':
        fight_alone()
    elif playerinput == '2':
        main()


def engage_together():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag
    playerinput = valid_input_ingame("'Since you have Torag with you, "
                                     "you think your chances of taking "
                                     "him\ndown are slightly higher'\n\n",
                                     "Enter 1. To Attack\n"
                                     "Enter 2. To Go Back\n", ['1', '2'])
    if playerinput == '1':
        print("\n\n")
        fight()
    elif playerinput == '2':
        print("\n\n")
        main()


def fight_alone():

    global HPWarchief
    global HPSigurdr

    narrator("You decide to attack him alone and wish for the best !\n\n", 2)
    narrator("DM says: 'Roll 20'\n\n", 2)
    narrator("You roll...\n\n", 2)
    dieroll = die_roll_player()
    if dieroll >= 19:
        narrator("'With the help of your tremendous luck, you manage to bury "
                 "your hatchet\nin his head !'\n\n", 2)
        narrator("'As the DM, I wasn't expecting this at all..'\n\n", 2)
        narrator("'He trembles down with lifeless eyes...'\n\n", 2)
        narrator("'Soldiers are cheering your name and celebrating as the"
                 " orcs lose heart\n and flee !'", 2)
        narrator("'Congratulations, you won the battle and thus, the game !!'",
                 2)
        play_again()
    elif dieroll < 19:
        narrator("'You fail miserably, warchief looks at you and grins..\n\n"
                 "'He swings his greataxe ...\n\n'", 2)
        dieroll = die_roll_npc()
        if dieroll < 10:
            narrator("'You dodge the axe at the last second and barely "
                     "manage\nto get behind your shieldwall !\n\n", 2)
            narrator("'A few soldiers looks back at you with disbelief'"
                     "\n\n", 2)
            engage_alone()
        else:
            HPSigurdr = 0
            narrator("'You are in death save, you are defeated'\n\n", 2)
            play_again()


def friendly_turn():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag
    print(f"Warchief's HP is = {HPWarchief}")
    print(f"Sigurdr's HP is = {HPSigurdr}")
    print(f"Torag's HP is = {HPTorag}\n\n\n")
    narrator("'You go first !'\n\n", 2)
    narrator("'Roll 20 !'\n\n", 2)
    dice = die_roll_player()
    if dice <= 9:
        attacker = random_attacker()
        narrator("'" + attacker + " attacks !'\n\n", 3)
        narrator("'And thats a miss !'\n\n", 2)
    elif 9 < dice < 18:
        attacker = random_attacker()
        narrator("''" + attacker + " attacks and hits !'\n\n", 2)
        HPWarchief -= 25
        narrator("Warchief's current HP is:" + str(HPWarchief) + "\n\n", 2)

        if HPWarchief <= 0:
            narrator("'You managed to beat the Warchief and win the battle !'"
                     "\n", 2)
            narrator("'Congratulations !'\n\n", 2)
            play_again()

    elif dice > 18:
        narrator("'Nice roll !'\n\n", 2)
        narrator("'You attack him together !'\n\n", 2)
        narrator("'Thats a big hit !'\n\n", 2)
        HPWarchief -= 45
        narrator("Warchief's current HP is:" + str(HPWarchief) + "\n\n", 2)

        if HPWarchief <= 0:
            narrator("'You managed to beat the Warchief and win the battle "
                     "!'\n\n", 2)
            narrator("'Congratulations !'\n\n", 2)
            play_again()


def warchief_turn():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag

    narrator("'Warchief's Turn !'\n\n", 3)
    dice = die_roll_npc()
    if dice <= 13:
        target = pick_target()
        narrator("'And he goes for...'\n\n", 2)
        narrator("'" + target + "'!\n\n", 2)
        narrator("'That's a miss '!\n\n", 1)
    elif 13 < dice < 19:
        target = pick_target()
        if target == "Sigurdr":
            narrator("'And he goes for...'\n\n", 2)
            narrator("'" + target + "!'\n\n", 1)
            narrator("'He hits !'\n\n", 2)
            HPSigurdr -= 20
            narrator("Sigurdr's current HP is:" + str(HPSigurdr) + "\n\n", 2)
            if HPSigurdr <= 0:
                narrator("'Sigurdr stumbles down, his last words were:\n"
                         "'Torag, find her...'\n",
                         "He is in death save, you lose.'\n\n", 2)
                play_again()
        elif target == "Torag":
            narrator("'And he goes for...'\n\n", 2)
            narrator("'" + target + "'!\n\n", 1)
            narrator("'He hits !'\n\n", 2)
            HPTorag -= 20
            narrator("Torag's current HP is:" + str(HPTorag) + "\n\n", 2)
            if HPTorag <= 0:
                narrator("'Torag, is hacked by warchiefs axe ...'\n",
                         "'He is in death save, you lose.'\n\n", 2)
                play_again()
    elif dice >= 19:
        # Note to myself : use an " f"{}" " statement here and there
        # when you have time.
        target = pick_target()
        narrator("'And he goes for...' \n\n", 2)
        narrator("'" + target + "'!\n\n", 1)
        narrator("'He hits ! Ouch that's gonna hurt !'\n\n", 2)
        if target == "Sigurdr":
            HPSigurdr -= 25
            narrator("Sigurdr's current HP is:" + str(HPSigurdr) + "\n\n",
                     2)
            if HPSigurdr <= 0:
                narrator("'Sigurdr stumbles down, his last words were:\n"
                         "'Torag, find her...'\n",
                         "He is in death save, you lose.'\n\n", 2)
                play_again()
        elif target == "Torag":
            narrator("'And he goes for... '\n\n", 2)
            narrator(target + "!\n\n", 1)
            narrator("'He hits ! Ouch that's gonna hurt !'\n\n", 2)
            HPTorag -= 25
            narrator("Torag's current HP is:" + str(HPTorag) + "\n\n", 2)
            if HPTorag <= 0:
                narrator("'Torag, is hacked by warchiefs axe ...'\n",
                         "'He is in death save, you lose.'\n\n", 2)
                play_again()


def intro():

    narrator("DM say's : 'Things are not looking pretty, boys. The orc "
             "warchief is \nwreaking havoc on your lines.'\n\n", 1)

    narrator("'Your soldiers are falling one by one with each swing of his "
             "axe.\n\n", 1)

    narrator("'Sigurdr, Torag has flung himself into the fray as "
             "usual...'\n\n", 1)

    narrator("'You are on the high ground, just behind friendly lines and you"
             " have a \ngood view of the battlefield.'\n\n", 1)

    narrator("'Your 'tactics' skill is high enough to know that your soldiers"
             " are no \nmatch to the Orc Warchief and the line is about to "
             "break ...',\n\n", 2)

    narrator("'And let's be honest, the chances of you taking him down by "
             "yourself are not really high.'\n\n", 2)

    narrator("'But thankfully ...'\n\n", 3)

    narrator("'You can see Torag leading his contingent to fend off an enemy "
             "manouver on the flank. He took a good position and you know that"
             "his 'boys'\n -as he calls them- can easily hold the enemy by "
             "themselves...'\n\n", 2)

    narrator("'You know that you have a better chance of taking down the "
             "Warchief with him than alone. And you know that he has to be "
             "taken care of or he will break the center of your army in no "
             "time'\n\n", 1)

    narrator("'You assess the situation, you can try to deal with him yourself"
             " but you wont really stand a chance. On the other hand, if you "
             "could take Torag\nwith you...'\n\n", 2)


def main():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag
    playerinput = valid_input_system("You are on the hill, behind the lines, "
                                     "relatively safe.\n\n"
                                     "What do you want to do ?\n\n ",
                                     "Enter '1' To Engage The Warchief\n "
                                     "Enter '2' To Sprint To The Flank\n\n ",
                                     ['1', '2'])
    if playerinput == '1':
        narrator("'You charge towards the warchief'\n\n", 1)
        narrator("'He is busy finishing up a fallen brother...'\n\n", 2)
        narrator("'He sees you approach and points you with his axe...'\n\n",
                 2)
        narrator("'Soldiers, friend and foe alike stops fighting as if there "
                 "was a silent\n armistice and start watching you duel !'\n\n",
                 2)

        if "Torag" in companions:
            engage_together()
        else:
            engage_alone()

    elif playerinput == '2':
        the_flank()


def the_flank():

    global companions
    narrator("You start sprinting towards Torag's contingent.\n\nA few arrows "
             "fly over your head, you finally reach the flank.\n\n", 2)

    if "Torag" not in companions:
        narrator("You see Torag screaming orders everywhere as he swings his "
                 "bastard sword.\n\n", 2)
        narrator("He sees you approach and asks: \n\n"
                 "'Big guy is causing problems huh ?\nWas about to head there"
                 " myself after we secured the flank but...\nHe looks tough.\n"
                 "Nevertheless...\nWe must hold the center or the battle will"
                 " surely be lost.'\n\n", 2)
        join_together()
    else:
        narrator("'Torag's boys are doing fine a fine job at keeping the enemy"
                 " at bay.\nTorag smirks. Nothing much to do here...'\n\n", 2)
        narrator("'You head back to the hill.\n\n'", 2)
        main()


def fight():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag

    if HPWarchief > 0 and HPSigurdr > 0 and HPTorag > 0:
        friendly_turn()
        if HPWarchief > 0:
            warchief_turn()
            narrator("You back up a little and catch your breath\n\n", 2)
            engage_together()
    else:
        narrator("You won !\n\n", 2)
        narrator("You managed to beat the warchief !\n\n", 2)
        play_again()


def play_again():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag
    narrator("GAME OVER\n\n", 2)
    playagaininput = valid_input_system("Would you like to play again ?\n\n",
                                        "Y/N ?\n\n", ["y", "n"])
    if playagaininput == "y":
        narrator("Loading...\n\n\n\n\n\n\n\n", 3)
        narrator("Initializing...\n\n\n\n\n\n", 3)
        narrator("Lets play !\n\n\n", 2)
        init()
    elif playagaininput == "n":
        narrator("Thanks for playing !\n\n", 0)
        exit()


def game():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag
    companions = []
    HPWarchief = 90
    HPSigurdr = 45
    HPTorag = 45

    main()


def init():

    global companions
    global HPWarchief
    global HPSigurdr
    global HPTorag

    companions = []
    HPWarchief = 90
    HPSigurdr = 45
    HPTorag = 45
    game()


game()


#  couldn't figure out how to use the "scope". Would be glad if you'd
#  explain about it in your review.
#  There seems to be a problem with valid input functions. Explained inside
#  the function.
