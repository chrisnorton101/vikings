from sys import exit
from random import randint

chest_inventory = ['Bow and Arrow', 'Slingshot', 'Knife']
player_inventory = []


class Scene(object):

    def enter(self):
        print "This scene is not yet configured."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quotes = [
    "Never walk away from home ahead of your axe and sword.",
    "No lamb for the lazy wolf, no battles won in bed.",
    "A man is better blind than buried. A dead man is deft at nothing.",
    "Only your kin will proudly carve a memorial at the main gate.",
    ]

    def enter(self):
        print Death.quotes[randint(0, len(self.quotes)-1)]
        exit(1)

class Keep(Scene):

    def enter(self):
        print "You're Filip Halstensson, you are the son of famed Gotaland"
        print "king, King Halsten. However trouble is brewing here."
        print "You're uncle has always shown disgust that you're father"
        print "was king and not himself. He has always been very vocal"
        print "in his protests. However you never thought your uncle would"
        print "go so far. As you headed into the Keep, you could sense a"
        print "quietness about it. That was when you found him lying there."
        print "Your father was lying on his side with a gaping wound coming"
        print "from his abdominal. He knew he was not long for this world."
        print "\n"
        print "My son, you know I have always wanted nothing but the best"
        print "for you. You must know that this was the work of your uncle."
        print "It is up to you to revenge my name. By Odin himself you will"
        print "be guided. Go, you must find a weapon capable of destroying"
        print "Inge. For when we meet in Val Halla son. I love you."
        print "\n"
        print "Seeing your father lying there in a pool of his own blood"
        print "has awoken something inside of you. You feel overcome."
        print "As your lust for revenge grows, you must keep an even head."
        print "You must decide what steps to take to ensure revenge."
        print "Where is it that you decide to go?"
        print "The Forest"
        print "The Shipwreck"
        print "The Blacksmith"

        action = raw_input("> ")

        if action == "The Forest":
            print "You decide to venture off into the forest. Who knows what"
            print "is lurking there at this time of night."
            return 'forest'
            next_scene_name.enter(Forest)

        elif action == "The Shipwreck":
            print "You decide to venture off to the shipwreck that sits"
            print "off the coast. What is it you're hoping to find?"
            return 'ShipWreck'

        elif action == "The Blacksmith":
            print "You decide to venture off to the Blacksmith."
            print "Maybe there is something there you can craft to get your revenge."
            return 'BlackSmith'

        else:
            print "Maybe some other time."
            return 'Keep'


class Forest(Scene):

    def enter(self):
        print "As you enter the forest you feel an uneasiness about you."
        print "You see a bright light coming from a tree. As the moon is all but"
        print "hidden by the dark sky this seems peculiar. Your interest is"
        print "peaked and you decide to walk over to investigate the strange"
        print "light. As you approach you hear a strange voice, as though"
        print "whispered by the wind. No doubt a sign of the Gods."
        print "Coming into view you see a chest. Perhaps there is something of"
        print "use inside the chest. The chest creaks as you open it."
        print "Inside of the chest is: %s" % chest_inventory
        print "You only have room for one item. Which would you like to choose?"
        weapon = raw_input("> ")
        chest_inventory.remove(weapon)
        player_inventory.append(weapon)
        print "You chose the %s" % weapon


class ShipWreck(Scene):

    def enter(self):
        pass

class BlackSmith(Scene):

    def enter(self):
        pass

class Finished(Scene):

    def enter(self):
        print "You won! You are victorious!"
        return 'finished'

class Map(object):

    scenes = {
        'keep': Keep(),
        'forest': Forest(),
        'blacksmith': BlackSmith(),
        'shipwreck': ShipWreck(),
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




a_map = Map('keep')
a_game = Engine(a_map)
a_game.play()
