from sys import exit
from random import randint

places_inventory = []
chest_inventory = ['Bow and Arrow', 'Slingshot', 'Knife']
player_inventory = {'Gold': 10}
weapon_inventory = []
ship_treasure = ['Great Sword']
blacksmith_inventory = ['Viking Great Sword', 'Crowbar']
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


## variable that asks where the player wants to go

class ChoiceSelector(Scene):

    def enter(self):
        print "Where would you like to go?"
        print "Keep"
        print "Forest"
        print "Blacksmith"
        print "Shipwreck"
        print "Uncles House"
        choice = raw_input("> ")
        if choice == "Keep" and "Keep" in places_inventory:
            print "You've already found everything there is to find in the Keep."
            print "It's best to get continue your journey elsewhere."
            return 'choice_selector'

        elif choice == "Keep"
            return 'keep2'

        elif choice == "Forest" and 'Forest2' in places_inventory:
            print "You think about going to the forest, but there is nothing"
            print "left so see in the forest. Besides you have other"
            print "business to attend to."
            return 'choice_selector'

        elif choice == "Forest" and 'Forest' in places_inventory:
            return 'forest2'


        elif choice == "Forest":
            return 'forest'

        elif choice == "Blacksmith" and "Blacksmith" in places_inventory:
            print "There's nothing left to do there. You've got other matters"
            print "to attend to."
            return 'choice_selector'

        elif choice == "Blacksmith":
            return 'blacksmith'

        elif choice == "Shipwreck" and "Great Sword" in weapon_inventory:
            print "You already got everything of value from there."
            print "Besides, you've got other matters to attend to."
            return 'choice_selector'

        elif choice == "Shipwreck" and 'Shipwreck' in places_inventory:
            return 'shipwreck2'

        elif choice == "Shipwreck":
            return 'shipwreck'

        elif choice == "Uncles House":
            return 'uncles_house'

        else:
            print "You can't do that right now."
            return 'choice_selector'

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
        print "Uncles House"
        print "Explore the Keep"

        action = raw_input("> ")

        if action == "The Forest":
            print "You decide to venture off into the forest. Who knows what"
            print "is lurking there at this time of night."
            return 'forest'

        elif action == "The Shipwreck":
            print "You decide to venture off to the shipwreck that sits"
            print "off the coast. What is it you're hoping to find?"
            return 'shipwreck'

        elif action == "The Blacksmith":
            print "You decide to venture off to the Blacksmith."
            print "Maybe there is something there you can craft to get your revenge."
            return 'blacksmith'

        elif action == "Uncles House":
            print "You have no time for pondering, you are going to go there"
            print "right now!"
            return 'uncles_house'

        elif action == "Explore the Keep":
            return 'keep2'

        else:
            print "You are undone by your lack of decision making."
            print "While you're pondering your decision, your uncle sneaks up"
            print "behind you and swiftly strikes you in the back."
            print "He didn't want to take any chances you would take the throne."
            print "\n"
            return 'death'


class Keep2(Scene):

    def enter(self):
        places_inventory.append('Keep')
        print "You catch yourself expecting to see your father"
        print "as you always had. That expectation quickly dissipated at the"
        print "sight of the blood stain on the ground."
        print "You're not entirely sure what you came here hoping to find."
        print "However you decide to take a look around."
        print "You see the entrance to the Bedroom in the back."
        print "There's also the Storage Closet."
        return 'bedroom'

class Bedroom(Scene):

    def enter(self):
        places_inventory.append('Bedroom')
        print "You step into the bedroom and look around. The fuel for revenge"
        print "grows stronger within you as you think about your father's"
        print "premature demise. It wasn't by the Gods, it was by the hands"
        print "of your uncle. You begin to look around."
        print "As you continue walking the room you see something just sticking"
        print "out underneath the bed. Upon closer inspection you find a key."
        print "You take the key just in case it comes in handy."
        player_inventory['Key'] = 1
        print "You check to see if the key fits the front door of the Keep."
        print "The key does not work though. Who knows what it's for."
        print "You continue on towards the storage closet."
        return 'storage_closet'

class StorageCloset(Scene):

    def enter(self):
        places_inventory.append('Storage Closet')
        print "You walk into the storage closet, there's all kinds of different"
        print "foods inside. There's not much else of interest in the closet."
        print "There is a hall exit to the left and the right."
        print "Which way would you like to leave?"
        print "Right"
        print "Left"
        choice = raw_input("> ")
        if choice == "Right":
            print "You turn to walk down the corridor. As you walk something"
            print "out of the corner of your eye catches your attention."
            print "It's glistening in the light. As you walk towards it you"
            print "make out what it is. It's a small pearl."
            print "You place the pearl in your pocket."
            player_inventory['Pearl'] = 1
            print "You head out into the night sky."
            print "You're satisfied with what you have found here. You decide"
            print "to continue on with your journey."
            return 'choice_selector'
        else:
            print "You Turn to walk down the corridor. You appear into the night"
            print "sky. You must continue on your journey."
            return 'choice_selector'

class Forest(Scene):

    def enter(self):
        places_inventory.append("Forest")
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
        choice = raw_input("> ")
        if choice == "Bow and Arrow":
            weapon_inventory.append(chest_inventory.pop(chest_inventory.index("Bow and Arrow")))
            print "You have %s" % weapon_inventory
            print "The chest has %s" % chest_inventory

        elif choice == "Slingshot":
            weapon_inventory.append(chest_inventory.pop(chest_inventory.index("Slingshot")))
            print "You have %s" % weapon_inventory
            print "The chest has %s" % chest_inventory

        elif choice == "Knife":
            weapon_inventory.append(chest_inventory.pop(chest_inventory.index("Knife")))
            print "You have %s" % weapon_inventory
            print "The chest has %s" % chest_inventory
        else:
            print "Sorry"

        # print "Alright you now have the %s." % weapon_inventory
        # print "%s are still inside the chest." % chest_inventory
        print "You've found all you can."
        return 'choice_selector'

class Forest2(Scene):

    def enter(self):
        places_inventory.append("Forest2")
        print "You arrive back at the forest."
        print "You return to the spot where you found the chest before."
        print "However it looks like the chest is gone."
        print "You wander around looking for it but it appears to be lost"
        print "for good. You hear in the distance some rustling of the leaves."
        print "Do you want to go take a look?"
        action = raw_input("> ")
        if action == "Yes":
            print "You sneak over towards the sound of the noise. It seems to"
            print "be growing louder. It sounds like a group of men."
            print "As you step closer you see the light of a fire appear behind"
            print "a group of bushes."
            print "You step on a branch and it makes a loud cracking noise."
            print "You hear voices stir from the campfire as they make their way"
            print "towards you. They're just about on top of you"
            print "You recognize them as friends of your uncle"
            print "and quickly realize they are not going to be in a talking"
            print "mood. You count quickly, there are 4 of them coming this way"
            print "You need to think fast."
            print "They spot you and immediately draw axes from their belts."
            if "Bow and Arrow" in weapon_inventory:
                print "You draw the Bow from the holster on your back."
                print "You fire without giving the brute in the front time to"
                print "react. You pierce him right through the throat with an arrow."
                print "One down, three to go you think to yourself."
                print "At this point they've started to seperate to flank you."
                print "You get a glimpse of one rounding a tree to your left."
                print "You flee the bush you were behind to get a better angle"
                print "on him. As you steady your weapon you hear a grunt from"
                print "behind. One lunges at you. You turn around just in time"
                print "to stab him through the heart with an arrow."
                print "As he falls to the ground you continue running."
                print "Not out of fear though. They other two seemed to have lost"
                print "track of you in the dense brush. You use this to your"
                print "advantage and circle bac kto the campfire. They will"
                print "never have expected that. You see one of the last two men"
                print "circling your last known position. You draw the Bow back,"
                print "take a deep breath and release. The arrow pierces through"
                print "the night and takes another victim. One more out there."
                print "you stay a little while near the fire hunkered behind a"
                print "tree, waiting for the last to return. However after a"
                print "while you realize he might not be coming back. You decide"
                print "This may be for the best, your uncle can take the lone"
                print "survivor as a sign that you're coming for him, and"
                print "you decide to head out of the forest."
                return 'choice_selector'


            elif "Knife" in weapon_inventory:
                print "You take out your knife you found from the chest earlier."
                print "As the men close in on you, you take a look at your knife."
                print "Not much to protect yourself with, but it must do."
                print "Two men are coming straight at you, the other two are"
                print "flanking you from either side. The first man raises his"
                print "axe, you have no choice as to dodge, as your knife would"
                print "do little in terms of protection. You dodge to the left"
                print "and the man flies past. The man flanking from the left"
                print "starts to swing. Before he has time, you stab him right"
                print "through the gut, dropping him tothe ground. The second"
                print "man coming directly at you has reached his destination."
                print "Axe high he swings down as you are pulling your knife"
                print "from the downed viking. With no time to move, you are"
                print "struck square on the shoulder. You fall to the ground."
                print "You feel the blood trickling out as a cool breeze"
                print "seems to come over you. You try to keep your eyes open."
                print "As you look up, you see something, no someone, coming"
                print "towards you. It cannot be, this can't be your time."
                print "But it is. As Odin the All-Father comes for you, you"
                print "close your eyes one last time."
                return 'death'



            elif "Great Sword" in weapon_inventory:
                print "You pull out the Great Sword you found earlier at the"
                print "shipwreck. A slight smile sneaks forth as you see the"
                print "blade glisten in the moonlight. Now is a better time"
                print "than ever to test this blade. As the men close in on"
                print "your position, you ready yourself. Two are coming"
                print "straight at you, the other two are flanking you from"
                print "either side. The first man in front raises his axe,"
                print "ready to swing down upon you. You quickly raise"
                print "your blade and deflect the blow, while slicing down"
                print "into his stomach. He lets out a moan as he falls to the"
                print "ground. The second man was close behind. He swings for"
                print "your weak side. You lunge forward to dodge the attack."
                print "As you spin around you see one of the flanking men"
                print "running full speed at you, axe raised. You quickly duck"
                print "under and with a powerful upwards swing knock the man"
                print "off of his feet. You quickly pierce down through the man's"
                print "chest to finish him off. That's two down, two to go,"
                print "you think to yourself. As you look for the two remaining"
                print "men you see only one. He has regained control after"
                print "running past you. He takes a deep breath and walks slowly"
                print "towards you this time. You keep your eyes peeled waiting"
                print "for the other man to show himself, but he never does."
                print "You take care of the last man swiftly. With one left"
                print "alive you decide that may be for the best, your uncle"
                print "can take the lone survivor as a sign that you're coming"
                print "for him and you decide to head out of the forest."

            else:
                print "You pull out your Slingshot. You find a good stone on"
                print "the ground and ready it in the sling. As they move on"
                print "you, you pull back and fire at the first man in vision."
                print "The stone hits him and bounces off. The man flinches and"
                print "keeps coming. The other three are looping around to flank"
                print "You. The man in front reaches you and you dodge his"
                print "first attack and hit him upside the head. He stutters"
                print "and prepares to swing his axe again. You're ready"
                print "for it and you duck the blow, swinging your leg and"
                print "knocking him to the ground. You take his axe and"
                print "swing down, tearing through his chest. At this moment"
                print "two of the others have flanked you. One comes from behind"
                print "and grabs you. The other charges from the flank and"
                print "hits you in the side as you try to absorb the blow."
                print "You feel the blood trickling out, as a cool breeze"
                print "seems to come over you. You fall to the ground as you"
                print "are released from the hold of the other man."
                print "As you look up you see something, no, someone coming"
                print "towards you. It cannot be, this can't be your time."
                print "But it is. As Odin the All-Father comes for you, you"
                print "close your eyes one last time."
                return 'death'


        elif action == "No":
            print "You've got better things to do and decide to move on."
            choice_selector()


class ShipWreck(Scene):

    def enter(self):
        places_inventory.append("Shipwreck")
        print "You arrive at the sight of a sunken vessel nudged up against the"
        print "cliff face. It had been here for as long as you could remember."
        print "You remember your father telling you stories of a great battle"
        print "that had been fought here many years ago."
        print "\n"
        print "An Earl from a nearby village had grown jealous of what Gotaland"
        print "had grown to. With nearly double the ports and ships than his own,"
        print "he decided that he was going to siege Gotaland when it was"
        print "least expected. As the boats sailed into the ports flying"
        print "their gold and black banners, the residents of Gotaland knew"
        print "there was trouble. Horns sounded and everyone was in action"
        print "preparing for the defense. However half of the greatest warriors"
        print "were off on a raiding party to the east. Despite the lack of"
        print "experienced warriors, Gotaland was able to hold off the attack."
        print "This was how your father had started his rise to power."
        print "He had been one of the main warriors that led the defense"
        print "despite having little prior experience."
        print "The shipwreck that remained was that of the Earl. It was kept in"
        print "in the port as a challenge. That anyone who dared come after"
        print "Gotaland, would end up like the last, sunken in the bay."
        print "\n"
        print "You had explored the wreck a little before. However you felt the"
        print "need to explore more, as this was such a sentiment to your father."
        print "You approached the top of the cliff face and jumped down on to"
        print "the bow. You walked to the far end and felt the floor creak"
        print "below you. For a second you thought that it was just due to the"
        print "wood being older than you and weathered. However, you noticed a"
        print "glistening coming between the slit of the wood, unlike the"
        print "surrounding boards. You kicked with your foot until you felt"
        print "the floorboard come loose. As you pried it open you realized"
        print "that not only was this board loose, but it started a chain"
        print "reaction. Multiple other boards came loose and as you worked to"
        print "remove them. You wondered what you were going to find."
        print "Peering down you realized it was a large secret compartment."
        print "Large enough to possibly hold a grown man, if it wasn't for the"
        print "wooden crate inside. You tried to pull the crate out, but it"
        print "seemed to be attached to the bottom of the boat. Your mind"
        print "swirled with the possibilities of what could be in there."
        print "You just needed to get the lid off."
        if 'Knife' in weapon_inventory or "Crowbar" in weapon_inventory:
            print "You must have something that you could use to try to pry the"
            print "lid open. You give it all you've got but there wasn't"
            print "so much as a budge."
            print "Just as you are about to give up hope, you hear creaking."
            print "A little piece snaps off of the lid. It gives you all you"
            print "need to break the rest of it off."
            print "Once the lid is off all you see is hay. However the crate was"
            print "much too heavy to be holding only hay. As you dig through"
            print "you feel the cool touch of a steel blade. You find the handle"
            print "and lift it out of the crate. THe blade is massive and seems"
            print "to still be quite sharp. There is something printed on the"
            print "hilt. Upon further inspection it reads:"
            print "EARL BALGRUF"
            print "With the etching of an eagle below."
            weapon_inventory.append(ship_treasure.pop(ship_treasure.index("Great Sword")))
            print weapon_inventory
            print "You search through the remainder of the crate but there is"
            print "nothing in comparison to the great sword. You backtrack to"
            print "the cliff face and decide to venture off."
            return 'choice_selector'

        else:
            print "You try to pry the crate open but there is nothing around"
            print "for you to use. If only you had something to pry open the"
            print "lid with. You take a further look around the ship but there"
            print "is nothing else of interest to you. You decide to head back"
            print "to the cliff face."
            return 'choice_selector'

class Shipwreck2(Scene):

    def enter(self):
        print "You find your way back to the boat in hopes of opening the chest."
        if 'Knife' in weapon_inventory or "Crowbar" in weapon_inventory:
            print "You must have something that you could use to try to pry the"
            print "lid open. You give it all you've got but there wasn't"
            print "so much as a budge."
            print "Just as you are about to give up hope, you hear creaking."
            print "A little piece snaps off of the lid. It gives you all you"
            print "need to break the rest of it off."
            print "Once the lid is off all you see is hay. However the crate was"
            print "much too heavy to be holding only hay. As you dig through"
            print "you feel the cool touch of a steel blade. You find the handle"
            print "and lift it out of the crate. THe blade is massive and seems"
            print "to still be quite sharp. There is something printed on the"
            print "hilt. Upon further inspection it reads:"
            print "EARL BALGRUF"
            print "With the etching of an eagle below."
            weapon_inventory.append(ship_treasure.pop(ship_treasure.index("Great Sword")))
            print weapon_inventory
            print "You search through the remainder of the crate but there is"
            print "nothing in comparison to the great sword. You backtrack to"
            print "the cliff face and decide to venture off."
            return 'choice_selector'

        else:
            print "You try to pry the crate open but there is nothing around"
            print "for you to use. If only you had something to pry open the"
            print "lid with. You take a further look around the ship but there"
            print "is nothing else of interest to you. You decide to head back"
            print "to the cliff face."
            return 'choice_selector'


class BlackSmith(Scene):

    def enter(self):
        places_inventory.append("Blacksmith")
        print "You arrive at the Blacksmith's shop."
        print "You gaze at the number of weapon and armaments inside."
        print "A man behind the counter asks if there is anything particular"
        print "you are looking for. You take a look at his wares."
        print "Viking Great Sword - 100 Gold"
        print "Crowbar - 10 Gold"
        print "Is there anything out of those you'd like? He asks."


class UnclesHouse(Scene):

    def enter(self):
        places_inventory.append("Uncles House")
        print "You walk up to your uncles house and anxiety draws over you."
        print "You take a deep breath and step up to the house."

        if 'Key' in player_inventory:
            print "The door is locked. However you found a key earlier."
            print "You place the key in and slowly turn the knob."
            print "You hear a click and the door lurches open."
            print "You take a deep breath. Are you sure you're ready to enter?"

        else:
            print "You walk up to the door, however the door is locked."
            print "Maybe if you had the key to open it you could get in."
            return 'choice_selector'


class Finished(Scene):

    def enter(self):
        print "You won! You are victorious!"
        return 'finished'

class Map(object):

    scenes = {
        'choice_selector': ChoiceSelector(),
        'keep': Keep(),
        'keep2': Keep2(),
        'bedroom': Bedroom(),
        'storage_closet': StorageCloset(),
        'forest': Forest(),
        'forest2': Forest2(),
        'blacksmith': BlackSmith(),
        'shipwreck': ShipWreck(),
        'shipwreck2': Shipwreck2(),
        'uncles_house': UnclesHouse(),
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
