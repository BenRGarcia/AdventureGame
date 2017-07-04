"""Run this script with: $ python3 AdventureGame.py"""
class Scene(object):
    def enter(self):
        exit(1)

class Engine(object):
    pass

# Living choices
class Room(Scene):
    # Bathroom or Hallway
class Hallway(Scene):
    # Elevator or stairs (to Lobby)
class Lobby(Scene):
    # Outside_1 or Closet_1
class Closet_1(Scene):
    #
class Clost_2(Scene):

class Roof(Scene):

# Deadly choices
class Bathroom(Scene):
    # Zombies in bathroom eat your face off
class Elevator(Scene):
    # Zombies catch up to you at power outage elevators, eat your face off
class Outside_1(Scene):
    # Zombie hoard smells fresh meat and eats your face off
class Outside_2(Scene):
    # You shoot 3 Zombies before being overtaken by the hoard, face eaten off
class Shoot_Pilot(Scene):
    # You shoot creepy pilot, try to fly helicopter yourself, crash and burn, face eaten off

# happy ending
class Ending(Scene):
    # pilot flys you to safety of government Zombie Outbreak camp

"""

>>>Zombie Apocalypse<<<

Story Synopsis:
You wake up in a hospital room and you don't know where you are or how you got there.
All you know is that you're alone in the room and your head is pounding.
You realize the hospital room's door is closed and all power is out as you lay in the hospital bed.

Well isn't that strange...



Here is the scene order/decision to make:
1) Hospital Room: go to the bathroom (you really have to pee) <zombies eat you> or peek out the door to see WTH is going on <zombies chase you>
2) Hospital Hallway: take the elevator <power is out, zombies eat you> or take the stairs <zombies trip chasing you down stairs>
3) Hospital Lobby: you made it down the stairs into the main lobby, do you sprint to the outside <zombies swarm you, eat you> or look for a supply closet for supplies
4) Supply Closet: lucky you, you find a door labeled "Zombie Attack Supply Closet". Open the door, dead guy in the floor reanimates. Kill him for supplies or run to the outside <die>
5) Now that you have a backpack full of supplies and a shotgun with loooooads of ammo, do you face the zombies outside, or head to the roof to set off flares for help?
6) Hospital roof: Set off flares to attract helicopter's attention in hopes of being rescued. Shoot scary pilot and steal helicopter <crash>, or trust pilot not to kill you
7) Happy ending
"""
