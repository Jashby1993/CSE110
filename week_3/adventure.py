#Extras: Most endings loop back through the beginning, except for two hidden endings. There's a function that makes choice making consistent. And I imported time and made a function for a typewriter effect, instead of the instantaneous appearance.

import time

#typewriter effect?
def type_writer_effect(text, delay=1):
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
    printt("You blink, and suddenly you're somewhere else. You don't remember how you got here. \nIt's cold, you can see your breath.")
    printt("It's dark and cloudy, no moon or stars in sight. Clouds above, and a fog rolling in, enveloping you.")
    printt("Confused, but with no other options, you walk forward. Up ahead, some distance away, you see the entrance to a hedge maze. ")
    printt("As you enter the maze, you see a path to your LEFT, and to your RIGHT.")
    
def make_choice(choices):
    while True:
        printt("What do you choose?  ")
        for choice in choices:
            if choice == "WAKE UP" :
                printt(f"- ")
            elif choice == "ATTACK":
                printt(f"-")
            else:
                printt(f"- {choice}")

        user_input = input("Enter your choice: ").strip().upper()

        if user_input in choices or user_input == "AWAKE":
            return user_input
        else:
            printt("Invalid choice. Please enter one of the specified options.")

def main():
    start_story()
    choices_1 = ["LEFT", "RIGHT", "WAKE UP"]
    user_choice_1 = make_choice(choices_1).upper()

    
    #if user_choice_1 == "AWAKE":
        #printt("Suddenly, the world stops and fades to tones of grey. Just as suddenly, there's a hooded figure before you")
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
        choices_2 = ["GRAB GUN", "STAND YOUR GROUND", "RUN AWAY", "WAKE UP"]
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
            choices_3 = ["SWORD", "GOLD COINS", "FLEE", "WAKE UP"]
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
            elif user_choice_3 == "FLEE":
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
            printt("You scan the area.  Looking up,you see a beehive. That looks like it could make a good distraction if you manage\nto knock it down.")
            printt("You also see what appears to be a pile of discarded weapons. You don't feel up to a fight, but if you grabbed some\nof those, looked big and made a lot of noise, you could INTIMIDATE them, they could back down.")
            printt("They're all little, right?")

            #goblin choices
            choices_3 = [ "DISTRACT", "INTIMIDATE", "WAKE UP"]
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
            
            elif user_choice_3 == "INTIMIDATE":
                printt("Your hands close around a makeshift sword and a battered shield. Though your body protests every move, you muster the strength to \nstand, clutching the weapons. The goblins notice your emergence and cackle with glee, thinking they have an easy target.")
                printt("Summoning the last reserves of your strength, you stride purposefully toward the goblin camp, your eyes fixed on the nearest one. With \na menacing scowl, you swing the makeshift sword through the air, the metallic hiss cutting through the night.")
                printt("The goblins falter for a moment, their mirth turning to uncertainty. Taking advantage of their hesitation, you raise the battered shield high, \nits worn surface catching the flickering firelight. You growl, channeling every ounce of your determination into a fearsome glare.")
                printt("'Back off!' you snarl, your voice echoing through the night. 'I may be injured, but I won't hesitate to take you down with me!'")
                printt("The goblins exchange uneasy glances, their bravado wavering. Your desperate attempt at intimidation seems to be working. They inch backward, reassessing \nthe situation. With a final, authoritative swing of your makeshift weapon, you make a calculated step forward.")
                printt("The goblins, now thoroughly intimidated, scatter into the shadows, leaving you with a path to pass through their camp unharmed. Though your body aches and \nprotests, you've successfully bluffed your way past the goblin threat. As you hobble away, the echoes of your fierce display linger in\n the night, and you press on, grateful for the discarded weapons that helped you overcome the odds.")
                printt("You walk on through the forest, congratulatiosn in order. After how well that went, you confidence is definitely imrproving! You keep walking through the forest, and then")

                main()

            
        elif user_choice_2 == "STAND YOUR GROUND":
            printt("No where to run, no where to hide, and that gun isn't big enough for anything but making the bear")
            printt("angrier. You do what they said on Discovery Channel: you raise your arms and spread your legs to make")
            printt("yourself as large as possible, and you bellow and roar. Not to scare the bear exactly, but to make it seem you're")
            printt("bigger. The bear stops and looks at you. Is it working? You can't believe your luck. The bear turns around, and with one")
            printt("more look at you, he races away, obviously in a hurry. Was it you? Doesn't matter, you're not bear food.")
            printt("That thought lasts exactly 5.4 seconds, and then the relief quickly dissipates when you hear a terrible sound")
            printt("behind you. You can't believe your eyes. Flying towards you, like out of a movie, is a dragon. You start to")
            printt("run, but it's so fast, and you're already tired from walking for hours in the maze. Faster than you imagined possible,")
            printt("it's upon you, swooping down, and grasps you in it's claws, to take off again, vaulting back into the sky, off to some")
            printt("unknown destination. It's enormous, how does this thing even manage to fly? It's covered in scales, in a multitude")
            printt("of green and blue tones. It would be beautiful if you weren't hurtling hundreds of feet in the air against your will.")
            printt("It's squeezing you in it's massive talons, making it hard to move, to breathe, to think. The world goes dark...")
            printt("You wake up, which by itself is a relief. You look at your surroundings, you seem to be at the top of a mountain.")
            printt("Is this it's nest, it's lair? You assess what's around you. Lot's of bones. Lot's of BURNT bones, to be specific.")
            printt("Clearly this beast prefers to eat at home. Over to the right, you see a cave. Maybe a good place to HIDE until you can")
            printt("sneak away? Nearby, you see a corpse. It's sword is melted, but the surprisingly ornate SHIELD seems untouched. Can that defend you?")
            printt("On your other side, is a STAFF. It looks like little more than a carved walking stick, but you feel drawn towards it,")
            printt("for reasons you can't understand. You hear something, but you can't identify where the sound comes from. Is the dragon ")
            printt("on his way back? You need to choose soon.")

            #dragon choices
            choices_3 = ["HIDE", "STAFF", "SHEILD", "WAKE UP"]
            user_choice_3 = make_choice(choices_3).upper()

            if user_choice_3 =="HIDE":
                printt("Safe bet, you decide to go hide in that cave. You look around, don't see anything trying to")
                printt("eat you, and you head into the cave. A few steps in, your feet start sliding and clinking. You look down,")
                printt("and you see you're literally walking on piles of gold coins, even jewels. This is his hoard, you think.")
                printt("You barely have time to process that fact before you hear a low, rumbling growl. you turn, and the dragon is facing you,")
                printt("mouth open. It breaths in, breathes out, you see the flames rumbling towards you and")
                main()

            elif user_choice_3 == "STAFF":
                printt("You decide to follow that feeling of calling. You go to the staff and pick it up. It begins to glow. You feel...")
                printt("potential. You feel a potential energy you've never felt, something inside you waiting to be released.")
                printt("You don't have time to think, because the dragon is returning. You heft the staff, and you look inside yourself")
                printt("As the dragon flies above you, it sees you holding the staff and bellows in rage. It flies above you")
                printt("and unleashes billows of flames upon you. You focus your energies on the staff, and the flames are")
                printt("absorbed by the staff. You feel the energy flow into you, needing to be used. You let the energy rebound through")
                printt("you, back through the staff, and you hurl the energy back at the creature, focusing on COLD. A burst of intense")
                printt("cold catches the dragons wing and it comes tumbling to the ground. It clambers over to you, preparing it's flames. You hold the")
                printt("staff high. The flames are racing towards you, you're pulling energy into and through the staff, and")
                main()

            elif user_choice_3 == "SHEILD":
                printt("You pull the corpse's arm from the sheild. Everything around it is burned, but the sheild is untouched.")
                printt("There's obviously something special about the shield, but it's not a perfect defence. You strap it to your")
                printt("arm, and just in time, because the dragon comes lumbering out of the cave you had thought about hiding in!")
                printt("It spots you, and comes charging at you. It breathes in deep, and unleashes a torrent of flams at you. You duck behind")
                printt("the shield, and though the flames should hurt, they don't. Irked, the dragon charges towards you. It prepares it's")
                printt("fiery breath. You brace yourself behind your shield, awaiting the flames tht never come. The dragon has hooked")
                printt("it's tail around you, flips you in the air towards open jaws, and")
                main()
                       
    elif user_choice_1 == "RIGHT":
        printt("No option seems better than another, so you stride towards the right. The path is twisting, convoluted,")
        printt("but there's no other fork, no other path presenting itself. For what seems like hours, you do nothing")
        printt("but follow the path. Just you, the endless hedges, and the fog. It gives you time to think. Where")
        printt("are you, and how did you get here? What's on the other side. You were musing the possibilities,")
        printt("when you finally come to a fork. This time, three choices: left, right, straight. You're doing")
        printt("'eeney meeney miney mo' in your head to choose a path when you hear 'Lookey here, another one!'")
        printt("You look around, but you see no-one. 'Up here, landling!' You look up, but all you see is a pitch")
        printt("black raven, almost invisible in the darkness and fog. 'Yes, me. The bird' states the raven.")
        printt("'I've been watching you for some time now. Would you like to know the way out?' You nod eagerly.")
        printt("'Answer right my riddle, and I'll point you the way out of here. A wrong answer will get you a ")
        printt("wrong answer. Agreed?")
        printt("You've always been good at riddles, so you agree eagerly.")
        printt("Very well, I love a good sport. Your riddle is this: I can be cracked, made, told, and played. What am I?")
        printt("You think carefully. You can crack an EGG to make it... You love to play a JOKE... \nOooh, you can crack a CODE!")
        printt("This is a tough one, but you choose")
        #Raven's riddle
        choices_2 = ["EGG", "JOKE", "CODE", "WAKE UP"]
        user_choice_2 = make_choice(choices_2).upper()

        if user_choice_2 == "JOKE":
            printt("'HAHA, correct!' squawks the Raven. 'I thought I had you. Well done, a deal is a deal.'")
            printt("The Raven flapped it's wings and landed in the hedge next to you. 'A way out is that left there.")
            printt("'I will warn you, there are pitfalls in that direction. The way out may not be offered to you")
            printt("on a silver platter. Don't make the easy choice. In fact, I'll give you another right answer.'")
            printt("'ANY time you can make a choice, you can make the choice to leave. All you have to do is--'")
            printt("'BEGONE FOUL FOWL, you give too much!!' said a booming voice that seemed to resonate from everywhere.")
            printt("The raven immediately snapped it's beak shut. 'Sorry friend, he's probably right. Good luck!'")
            printt("And with that, the Raven abruptly flew away over the hedges. You think for a moment, and decide")
            printt("to take the left. Still no other clues as to what goes where, might as well listen to the riddling bird.")
            printt("The path starts winding again, but actually, it's getting brighter, and the fog is dissapating. And...")
            printt("THERE! In the distance! You see what looks to be the end of the maze!")
            printt("You sprint the rest of the way, grateful to be out of this dreary maze. You run onto what looks like ")
            printt("a wooden platform, when suddenly everything is moving. As soon as both feet were on the wood, the ground")
            printt("behind you fell away, and what appeared to be a distant mountain is now very much moving, and very much")
            printt("right in front of you. First you recognize a gargantuan arm, an enormous shoulder, and last a VERY ugly face.")
            printt("'WHO DARES DISTURB MY SUPPER!?!' He picks you up between two fingers and examines you. 'Bah, another wanderer'")
            printt("For disturbing my supper, the least you can do for me is entertain me. Let's play a game.")
            printt("The giant turned, and when he returned he was holding  3 cups")
            printt("'Two of these cups contain poisons, and one is safe. Drink the safe cup, and I'll take you to fairy land.'")
            printt("You look at the three cups, and nothing stands out. You see a BRASS GOBLET,\n a JEWELED CHALICE, and a plain wooden mug.")

            #Giants drink
            choices_3 = ["BRASS GOBLET", "JEWELED CHALICE", "WOODEN MUG", "WAKE UP", "ATTACK"]
            user_choice_3 == make_choice(choices_3)

            if user_choice_3 == "BRASS GOBLET":
                printt("With the giant looming over you, you step towards the brass goblet. \nIt's simple, but elegantly ornate, simple designs repeated in a fashion very ")
                printt("pleasing to the eye. The liquid within doesn't \nbubble or ripple like the others. It's completly still, surface flat as a mirror.")
                printt("The black liquid within could be distilled night, \ndistilled darkness. It's as dark and still as... on second thought, maybe it's better not to think to much about what it's like.")
                printt("You grab the enourmous goblet in both hands, and awkwardly manage to tip it towards you.")
                printt("It's viscous, like molasses. It slides towards \nyou, more than pours. You take a breath, and you slurp it up.")
                printt("You do manage to spill more on yourself than drink, \nbut that,s fine, let's get this over with. You set the goblet down, and wait.")
                printt("After a moment, your fingertips start tingling, Then \nthe sensation moves up your hands, your wrist. It's slightly painful, like pins and needles but so much worse.")
                printt("Then the cold starts. Moving up from your feet, it spreads. \nYou realize you're stuck, literal frost showing all across your body.")
                printt("You can't move. The giant roars with menacing laughter. Now you're encased in ice")
                printt("a statue, a trophy for this cruel giant. You're panicking, \nbut even your thoughts are slow in this cold. You try to break free and")
                main()

            elif user_choice_3 == "JEWELED CHALICE":
                printt("You reach for the jeweled chalice, enchanted by its \nshimmering gems and intricate carvings.")
                printt("As you lift it to your lips, the liquid inside sparkles like a \nthousand stars. It tastes sweet at first, a deceptive allure.")
                printt("Suddenly, the jewels on the chalice start glowing brighter, and a \nsearing heat courses through your veins.")
                printt("The sweetness turns to an unbearable burning sensation, and you collapse in agony.")
                printt("The giant, pleased with your suffering, watches as your body ignites \nfrom the inside, your whole being fading into ashes until")
                main()
            
            elif user_choice_3 == "WOODEN MUG":
                printt("Opting for the humble wooden mug, you appreciate its simplicity \ncompared to the other extravagant vessels.")
                printt("The liquid inside looks like a clear, refreshing water. As you\n take a cautious sip, a strange sensation creeps over you.")
                printt("Your body begins to convulse uncontrollably, and you feel an intense pressure building within.")
                printt("To your horror, small wooden tendrils sprout from your skin, intertwining with your muscles and bones.")
                printt("You're transforming into a wooden statue, frozen in a grotesque pose. The giant, amused by the sight,")
                printt("reaches over to pick you up and place you near his set of petrified victims. Just as his hand almost reaches you")
                main()

            elif user_choice_3 == "ATTACK":
                printt("Somehow, you know that none of those goblets are safe. None of this has been fair.")
                printt("You can see it in his ugly smug face; he's never letting you go. You pretend to examine the")
                printt("enormous cups, but take the time to examine your surroundings. You see strange wooden statues,")
                printt("in agonizing positions, and you realize that it's people, transformed into wood. You see")
                printt("burn marks across the table. Further down, you see withered what appears to be holes in the ")
                printt("enormous table, as if melted by acid. There's no way you're drinking from any of the cups.")
                printt("Anger starts boiling within you. But what to do? You look around nothing really obvious to arm yourself.")
                printt("But maybe... maybe you can beat him at his own game. Nearby, you see a helmut from a suit of armor.")
                printt("The beginnings of an idea are forming. You go to inspect the helmut, as if you want to distract yourself")
                printt("from this terrible situation. 'Time enough, now you CHOOSE' bellowed the giant, face contorting with impatience.")
                printt("You take the helmut with you, as if without thought. You go to the brass goblet, you inspect as if about")
                printt("to drink, then walk off, 'absent-mindedly' dunking the helmut in the dark liquid. You head towards the wooden")
                printt("wooden mug, and do the same thing. When the dark liquid meets the clear liquid, they turn a disconcerting yellow.")
                printt("You move faster, as the giant is clearly becoming agitated with your antics. 'DRINK!' he roars. You head")
                printt("the final cup, the jeweled chalice. Moving quickly, you abandon the ruse, and simply scoop up as much")
                printt("of the blue liquid as you can. The mixture is smoking and giving off an acrid smell and smoking. The giant")
                printt("is enraged with the turn of events, and screams in frustration. You're very worried, that's a big giant")
                printt("for not a lot of liquid, but there's no way you're drinking it. He's reaching towards you now, and you")
                printt("throw the liquid, helmut and all at the outstretched hand, and the results were surprising. As soon as ")
                printt("the liquid contacts the hand, it starts turning to crumbling stone. The giant howls in pain, looking")
                printt("at where a hand used to be. He grips the stump, and you notice he leans against the table, right")
                printt("next to the brass goblet. While he's distracted, you run to the goblet and heave. trying to be fast")
                printt("but also terrified to get a single drop on you. You HEAVE, and manage to tip the goblet, and the black")
                printt("liquid spills over the giants arm, frost immediately spreading, and fixing him in place. His arm flails,")
                printt("and knocks over the wooden goblet, luckily AWAY from you. He's ignoring you now in his panic, and you")
                printt("run to the final goblet and HEAVE again, now with a confidence that maybe you can survive this.")
                printt("The sparkling liquid flows down the table and onto the giant, and he bursts into flames.")
                printt("It looks so painful, you almost feel sorry for him, until you remember that this is what he")
                printt("planned for you. You don't think he's going to recover, but you don't wait around. You climb your way")
                printt("down the table, and you look in the direction the giant came from. It's time to find your way home.")
                printt("But maybe, we'll see if there's a giant's hoard of gold to pick through while we're looking.")

        
        elif user_choice_2 == "EGG":
            printt("'Very astute' says the raven, then makes a sound between a laugh and a caw. Very well,")
            printt("a deal is a deal.' The raven thinks for a moment, as if making a decision. 'The way you want to go, ")
            printt("is straight ahead.' That's the way you were going to pick anyways, excellent! 'Have fun' the raven")
            printt("cries, then flaps away without another word. You go straight ahead. As you walk, you think.")
            printt(f"{user_choice_2.capitalize()}s. I crack them. I make them. Wait, how do you tell the {user_choice_2.lower}? Can you play the {user_choice_2.lower()}... Suddenly you ")
            printt("about the raven's sincerity, which makes you feel a little crazy for having a conversation with an insincere")
            printt("bird. Before you can keep second guessing, you round a corner and abruptly hit a wall, with a large")
            printt("wooden door in the middle. You test it, and it's not locked, so you go through. It's dark inside. You take")
            printt("a few steps, and the door shuts abruptly, startling you. Suddenly, candles light and you can see your")
            printt("surroundings. You're in a stone room with vaulted ceilings. To your right, you see a way out of the room")
            printt("and back into the HEDGE MAZE. You take a shock as you look to your left, where stone platforms seem")
            printt("suspended in middair! And straight ahead, you see a relatively normal looking corridor, except for the")
            printt("suits of armor and bizzare statues that line both sides. Something feels...off about this place, menacing.")
            printt("You also feel like you shouldn't stay here long. Where will you go?")

            #trap room
            choices_3 = ["HEDGE MAZE", "FLOATING PLATFORMS", "STATUES", "WAKE UP"]
            user_choice_3 = make_choice(choices_3)

            if user_choice_3 == "HEDGE MAZE":
                printt("You opt to go back into the hedge maze. You step through the archway and")
                main()

            elif user_choice_3 == "FLOATING PLATFORMS":
                printt("You take a left, going to inspect the floating platforms. You push on the first one with your foot,")
                printt("and it doesn't budge. You ease your weight onto it, and it seems solid. You put your full weight onto it.")
                printt("No movement, solid as a mountain. You jump up and down, solid. Ok, you think, I can do this. You stride along,")
                printt("and then you look down. Immediate regret floods your mind, just as quick as the fear. Below you is nothing.")
                printt("Nothing. Not a distant floor. Just nothing. You pick your eyes up and keep moving. You see another platform ahead,")
                printt("separated by just a few inches. You test the platform, which is just a few inches narrower than the one you")
                printt("find yourself on now. You test it, still pretty solid. You make the step with little issue. But as soon as")
                printt("both feet are on the new platform, the previous platform evaporates. Not moves away, not descends, it simply PUFFS")
                printt("into smoke. So much for solid. And as you walk, you realize this platform isn't perfectly stable as the last.")
                printt("It has just a little give, like walking in an elevator. Can't jump back, it's too far. Nothing to do but move forward,")
                printt("but you feel panic rising as you begin to understand just what's happening. As you test the third platform, you nearly")
                printt("tumble off because the platform you're on evaporates when you put ONE foot on the next platform, and is smaller and")
                printt("slightly less stable than the last. You start moving faster. You keep going, no end in sight. Nothing in sight, really.")
                printt("No walls, no landmarks, just platforms and blackness. Each platform smaller and less stable than the last, and disappearing just")
                printt("a little earlier than the last. You start running. There's no warning before a platform disappears, just gone.")
                printt("Intuitively, you start jumping before you reach the end. The platforms aren't waiting for you to land, they disappear")
                printt("as you jump. You're terrified now, trying to run faster and faster on platforms that are increasingly unstable.")
                printt("And then the inevitable: you prepare yourself for the next jump, and your next step is through smoke and you find yourself")
                printt("falling, tumbling through blackness. The fear is incredible as you just keep falling. Then you see a floor, cold stone")
                printt("hurtling towards you. You brace for impact, and then")
                main()

            elif user_choice_3 == "STATUES":
                printt("Not trusting the impossible floating platforms, and reluctant to go through the maze again, you")
                printt("just walk down the corridor. You look at the statues as you go. The suits of armor are all armed:")
                printt("swords, lances, mauls, crossbows, sheilds, flails, pikes. The statues are all monstrous, cast in iron")
                printt("or bronze, all depicting terrors of varying sizes, some ogre or troll looking ones, and some tiny ones,")
                printt("no more than 8 inches with wings. The level of detail is incredible. you step forward to inspect one,")
                printt("and it moves! It only looks at you, but you jump back in fright, inadvertantly bumping into an suit of armor")
                printt("which, in turn, pushes you out of the way! It lifts a massive sword and cuts the gargoyle looking thing")
                printt("that was looking at you in half, sending bronze chunks everywhere. You realize that EVERYTHING in the corridor is")
                printt("starting to move. Nothing is paying attention to you though. The suits of armor taking their weapons and destroying")
                printt("the waking monsters, and the monsters in turn are trying to dismantle the suits of armor. In moments, it's a full")
                printt("battle ensuing in this large corridor. Suddenly, some of the monsters lock eyes on you and come running at you.")
                printt("You dash the other way, but they're soon dispatched by suits of armor with massive battle axes. You're relieved,")
                printt("but that's shortlived as the suits of armor who saved you now start swinging weapons at you! It's absolute")
                printt("pandemonium. You just keep running, then you trip over a discarded gauntlet and crash to the ground.")
                printt("You pick yourself up as quickly as you can, just in time to avoid a cyclop's club, you turn to run again, when")
                printt("you see a suit of armor level a crossbow at you. You see a bolt hurtling right towards your chest, you feel")
                printt("an impact, then pain and then")
                main()

        


    elif user_choice_1 or user_choice_2 or user_choice_3 == "WAKE UP":
        printt("Suddenly, the world stops and fades to tones of grey. Just as suddenly, there's a hooded figure before you.")
        printt('"Have you tired of our little game, have you?" he says in a deep, booming voice. Suddenly, this all seems familiar.')
        printt("'I've done this before. I've had this conversation before,' you think. How long have I been here? \nHow many times have I been through this?")
        printt('"I asked you a question," comes the booming voice again. "Are you done with our game?"')
        wake_up = input('"Do you want to wake up?," the voice continues."A simple YES or NO will suffice." ').upper()
        if wake_up == "NO":
            printt('"Delightful!" says the mysterious figure. "I was not quite finsihed toying with you."')
            printt("The world starts to spin, the colors returning, and becoming brighter, until everything seems\nbrighter than could possibly exist. Your head starts pounding and then")
            main()
        elif wake_up == "YES":
            printt("In the next moment, you open your eyes to find yourself lying in your bed. The soft glow of morning \nlight filters through your window, and the distant chirping of birds signals the \nbeginning of a new day. Sweat beads on your forehead as the remnants of the \ndream linger in your mind.")
            printt("The enchanted realm, the maze, the dragons, and the goblins—all of it was just a vivid dream. Yet, the \nemotions and memories are so vivid that for a moment, you question \nwhich reality is the true one.")
            printt('As you sit up and collect your thoughts, you realize that the choice to "WAKE UP" was an escape,\n a reset to the comfort of the familiar. The adventure may have been a dream, \nbut the lingering sense of wonder and excitement remains.')
            printt("As you ponder the dream and the choice you made, you can't help but wonder if the enchanted realm \nis still there, waiting for you to explore it again. The decision is yours—will \nyou dismiss it as a mere dream, or will you embrace the mystery and embark on a new journey?")
            printt("The room is quiet, and the possibilities are endless. Welcome back to reality. What will you do?")

#playing the game
main()
