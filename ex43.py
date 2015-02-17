from sys import exit
from random import randint

#Gothons from Planet Percal #25
#a small space adventure game

#"Aliens have invaded a space ship and our hero 
#has to go through a maze of rooms defeating them 
#so he can escape into an escape pod to the planet 
#below. The game will be more like a Zork or Adventure 
#type game with text outputs and funny ways to die. 
#The game will involve an engine that runs a map full 
#of rooms or scenes. Each room will print its own 
#description when the player enters it and then tell 
#the engine what room to run next out of the map."

class Scene(object):

    # this is the base class for all scenes
    # in this simple program it doesn't do much
    # is is more a demonstration of a base class.

    # in the following code, the function enter is defined but then
    # prints an explanation of its uselessness and exits

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # a_game.play() is called
    # current_scene is set to self.scene_map.opening_scene() which is at first CentralCorridor()
    # last_scene is set to self.scene_map.next_scene('finished') which makes it Finished()
    # while current_scene is not equal to last_scene, next_scene_name = current_scene.enter() with is CentralCorridor.enter()
    # current_scene is updated to be self.scene_map.next_scene() with next_scene_name as argument.
    # current_scene.enter() is run on CentralCorridor
    # CentralCorridor() returns laser_weapon_armory 
    # SO.... then what? laser_weapon_armory 

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene

        current_scene.enter()



class Death(Scene):
    # This is when the player dies and should be something funny.

    quips = [
        "You died. You're not very good at this.",
        "You died.",
        "You die. Is that the best you can do?",
        "You don't get out much do you."]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    #This is the starting point and has a Gothon already standing 
    #there they have to defeat with a joke before continuing.

    def enter(self):
        print """
        The Gothons of Planet Percal #25 have invaded your ship.
        You are the last remaining survivor.
        Your mission is to get the neutron bomb from the Weapons
        Armory, put it in the bridge, and blow up the ship.
        Don't forget to get into the escape pod before it blows up.
        """
        print "You need to make your way to the Armory."
        print "But the Gothon guarding the door sees you and draws his gun."

        action = raw_input("> ")

        if action == "shoot":
            print """
            Quick draw McGraw, you draw your blaster and fire away.
            But what's this? Your blaster rays are absorbed into his body!
            The Gothon laughs and shoots you.
            """
            return 'death'

        elif action == "123":
            print "CHEAT CODE DEPLOYED:"
            print "The bomb magically moves to the bridge and begins counting down"
            print "Time to get out of here!"
            return 'escape_pod'

        elif action == "tell a joke":
            print """
            You're a smart cookie and you know trying to shoot the Gothon 
            won't work. Only jokes will kill a Gothon!
            You say, "why did the chicken cross the road?
            The Gothon replies, "What?? How dare you....." 
            but quicker than lightning his head explodes.
            """
            return 'laser_weapon_armory'

        else:
            print "Come again?"
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    #This is where the hero gets a neutron bomb to blow up the ship 
    #before getting to the escape pod. It has a keypad the hero has 
    #to guess the number for.

    def enter(self):
        print """
        You dive roll into the Weapon Armory prepared to hurl jokes
        and any oncoming Gothons. You make a break for the far side
        of the room where the neutron bomb is locked. There is a keypad
        lock on the container. You have 10 tries to get the 3 number
        combination correct. Good luck!
        """

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print code
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            guesses +=1
            print "Try again. You have %d guesses left" % (10 - guesses)
            guess = raw_input("[keypad]> ")

        if guess == code:
            print """
            The code worked! You lift the bomb out and head for the door.
            """
            return 'the_bridge'

        else: 
            print "That was your last guess. The code locks forever."
            return "death"


class TheBridge(Scene):

    #Another battle scene with a Gothon where the hero places the bomb.

    def enter(self):
        print """
        You burst on the Bridge carrying your neutron booty.
        The Gothons see your bomb and know you mean business.
        Your move.
        """

        action = raw_input("> ")

        if action == "joke":
            print "'ha ha! ha ha ha!!!' say the Gothons and explode."

        else:
            print "Come again?"
            return 'the_bridge'

        print "You set the bomb down and arm it to detonate in 2 minutes"
        print "You turn and head for the escape pod"
        return 'escape_pod'


class EscapePod(Scene):

    #Where the hero escapes but only after guessing the right escape pod.

    def enter(self):
        print "You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "you jump into pod %s and hit the eject button" % guess
            print "the pod exploded instantly"
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod jetisons away from the ship just as it explodes."
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "you won!"
        return 'finished'

class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
    # what happens?
    # initiates a_Map as an instance of Map with 'central_corridor' as an argument
    # 'central_corridor' is the argument for def __init__, so self.start_scene = 'central_corridor'
    # def next_scene is run with 'central_corridor' as the argument, returning CentralCorridor()
    # def opening_scene is run with no additional arguments, using next_scene which uses start_scene
a_game = Engine(a_map)
    # a_game = Engine(a_map)
    # a_game instance of Engine object is created
    # it uses a_map as scene_map and does the __init__ thing on it

a_game.play()