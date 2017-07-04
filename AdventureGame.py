"""Run this script with: $ python3 AdventureGame.py SplashScreen.txt"""
from sys import exit
from sys import argv
script, file_1 = argv


class Scene(object):
    def enter(self):
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('ending')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Deadly(Scene):
    print ("Who knew surviving a Zombie Apocalypse would be so hard? Better luck next time.")
    def enter(self):
        exit(1)

# Living choices
class Room(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("You wake up in a hospital room. You don't know how you got here or for how long.")
        print ("All you know is your head is pounding, it is silent, and the power appears to be out.")
        print ("\nYou stand up out of your bed and you hear a curious groaning coming from the bathroom.")
        print ("You really have to go to the bathroom, but you're also curious to take a look in to the hallway.")
        print ("\nDo you go to the bathroom or look down the hallway?")
        answer_1 = input(">>>").lower()

        if "bathroom" in answer_1:
            print (input("Great. Hit the ENTER key to head into the bathroom.\n>>>"))
            return 'bathroom'

        elif "hallway" in answer_1:
            print (input("Great. Hit the ENTER key to head into the hallway.\n>>>"))
            return 'hallway'

        else:
            print (input("Eh. That doesn't sound like a good idea. Let's try this one more time.\n>>>"))
            return 'room'

class Hallway(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("As you peek out in to the hallway, you see a couple Zombies shuffling about.")
        print ("\nDown one side of the hallway you see a clear path to an elevator.")
        print ("Down the other side of the hallway (through the Zombies) lie the stairs.")
        print ("\nLooks like you're gonna have to make a run for it to survive.")
        print ("Do you run to the elevator, or, run past the Zombies to go to the stairs?")
        answer_2 = input(">>>").lower()

        if "elevator" in answer_2:
            print (input("Great. Hit the ENTER key to sprint towards the elevators.\n>>>"))
            return 'elevator'

        elif "stairs" in answer_2:
            print (input("Great. Hit the ENTER key to sprint through the Zombies towards the stairs.\n>>>"))
            return 'lobby'

        else:
            print (input("Eh. That doesn't sound like a good idea. Let's try this one more time.\n>>>"))
            return 'hallway'

class Lobby(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("Wow. The Zombies are pretty slow on foot and you make it to the stairs.")
        print ("Looks like you made the right decision.")
        print ("\nAs you head down the stairs, the map on the walls says you're approaching the main lobby.")
        print ("You arrive at the lobby and surprisingly it appears to be Zombie free.")
        print ("\nThe front door is within eyesight, but there's a sign by a door for a supply closet nearby.")
        print ("There may be something useful in there for your journey.")
        print ("\nDo you go ahead and exit the building, or, take a look in the supply closet?")
        answer_3 = input(">>> ").lower

        if "exit" or "building" in answer_3:
            print (input("Great. Hit the ENTER key to exit the hospital through the front doors.\n>>>"))
            return 'outside_1'

        elif "supply" or "closet" in answer_3:
            print (input("Great. Hit the ENTER key to head towards the supply closet.\n>>>"))
            return 'closet_1'

        else:
            print (input("Eh. That doesn't sound like a good idea. Let's try this one more time.\n>>>"))
            return 'lobby'


class Closet(Scene):
    def enter(self):
        print("\033c")
        print ("As you walk towards the supply closet, you see a small hand-written sign on the door that reads:")
        print ("'Zombie Attack Supply Closet'. Wow, that's convenient, huh.")
        input(">>>")
        print ("\nYou open the supply cabinet door. Inside you see a man who appears dead lying in the floor.")
        print ("Suddenly, he begins to stir. You have just witnessed the reanimation of a human becoming a Zombie.")
        print ("You instinctively stomp his head in (nice job, BTW) and you discover a wonderful collection of supplies.")
        print ("You find a shotgun, loads of ammo, and a backpack full of supplies like MRE's and a flare gun.")
        input(">>>")
        print ("\nOn the wall inside you see another sign that shows the location of a helipad on the roof of the hospital.")
        print ("Do you head to the roof with your supplies to shoot off some rescue flares, or,")
        print ("Do you head out the front door and let your shotgun do the talking with those Zombies out there?")
        answer_4 = input(">>>").lower

        if "front" or "door" in answer_4:
            print (input("Great. Hit the ENTER key to head outside and deliver some shotgun justice to those Zombies.\n>>>"))
            return 'outside_2'

        elif "roof" in answer_4:
            print (input("Great. Hit the ENTER key to head towards the helipad on the roof.\n>>>"))
            return 'roof'

        else:
            print (input("Eh. That doesn't sound like a good idea. Let's try this one more time.\n>>>"))
            return 'closet'


class Roof(Scene):
    def enter(self):
        print("\033c")
        print ("You make it to the helipad on the roof. Not 2 minutes after firing off the first flare,")
        print ("you hear the whirring of a helicopter approaching the hospital.")
        print ("As the pilot touches down, you are overcome with the joy of your rescue.")
        input(">>>")
        print ("\nJust as you're about to board the helicopter, you get a look at how grotesque the pilot looks.")
        print ("In fact, you see that he is badly injured himself and it's possible he'll turn in to a Zombie momentarily.")
        print ("Do you shoot the pilot with your shotgun to fly yourself outta hear, or,")
        print ("do you just hope the pilot will fly you to safety?")
        answer_5 = input(">>>").lower

        if "shoot" or "shotgun" in answer_5:
            print ("History favors the bold, am I right?!")
            print (input("Hit the ENTER key to fly this baby outta here."))
            return 'shoot_pilot'

        elif "hope" or "safety" in answer_5:
            print ("Great. Hit the ENTER key see what happens next.")
            return 'ending'

        else:
            print (input("Eh. That doesn't sound like a good idea. Let's try this one more time.\n>>>"))
            return 'closet'

# Deadly choices
class Bathroom(Scene):
    def enter(self):
        print("\033c")
        print ("Zombies lurch at you from inside the bathroom, eating your face off.")
        print ("How were you supposed to know there were Zombies in there? I guess the moaning didn't give it away.")
        return 'deadly'

class Elevator(Scene):
    def enter(self):
        print("\033c")
        print ("Um... Did you forget the part about the power being out?!")
        print ("Guess not. Well, the Zombies caught up and begin eating your face off.")
        return 'deadly'
        

class Outside_1(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("You should've looked before you leaped. The Zombie Hoards are vast.")
        print ("Zombies soon surround you just outside the front door and begin eating your face off.")
        return 'deadly'
        # Zombie hoard smells fresh meat and eats your face off

class Outside_2(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("These Zombies are no match for you and your shotgun. Right?")
        input(">>>")
        print ("Until they outnumbered you 1000 to 1... Your face = eaten off.")
        print ("I guess there were more Zombies outside than you had realized.")
        return 'deadly'
    # You shoot 3 Zombies before being overtaken by the hoard, face eaten off

class Shoot_Pilot(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("Awwww crap. You don't know how to fly a helicopter, do you?")
        print ("The good news: you survived the crash.")
        print ("The bad news: Zombies begin eating your face off on the ground.")
        return 'deadly'
    # You shoot creepy pilot, try to fly helicopter yourself, crash and burn, face eaten off


# happy ending
class Ending(Scene):
    def enter(self):
        print("\033c") # to clear the user's terminal window
        print ("The pilot lifts off with you in the back seat.")
        print ("Surprisingly his flying skills remain unimpaired despite his injuries.")
        print ("\nAnd thankfully he doesn't appear to be reanimating as a Zombie mid-flight.")
        print ("As he starts to touch down in a field inside a giant prison-like wall,")
        print ("you're not sure what to think.")
        print ("\nA swarm of troops approach the helicopter.")
        print ("They inform you of all that's happened and that you're now safe in a Zombie Outbreak camp.")
        print ("'Happy'... meet 'ending'")
        return 'ending'

class Map(object):

    scenes = {
    'room': Room(),
    'hallway': Hallway(),
    'lobby': Lobby(),
    'closet': Closet(),
    'roof': Roof(),
    'bathroom': Bathroom(),
    'elevator': Elevator(),
    'outside_1': Outside_1(),
    'outside_2': Outside_2(),
    'shoot_pilot':Shoot_Pilot(),
    'deadly': Deadly(),
    'ending':Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)


def SplashScreen(f):
    print ("\033c")
    open_f = open(f)
    print (open_f.read())
    print (input("Press ENTER key to begin\n>>>"))

SplashScreen(file_1)

first_scene = Map('room')
game = Engine(first_scene)
game.play()

"""
6) Hospital roof: Set off flares to attract helicopter's attention in hopes of being rescued. Shoot scary pilot and steal helicopter <crash>, or trust pilot not to kill you
7) Happy ending
"""
