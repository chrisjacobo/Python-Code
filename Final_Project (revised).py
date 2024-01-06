# Final Project - Alcaraz Escapee
# !/var/env python3
#
# File: Final Project
#
# This file is for creating the final project for out computer programming
# class
# Authors: Devin Schlisner, Chris Jacobo, Arse Tufa, Jiban Gurung
# Date: 2021 December 11
# Version: 1.0
# Course: CPTR 226
# Assignment: Final Project


# Includes
import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest
import random
import sys

# Global Variables


# Functions


# This runs if the file is run as a script vs included as a module

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--doctest', action='store_true',
                        help='Pass this flag to run doctest on the script')
    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    if(args.doctest):
        doctest.testmod(verbose=True)  # run the tests in verbose mode
    print("--------------------")

    print('You wake up and aggressively turn off the alarm that so\n'
          'rudely interrupted your sleep. You slowly roll out of bed\n'
          'and get ready for work. You show up for your shift and the \n'
          'prisoners are as rowdy as ever. You still wonder how you\n'
          'ended up as a guard at the famous Alcatraz Prison.\n')

    input('Press enter to continue: ')

    print('\nAs you are making your rounds, you notice that something\n'
          'is different. One of the cells is empty, but you swear that\n'
          'there should be a prisoner in there. You quickly ask the\n'
          'other guards but they aren\'t much help. To be safe, you\n'
          'request a perimeter search. You decide to go check outside\n'
          'yourself.\n')

    input('Press enter to check outside: ')

    print('\nYou walk outside and the guards stationed outside are all\n'
          'knocked out. You look out and see a speed boat driving off\n'
          'with the escapee. You sound the alarm and military personel\n'
          'arrive within seconds to chasae him down. After all of this,\n'
          'you are requested into an office for interrogation.\n')

    input('Press enter to step into the office: ')

    print('\nYou were apparently seen giving the escapee the key to his\n'
          'cell. You quickly deny it and tell them your side of the\n'
          'story, but they quickly silence you. They say they believe\n'
          'you but you still need to do something for them. They say\n'
          'the military is still searching for the escapee but they are\n'
          'trying to be discrete about it because they do not want the\n'
          'public informed about this mistake. So they are sending you\n'
          'to go catch him.\n')
    input('\nPress enter to begin your chase: ')
    print('-' * 50)

# Chris Jacobo
# Forest section
# Final Project
# Capturing Prisoner who escaped Alcatraz


class Forest:
    def __init__(self, hhp=120, hatk=12):
        self.hhp = hhp
        self.hatk = hatk

    def retriving(self, hhp, hatk):
        self.hhp = hhp
        self.hatk = hatk
        print("\nThe criminal runs into the forest! Hurry and capture him!")
        print("The criminal vanishes deep into the forest!")
        self.path(hhp, hatk)

    def path(self, hhp, hatk):
        path1 = input("There is two paths! Left and right choose where "
                      "he went (l,r) ")
        if path1 == "l":
            print("\nLook! There he is! He is really close!")
            print("Get ready to capture him!")
            input('\nPress enter to tackle him: ')
            self.attack_1(hhp, hatk)
        elif path1 == "r":
            print("\nWe lost him I don't know where he went!")
            self.path2(hhp, hatk)
        else:
            print("\nWhat are you doing!? He's getting away!")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()

    def path2(self, hhp, hatk):
        print("\nIf we keep going further we are probably are going to "
              "find him")
        print("You find a village nearby...")
        print("Let's ask them if they've seen our criminal.")
        ask = input("\nDo you want to go to village? (y,n) ")
        if ask == "y":
            print("\nOkay...")
            print("You go into the village")
            print("You ask around if they have seen the criminal")
            print("They didn't see him.")
            print("Mission Failed!")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()
        elif ask == "n":
            print("He probably wouldn't run through the village")
            print("\nMission Failed!")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()
        else:
            print('\nI guess he got away...')
            print("\nMission Failed!")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()

    def attack_1(self, hhp, hatk):
        jhp = 100
        jatk = random.randint(12, 15)
        print("\nWe got him!")
        input('\nPress enter to take him away: ')
        print("A jaguar shows up out of nowhere!")
        jaguar = input("Do you want to fight the jaguar? (y,n): ")
        if jaguar == "y":
            while self.hhp >= 20 and jhp >= 0:
                self.hhp -= jatk
                jhp -= self.hatk
                print("\nI've been hit", jatk, "hits",
                      self.hhp, "health remaining")
        elif jaguar == "n":
            print("\nSlowly back away from the animal...")
            print("Animal gets mad and attacks you!")
            print("YOU DIED")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()
        else:
            print("What are you doing!? The jaguar is gonna attack you!")
            print("Jaguar attacks you!")
            while self.hhp > 0:
                self.hhp -= jatk
            print("YOU DIED")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                first.retriving(120, 12)
            else:
                sys.exit()

    def moving_on(self, hhp, hatk):
        print("\nYou're badly injured, but you get reports that the criminal")
        print("Has run off into the mountains!")
        character = input("\nDo you want to recover and chase the criminal to"
                          " the mountains? (y,n) ")
        if character == "n":
            print("\nWell you need to catch him so I guess you don\'t\n"
                  "really have a choice...Well, get some sleep!")
        else:
            print("\nAlright you will rest for a while and continue tracking "
                  "our criminal down!")


first = Forest()
second = Forest()

print('\nYou heard that the prisoner was seen near the Amazon forest. You\n'
      'head to the forest to chase him down.')
first.retriving(120, 12)
second.moving_on(120, 12)

# Mountain by Jiban Gurung

your_health = 100
your_attackpoint = 15
yeti_attackpoint = 6
yeti_health = 20


class Project:
    def __init__(self, greeting):
        self.greeting = greeting

    def player(self):
        print("Hello and " + self.greeting, "\n")


intro = Project("WELCOME!!")
intro.player()


print("You have to go through the mountains to catch the escaped prisoner. \n"
      "You just made it through the forest. \n")
print('Before leaving the forest, you are given some food and a dull pocket\n'
      'knife from your supervisors.\n')

inventory = ('bread', 'pocket knife')
print("Now you have this much in your inventory: ")
print(len(inventory), 'items')
print(inventory)
input('\nPress enter to trek through the mountains: ')

print("-" * 50)


def yeti():
    choice = input(
        "\nYou have reached the Mountain and you see the prisoner far away.\n"
        "You have to catch him, but you see a Yeti ahead, and you have to\n"
        "get away from the yeti..\n"
        "what will you do? \n"
        "[1] Fight the Yeti \n"
        "[2] Run as fast as you can  :")

    if choice == "1":
        yetifight()

    if choice == "2":
        Runaway()


def yetifight():

    print("\nYou chose to fight the Yeti with your pocket knife.\n")

    global your_health
    your_attackpoint
    yeti_attackpoint
    yeti_health = 20

    print(
        f"Your health: {your_health}\nYour Attack Points: {your_attackpoint}\n"
    )
    print(
        f"Yeti health: {yeti_health}\nYeti Attack Points: {yeti_attackpoint}")
    print("-" * 50)

    game_loop = "play on"
    while game_loop == "play on":
        attack_opponent = random.randrange(
            1, 10)  # RANDOMIZATION, CHOOSES ANY NUMBER BETWEEN 1 AND 10

        if attack_opponent >= 6:  # You attack the Yeti..
            print('You hit the Yeti before he hits you.\n')
            yeti_health -= your_attackpoint
            print(f"Your remaining health is ", your_health, "\n")
        if attack_opponent < 6:  # Yeti attacks
            print("The Yeti attacks you.\n")
            your_health -= yeti_attackpoint
            print("Your remaining health is ", your_health, "\n")

        if yeti_health <= 0:  # If Yeti dies
            print(f"You killed the Yeti. Your health is {your_health}")
            Chase()
            break
        if your_health <= 0:
            print("You did not kill the Yeti. Sorry! yeti health "
                  f"is {yeti_health}")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                your_health = 100
                yeti_health = 20
                yeti()
                break
            else:
                sys.exit()


def Runaway():
    print("\nYou chose to runaway.\n" "But the Yeti is chasing you...")

    global your_health
    your_attackpoint
    yeti_attackpoint = 20
    yeti_health = 70

    print(f"Your health: {your_health}\n"
          f"Your Attack Points: {your_attackpoint}\n")
    print(f"Yeti health: {yeti_health}\n"
          f"Yeti Attack Points: {yeti_attackpoint}")
    print("-" * 50)

    game_loop = "play on"
    while game_loop == "play on":
        attack_opponent = random.randrange(
            1, 10)  # RANDOMIZATION, CHOOSES ANY NUMBER BETWEEN 1 AND 10

        if attack_opponent >= 8:  # You attack the Yeti
            print('You hit the Yeti before he hits you.\n')
            yeti_health -= your_attackpoint
            print(f"Your remaining health is ", your_health, "\n")
        if attack_opponent < 8:  # Yeti attacks
            print("The Yeti attacks you.\n")
            your_health -= yeti_attackpoint
            print("Your remaining health is ", your_health, "\n")

        if yeti_health <= 0:  # If Yeti dies
            print(f"You killed the Yeti. Your health is {your_health}")
            Chase()
        if your_health <= 0:
            print(f"You did not kill the Yeti. Sorry!")
            again = input('\nTry again? (y,n) ')
            if again == 'y':
                your_health = 100
                yeti_health = 20
                yeti()
                break
            else:
                sys.exit()


def Chase():
    print("-" * 50)
    option = input(
        f"\n\nYou survived the Yeti \n"
        "You see the prisonner taking the helicpter and flying to the "
        "Ocean.\n"
        "What will you do next? \n"
        "[1] ask for a help using the radio.\n"
        "[2] search for tools. \n"
        "[3] Use the zipline down the mountain:  ")

    if option == "1":
        print("\n NO")
        print("The Prisoneer escaped away.")
        input("Press enter to try again\n")
        Chase()

    if option == "2":
        print("\nYou found a few things lying around, but the tools aren't "
              "helpful now.")
        global inventory
        inventory += "Torch light", "map", "Boots"
        print("Now you have this much in your inventory: ")
        print(len(inventory))
        print(inventory)
        print("But I guess that doesn\'t matter since the prisoner escaped.")
        input("Press enter to try again\n")
        Chase()

    if option == "3":
        print("You made a good choice. You are one step closer to "
              "the prisoner.\n")


yeti()

# Ocean by Arse Tufa
print('-' * 50)


def fight(health, atk):

    enemy_health = 100
    enemy_attack = random.randint(5, 8)

    # description of the game
    print("\nYou have", hero_health, " health points and only a dull pocket\n"
          "knife to fight with.")

    print("Please type 'search' to search for a weapon on the boat")
    input(">")
    print("\nYou have searched the area around you and found a metal pipe" +
          " that gives you an attack value of 18")

    print("\nNow armed. You move forward to fight your way to freedom.")

    print("\nThe enemies in the water have ", enemy_health,
          " health points and attacks" + " of ", enemy_attack)

    # while statement to loop untill the game is done
    while health > 0 and enemy_health > 0:
        # choice
        print("\nPlease select a move:\n1. Punch \n2. Hit with the pipe " +
              "\n3. Stab with dull knife\n")
        x = int(input("1, 2 or 3 > "))
        y = random.randint(1, 3)
        # if the random number and and choice are the same
        if x != y:
            if x == 1:
                print("\nYou used Punch. It dealt ", enemy_attack, " dam" +
                      "age on you.")

            if x == 2:
                print("\nYou used pipe to hit the enemy. " +
                      "It dealt ", enemy_attack, "damage on you.")

            if x == 3:
                print("\nYou stabed the enemy but both your legs are damged")

                print("\nYou have no choice, you are surrounded by 100 of" +
                      " enemies")

                print("\nThey killed you")

                print("\nGAME OVER")
                again = input('\nTry again? (y,n): ')
                if again == 'y':
                    continue
                else:
                    break
            health -= enemy_attack
            print("You have ", health, " health remaining")
        # if the random number and and choice are not the same
        elif x == y:
            if x == 1:
                print("\nYou used Punch. It dealt ", atk, " damage" +
                      " on the enemy.")

            if x == 2:
                print("\nYou used pipe to hit the enemy. " +
                      "It dealt ", atk, " damage on the enemy.")

            if x == 3:
                print("\nYou stabed the enemy and broke your ankles")

                print("\nbut you made it to the safe zone")

                break
            enemy_attack = random.randint(5, 8)
            enemy_health -= atk
            print("enemy has ", enemy_health, " health remaining")
        if health == 0:
            print("\nYou finished your health point")

            print("\nYou have", health, " health point")

            print("\nGAME OVER!")
            again = input('\nTry again? (y,n): ')
            if again == 'y':
                continue
            else:
                break
        if enemy_health == 0:
            print("\nenemy has finished his point")

            print("\nhe has", enemy_health, " health points")

            print("\nYOU WON!")

            break


# Beginning of Story
print("\nYou wake up on a boat floating on the ocean. After getting off the\n"
      "mountain, you boarded this boat to take you towards the ecapee.")

print("\nIn order to survive you must fight your way to the other side" +
      "and find the prisoner.")


# main program
hero_health = 100
hero_attack = 10

hero_health = fight(hero_health, hero_attack)

# Cave by Devin Schlisner

health = 100
floor = 10
inventory = ['sword', 'shield', 'bread', ]


class Enemy(object):
    """Creating Enemy and Battle"""
    def __init__(self, name, ht=0):
        self.name = name
        self.hit = ht
        enemy_health = random.randint(35, 45)
        enemy_attack = random.randint(5, 25)
        self.enemy_health = enemy_health
        self.enemy_attack = enemy_attack

    def battle(self):
        """Battle Function"""
        global floor
        global health
        self.enemy_attack += floor
        print('\nA', self.name, 'appears and it looks even stronger '
              'than the last enemy.\n')
        turn = 0
        while health > 0 and self.enemy_health > 0:
            choice = 0
            hp_up = 0
            while choice == 0:
                hit = random.randrange(5)
                if self.hit == 1:
                    if turn == 1:
                        print('The', self.name, 'charges up for an attack\n')
                        self.enemy_attack += 30
                        hit = 3
                    if turn == 2:
                        self.enemy_attack -= 25
                if self.hit == 2:
                    if turn == 0:
                        print('\nThe bats begin to megre into a huge super'
                              'bat!')
                        self.enemy_health += 20
                        self.enemy_attack += 8
                if self.hit == 3:
                    print('Your attacks are slower in the water')
                print(inventory)
                item = str(input('\nWhat would you like to use? '))
                print('-' * 50)
                if item == 'sword' and 'sword' in inventory:
                    h_attack = 20
                    choice = 1
                    continue
                if item == 'bread' and 'bread' in inventory:
                    h_attack = 0
                    health += 10
                    choice = 1
                    hp_up = 1
                    continue
                if item == 'shield' and 'shield' in inventory:
                    h_attack = 0
                    hit = 5
                    choice = 1
                    continue
                if item == 'flashlight' and 'flashlight' in inventory:
                    print('\nThis really won\'t do you much good here.\n')
                    continue
                if item == 'rope' and 'rope' in inventory:
                    print('\nThis really won\'t do you much good here.\n')
                    continue
                if item == 'mysterious potion':
                    if 'mysterious potion' in inventory:
                        print('\nMaybe we shouldn\'t use a random potion we '
                              'got from a bat.\n')
                        continue
                    else:
                        print('\nI\'m sorry, please pick an item in your '
                              'inventory.\n ')
                        continue
                if item not in inventory:
                    print('\nI\'m sorry, please pick an item in your '
                          'inventory.\n ')
                    continue
            turn += 1
            if self.hit == 3 and h_attack > 7:
                h_attack -= 7
            if hp_up == 1:
                print('\nHealth inceased by 10.')
            print('\nThe', self.name, 'lunges at you.')
            if hit == 1:
                print('\nYou succesfully dodge the attack.')
            elif hit == 5:
                print('\nYou block the attack with your shield.')
                print('You blocked', random.randrange(5, self.enemy_attack),
                      'damage.')
            else:
                e_attack = random.randrange(5, self.enemy_attack)
                health -= e_attack
                print('\nThe', self.name, 'strikes you and deals', e_attack,
                      'damage.')
            self.enemy_health -= h_attack
            print('\nYou strike the', self.name, 'and deal',
                  h_attack, 'damage to it.\n')
            if health > 0 and self.enemy_health <= 0:
                print('You defeated the', self.name)
                print('\nYou have', health, 'health remaining.')
                gift = random.randrange(7)
                if gift == 5:
                    print('\nWhat luck! You find a health potion in the '
                          'enemy\'s possesion.')
                    health += 5
                    print('\nHealth increased by 5.')
        if health <= 0:
            print('\nThe', self.name, 'strikes you and you lose the '
                  'last bit\n'
                  'of strength you had left.')
            print('\n\nYou have died.')
            sys.exit()
        input('\nPress enter to move on: ')
        floor += 1


print('\nYou arrive in Kentucky where the escapee has recently been seen.\n'
      'You talk to the people who said that they recently saw him and they\n'
      'tell you that he was seen near Mammoth Cave. You grab a flashlight\n'
      'and a rope and head into the cave.\n')
input('\nPress enter to go into the cave? ')

print('\nAs you are about to enter the cave, one of your supervisors stops\n'
      'you and gives you a bag of items. He says these tools will be needed\n'
      'to make it through the cave.')
input('\nPress enter to look through the bag:')

print('\nYou got a sword and a shield.')
print('\nYou\'re carrying too much stuff. You decide to drop the metal pipe\n'
      'and dull pocket knife since you have a sword.')
inventory += 'flashlight', 'rope'
print('\nYour inventory is:')
print(inventory)

print('\nAs you are sqeezing through the narrow spaces, a giant spider\n'
      'attacks you out of nowhere!')
input('\nPress enter to fight: ')
spider = Enemy('Spider', 1)
spider.battle()

print('As you conitnue, you hear something moving around in the darkness\n')
dark = 3
while dark != '1' and dark != '2':
    dark = (input("""What would you like to do (please type a 1 or 2):
    [1] Use flashlight
    [2] Keep walking: """))
if dark == '1':
    print('\nYou shine your flashlight and see a bat chewing on something.\n'
          'You try to get closer but your presence startles it and it flies\n'
          'away. But it ends up dropping what it was chewing on. It looks\n'
          'like some mysterious potion.')
    inventory += 'mysterious potion',
if dark == '2':
    print('\nYou decide to just keep on walking, I\'m sure it is nothing '
          'important.')
print('\nYou come to a fork in the path and there are two possible tunnels.')
tunnel = 3
while tunnel != '1' and tunnel != '2':
    tunnel = (input("""Which tunnel would you like to take:
    [1] The Right
    [2] The Left: """))
if tunnel == '1':
    print('\nYou decide to follow the tunnel on the right.')
    print('\nYou enter a huge open room and quickly notice all of the bats\n'
          'on the ceiling. You try to remain quiet and not startle them,\n'
          'but someone else in the room throws a rock against the wall and\n'
          'bolts out of the room. The echoing from the impact of the rock\n'
          'frightens the bats. They all come swooping down at you.')
    input('\nPress enter to fight: ')
    bats = Enemy('Bat', 2)
    bats.battle()
if tunnel == '2':
    print('\nYou decide to follow the tunnel on the left.')
    print('\nYou enter a very small room and you can\'t seem to find the\n'
          'exit. You look down and there is a very small hole in the\n'
          'ground filled with water. You decide that the escapee probably\n'
          'didn\'t come this way, until you see the escapee\'s jacket and\n'
          'hat on the ground by the hole...')
    input('\nPress enter to jump in the water: ')
    print('\nYou jump in but can barely see anything. Luckily, your\n'
          'flashlight is waterproof. You shine it around to find a way out\n'
          'and you see the legs of someone swimming in the distance. You\n'
          'start swimming after them until a barracuda starts swimming\n'
          'directly at you! You won\'t make it back to the hole in time \n'
          'so you must fight.')
    input('\nPress enter to fight: ')
    barracuda = Enemy('Barracuda', 3)
    barracuda.battle()

print('\nAfter your exhausting battle, you manage to make it out of the '
      'cave.')
if 'mysterious potion' not in inventory:
    bat = ''
    while bat != 'y' and bat != 'n':
        bat = input('\nYou see a bat chewing on something beside you.\nDo you'
                    ' want to take time to go see what it is? (y,n): ')
    if bat == 'y':
        print('\nYou try to get closer but your presence startles it and it\n'
              'flies away. But it ends up dropping what it was chewing on.\n'
              'It looks like some mysterious potion.')
    inventory += 'mysterious potion',
    if bat == 'n':
        print('\nWell that\'s awkward... You kind of need to go look at\n'
              'that bat to beat the game...So you go over to the bat\n'
              'anyways. As you get closer, it flies away and drops what it\n'
              'was chewing on. It looks like some mysterious potion.')

print('\nYou then see the escapee hopping into a helicopter across the\n'
      'ravine infront of you. The ravine is too wide for you to jump, but\n'
      'you will not make it in time if your run around. What do you want to '
      'do?')

flash = 0
ravine = ''
while ravine not in inventory:
    print('\n', inventory)
    ravine = input('\nWhat item would you like to use? ')
    print('-' * 50)
    if ravine == 'mysterious potion':
        print('\nYou take the oddly colored liquid and quickly drink it.\n'
              'Nothing seems to happen, but you feel a bit lighter. You look\n'
              'down and notice that you aren\'t on the ground anymore. You\n'
              'are flying?!')
        input('\nPress enter to fly over to the helicopter: ')
        print('\nThe helicopter starts lifting off the ground and the\n'
              'escapee thinks that he has won, but you are able to grab\n'
              'onto the bottom of the helicopter. Before you can climb up,\n'
              'the effects of the potion wear off. All you can do is hold\n'
              'on for dear life.')
    if ravine == 'rope':
        print('\nYou try to throw the rope over the ravine and catch the\n'
              'helicopter. Your rope hooks on the chopper and you feel like\n'
              'a hero, until you realize that you did not hold on to the\n'
              'other end of the rope...You watch the helicopter fly away\n'
              'with your rope swaying in the wind.')
        again = input('\nTry again? (y,n): ')
        if again == 'y':
            print('-' * 50)
            ravine = ''
        else:
            sys.exit()
    if ravine == 'flashlight' and flash == 0:
        print('\nWhat are you going to do, blind them?')
        flash += 1
        ravine = ''
        continue
    if ravine == 'flashlight' and flash == 1:
        print('\nTrust me, this is a stupid idea.')
        flash += 1
        ravine = ''
        continue
    if ravine == 'flashlight' and flash == 2:
        print('\nOk, if you insist. You take the flashlight and shine it at\n'
              'the pilot\'s eyes. He becomes confused and starts flying the\n'
              'helicopter away from the light, which is also away from you...')
        again = input('\nTry again? (y,n): ')
        if again == 'y':
            print('-' * 50)
            ravine = ''
        else:
            sys.exit()
    if ravine == 'bread':
        print('\nYou decide that you have put in enough work for trying to\n'
              'catch one escapee. You sit down and take out the bread you\n'
              'have in your pocket, and you enjoy your snack while the\n'
              'escapee flies off. It\'s ok, you can always find a new job.')
        again = input('\nTry again? (y,n): ')
        if again == 'y':
            print('-' * 50)
            ravine = ''
        else:
            sys.exit()
    if ravine == 'sword':
        print('\nYou decide to attempt to throw your sword across the\n'
              'ravine. You back up to get a running start. You start\n'
              'building up speed to launch the sword into the helicopter.\n'
              'Suddenly, you trip on a loose rock and impale yourself in\n'
              'the leg...but that\'s not all. You end up falling down the\n'
              'long ravine. Luckily you land in water! Unluckily, it is\n'
              'very hard to swim with a sword in your leg.\n'
              '\nYou sadly drown.')
        again = input('\nTry again? (y,n): ')
        if again == 'y':
            print('-' * 50)
            ravine = ''
        else:
            sys.exit()
    if ravine == 'shield':
        print('\nYou take your shield out and...ok, I really don\'t know\n'
              'what you expected to do with this. I guess it can make for a\n'
              'comfortable seat as you watch them fly away.')
        again = input('\nTry again? (y,n): ')
        if again == 'y':
            print('-' * 50)
            ravine = ''
        else:
            sys.exit()

print('\nYou don\'t know where you are but you keep holding onto the leg\n'
      'of the helicopter with all your strength. Just as you feel like you\n'
      'can\'t hold on any longer, the helicopter begins to descend. You can\n'
      'see a landing pad coming into view. As it touches the ground, you\n'
      'quickly hide on under the chopper. You see the escapee come out of\n'
      'the helicopter laughing about his \"successful\" escape. You are\n'
      'eager to rain on his parade, but you have learned that patience is\n'
      'the key.')
input('\nPress enter to wait: ')
print('\nThe escapee and his friends enter the building next to you. You\n'
      'get up, brush yourself off and take out your phone to make an\n'
      'important call..')
print('\nWithin an hour, the military has surrounded the building and the\n'
      'escapee has nowhere to go.')
input('\nPress enter to take him away: ')

print("""     You Win! Congratulations!""")
