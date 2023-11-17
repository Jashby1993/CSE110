import time

#typewriter effect?
def type_writer_effect(text, delay=0.035):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def printt(*args):
    for arg in args:
        if isinstance(arg, str):
            type_writer_effect(arg, delay=0.035)
        else:
            print(arg, end='', flush=True)
    print()



def start_story():
    printt("You blink, and suddenly you're somewhere else. It's cold, you can see your breath.")
    printt("It's dark and cloudy, no moon or stars in sight. Clouds above, and a fog rolling in, enveloping you.")
    printt("Confused, but with no other options, you walk forward. Up ahead, some distance away, you see the entrance to a hedge maze. ")
    printt("As you enter the maze, you see a path to your LEFT, to your RIGHT, and STRAIGHT ahead.")
    
def make_choice(choices):
    while True:
        printt("What do you choose?  ")
        for choice in choices:
            if choice == "AWAKE":
                printt(f"- ")
            else:
                printt(f"- {choice}")

        user_input = input("Enter your choice: ").strip().upper()

        if user_input in choices or user_input == "AWAKE":
            return user_input
        else:
            printt("Invalid choice. Please enter one of the specified options.")

def main():
    start_story()
    choices_1 = ["LEFT", "RIGHT", "STRAIGHT", "AWAKE"]
    user_choice_1 = make_choice(choices_1).upper()

    if user_choice_1 == "LEFT":
        #narrative
        printt("You chose to go LEFT.")
        printt("You continue walking, taking turn after turn after turn, but without any other forks in the road.")
        printt('After what seems like hours, you see the exit from the maze. You think to yourself, "What kind of maze only has one choice in the beginning?')
        printt("As you exit the maze, you're on the road to what looks like a dense forest. What little light filters through the dense canopy \nhas a distinct green tint. This place seems so...alive.")
        printt("In the distance, you hear a growl, and you see a brown blur. You look around, and you see a shotgun propped against the tree.")
        printt("A split second later, you see a grizzly bear, obviously agitated, poised to charge.")
        printt("Do you GRAB GUN, STAND YOUR GROUND, or RUN AWAY?")
            
        #first bear choice
        choices_2 = ["GRAB GUN", "STAND YOUR GROUND", "RUN AWAY", "AWAKE"]
        user_choice_2 = make_choice(choices_2).upper()

        if user_choice_2 == "GRAB GUN":
            #narrative
            printt("In a panic you GRAB GUN, take aim at the grizzly bear, and... click.")
            printt("It's not loaded. You're pointing a useless unloaded gun at the grizzly bear, and it begins to charge.")
            printt("You panic, and you turn to run. You sprint through the forest at a breakeck pace, jumping over logs, dodging around roots until...")
            printt("You fall. Your foot catches on a gnarled root, and you come crashing to the ground, painfully.")
            printt("You're prone on the ground, and everything hurts, but worse than the pain is the certainty that your human experience is at an end.")
            printt("You brace for jaws and claws, but... it doesn't come. One second, two seconds, 10 seconds, nothing.")
            printt("You open your eyes, which you just realize were clenched tight. You look up, and the bear is there, tall on it's hind legs, looking at you.")
            printt("The bear ambles away. You can't belive your luck. You see a trail through the forest nearby on your right, leading to a bridge over the raging\n river winding around to your left.")
            printt("As you think about which way to go, you see two wide eyes gleaming from beneath the bridge. You stand up, brush yourself off,\n and call out, grateful assistance was nearby.")
            printt("A figure shuffles out from the shadows, and you see that wow, that's quite a large fellow.")
            printt(" Except then the eyes keep going higher, and the figure steps into the light. It's a gargantuan TROLL! Green scaly skin, ape-like\n arms, long, greasy hair in patches across it's body, and FAT, with an enormous belly.")
            printt("Once again, you brace yourself, and look around for options. Nearby, you see an actual SWORD, albeit an incredibly rusty one.")
            printt("On your other side, you see a few scattered GOLD COINS amid the underbrush. Or maybe... do you just TALK to him?")

            #third choice
            choices_3 = ["SWORD", "GOLD COINS", "TALK", "AWAKE"]
            user_choice_3 = make_choice(choices_3).upper()

            #first troll choice
            if user_choice_3 == "GOLD COINS":
                #narrative
                printt("You scrabble to dig through the leaves to find these scattered coins. Thoughts race through your mind: Will this work? Is the troll \ninterested in gold? Will you be able to keep some for yourself?")
                printt("The troll picks up his club, and charges toward you. You immediately fall to your knees, extending the gold coins in your cupped hands,\noffering them in exchange for your life.")
                printt("The troll pauses, intrigued by your offering, once bloodthirsty eyes now glinting with greed. He reaches out, and snatches the gold coins.")
                printt("Then he nods at you and turns away, satisfied with the business transaction.")
                printt("As he starts to walk back towards the bridge, you eye the gold with longing. You didn't have time to hide any for yourself.")
                printt("He shoots a gloating look over his shoulder, looks you square in the eye, and flips a coin towards you.")
                printt("Surprised, you catch the coin, the glinting gold holding your attention for a moment. When you look up again, to your surprise,\n the troll is gone! You look around in confusion, and in it's place you see a tiny figure.")
                printt("About two and a half feet tall, but with enormous, hairy, bare feet, and wearing a glowing blue amulet. 'Thank you for your patronage!' he called.")
                printt("Tricked! This, this, this MIDGET tricked you! You start for the sword to get that gold back and make that trickster pay, AND")

                #starting over!
                main()
            
            #2nd troll choice
            elif user_choice_3 == "SWORD":
                printt("As the troll approaches warily, you glance at the sword. It may be rusty, but it's still dangerous. Right?")
                printt("The troll sees your glance, notices the sword, and starts shambling faster towards you. You make a mad dash for the sword, not knowing what you'll\ndo if you actually get it in your hands.")
                printt("With the troll coming quickly, you reach down, grab the sword and... drop it. That is a LOT heavier than it looks. You pick it up again,\nthis time holding on for dear life. The pointy bit (Blade? Yeah, Blade) hovers precariously close to the ground.")
                printt("You heft the sword, and make as menacing a posture as you can manage. The troll, without stopping, looks at you, reaches up, and rips a \nlarge branch from the tree above him, then snaps it off when it starts getting thin. Great, now he's armed. ")
                printt("You hold your ground, and the trolls lumbering gait slow, evaluating. After a moment, you see what could almost be a condescending smile as he notes\nyour posture and difficulty holding the sword.")
                printt("Terrified, but commited to your decision, you decide that the best you can do is engage with surprise on your side. You take a step back, making it \nlook like you're losing courage (can't lose what you never had!) and then...CHARGE!!")
                printt("You run as fast as you can towards the troll. He WAS surprised, but not for as long as you hoped, because after just a moment he's swinging what's \nreally a fair sized tree at you. You manage to duck underneath the swing and avoid the blow, and you swing\n your own weapon in a mad attempt at attack, somehow managing to be less grateful than a troll \nswinging a tree, but your sword lands a blow! You don't know who's face looks more surprised,\n yours or the troll's. You pull the sword from the new gash in the grotesque leg and make another\n mad slash at the trolls general direction,  just wanting to hit anything. You're so close, the \ntroll is having trouble using the club, so he drops it and grabs towards you with enormous hands.\n Your mad slash manages another gash, this time on the overstuffed belly.  It looks \npainful, but nothing near a finishing blow. The troll grabs you, his hand wrapping all \nthe way around your shoulder, and he lifts and throws you several feet. You fall, rolling painfully\n several feet across rocks and brush. You feel your fear disappearing,\n replaced with blind anger. Instead of running away, which sounded tempting just moments ago, \nyou run, unarmed, towards the injured troll. He swings at you with a closed fist, but\n you duck, grab the fallen sword, point it upwards, and make a blind thrust UP with all \nyour might. You have hopes of ENDING this fight, this THREAT to whoever\n else might travel this way, and then") 
                #starting over!
                main()

            #3rd troll choice
            elif user_choice_3 == "RUN AWAY":
                printt("You turn and sprint away from the troll as fast as your legs can carry you.")
                printt("The troll roars in frustration behind you, but you don't look back.")
                printt("As you race through the dense forest, you start to feel a strange tingling on the back of your neck.")
                printt("Suddenly, the ground beneath you gives way, and you find yourself falling into a hidden pit.")
                printt("You land with a thud at the bottom, surrounded by darkness.")
                printt("As your eyes adjust to the dim light, you realize you're not alone.")
                printt("Glowing eyes stare at you from the shadows, and eerie whispers fill the air.")
                printt("Before you can react, a mysterious figure steps forward, shrouded in darkness.")
                printt("They speak in a low, menacing voice, 'Running away won't save you. You've entered a realm beyond imagination.'")
                printt("You feel a piercing pain in your back, and a burning sensations spreads through you, and then")
                main()
        
        #2nd bear choice
        if user_choice_2 == "RUN AWAY":
            printt("As soon as you see the bear, you spin around and BOLT. You run as you've never run before. You feel the \nadrenaline pumping through you. You race through")
            printt("the forest, dodging roots and brush and trunks. As fast as you're going, you're tiring. You can't maintain")
            printt("this sprint forever. You take a quick glance back, and you managed to outpace the bear, for now, but you don't dare stop.")
            printt("You see lots of places to hide, but you don't trust that you could hide from that nose for long.")
            printt("You don't know what else to do except keep running, but you're tiring quick, your legs are burning, your LUNGS are burning.")
            printt("You look back, and see that you've slowed or the bear sped up, either way, it's gaining.")
            printt("You look ahead, just in time to see a precipice in front of you. You don't try to stop, because of\na certain large animal, but you try to change direction.")
            printt("You are not successfull. You slip in some mud, and you go tumbling down the sharp decline. You land at the bottom,\nhard, and the breath is knocked out of you.")
            printt("You lay there for a moment, dazed, struggling to breathe. That HURT. You look above you, and the bear is at the top,\napparently looking for a way down, but unable to find an easy way down,\nlumbers off to go eat someone else, presumably.")
            printt("You get up, painfully, and brush yourself off, painfully. Grateful to not be eaten by a bear, but less\nthan grateful for your mode of escape, you start walking in a direction OPPOSITE where\nyou last saw the bear.")
            printt("As you limp through the forest, you start to notice crude markings, maybe drawings on the tree, though\nnone of these scratched or painted designs is over 2 feet above the ground.")
            printt("You continue onward, aimlessly, for some time. It's getting dark, you need shelter. Then, in the distance,\nyou see smoke! Smoke means people, warmth, shelter, food, all of which you desperately need.")
            printt("As you move towards the smoke, you start hearing strange noises. Hooting, howling, shouting, oddly high pitched grunting;\nand you begin to approach more cautiosly.")
            printt("With darkness falling and desperation rising, you continue onward, cautiously, if only to see how close the danger is.")
            printt("You approach slowly, and from the treeline, you encounter a bizarre sight. You find a primitive encampment full of\nthree foot tall...things. Green, large black eyes, pointed ears almost as long\nas they are tall. And all of them that you can see are armed.")
            printt("Most have clubs, but you see some with spears, and even a few with short blades, probably scavenged daggers.")
            printt("You don't really want to get involved, because they don't seem to like EACH OTHER, let alone an outsider.")
            printt("You scan the area. It looks like you could SNEAK through the forest, staying within the treeline. Looking up,\nyou see a beehive. That looks like it could make a good distraction if you manage\nto knock it down.")
            printt("You also see what appears to be a pile of discarded weapons. You don't feel up to a fight, but if you grabbed some\nof those, looked big and made a lot of noise, you could INTIMIDATE them, they could back down.")
            printt("They're all little, right?")

            #goblin choices
            choices_3 = ["SNEAK", "DISTRACT", "INTIMIDATE", "AWAKE"]
            user_choice_3 = make_choice(choices_3).upper()

            if user_choice_3 == "DISTRACT":
                printt("Careful not to draw attention to yourself, you grab a nearby stone, take careful aim, and launch your projectile\nat the beehive with all your might. And you")
                printt("miss. By a lot. You watch on in horror as the rock sails towards a goblin on the outskirts, and clocks him right in the head. ")
                printt("You jump to hide behind the tree. The goblin you inadvertantly hit looks around in confusion, bellowing in anger.")
                printt("Suddenly, he barrels in your direction, and you freeze in terror. Then suddenly, he punches another goblin square in\nthe jaw, apparently having blamed him for the attack.")
                printt("The bewildered fellow quickly shakes of his bewilderment and becomes enraged, gesturing to some of his companions, who\nstart grabbing their weapons of choice. The goblin you hit")
                printt("continues bellowing and gesturing wildly, and some of his companions start picking up their weapons, and calling frinds\ntheir own. Soon, the entire camp has split down the middle, all armed and angry.")
                printt("Intrigued, you want to stick around to watch the outcome, but you think it better to use THIS distraction to move\nthrough the forest around the camp.")
                printt("Behind you, you hear the fight break out, with shouts of pain and anger and victory, but you keep moving ahead towards\na narrow path in front of you.")
                printt("You're just about to the path, when you look up. Up in the trees, watching you with gloating, greedy, menacing grins, are\nmore goblins, who were NOT caught up in your distraction.")
                printt("Panicking, you get ready to run. You see one behind you heft a small spear. You sprint, despite the pain, but you feel\na sharp stabbing pain in your back between your ribs and then")
                main()

            elif user_choice_3 == 


#playing the game
main()
