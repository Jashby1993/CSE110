
def start_story():
    print("You blink, and suddenly you're somewhere else. It's cold, you can see your breath.")
    print("It's dark and cloudy, no moon or stars in sight. Clouds above, and a fog rolling in, enveloping you.")
    print("Confused, but with no other options, you walk forward. Up ahead, some distance away, you see the entrance to a hedge maze. ")
    print("As you enter the maze, you see a path to your LEFT, to your RIGHT, and STRAIGHT ahead.")
    
def make_choice(choices):
    while True:
        print("What do you choose?  ")
        for choice in choices:
            print(f"- {choice}")

        user_input = input("Enter your choice: ").strip().upper()

        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please enter one of the specified options.")

def main():
    start_story()

    choices_1 = ["LEFT", "RIGHT", "STRAIGHT", "AWAKE"]
    user_choice_1 = make_choice(choices_1).upper()

    if user_choice_1 == "LEFT":
        #narrative
        print("You chose to go LEFT.")
        print("You continue walking, taking turn after turn after turn, but without any other forks in the road.")
        print('After what seems like hours, you see the exit from the maze. You think to yourself, "What kind of maze only has one choice in the beginning?')
        print("As you exit the maze, you're on the road to what looks like a dense forest. What little light filters through the dense canopy \nhas a distinct green tint. This place seems so...alive.")
        print("In the distance, you hear a growl, and you see a brown blur. You look around, and you see a shotgun propped against the tree.")
        print("A split second later, you see a grizzly bear, obviously agitated, poised to charge.")
        print("Do you GRAB GUN, STAND YOUR GROUND, or RUN AWAY?")
         
        #second choice
        choices_2 = ["GRAB GUN", "STAND YOUR GROUND", "RUN AWAY", "AWAKE"]
        user_choice_2 = make_choice(choices_2).upper()

        if user_choice_2 == "GRAB GUN":
            #narrative
            print("In a panic you GRAB GUN, take aim at the grizzly bear, and... click.")
            print("It's not loaded. You're pointing a useless unloaded gun at the grizzly bear, and it begins to charge.")
            print("You panic, and you turn to run. You sprint through the forest at a breakeck pace, jumping over logs, dodging around roots until...")
            print("You fall. Your foot catches on a gnarled root, and you come crashing to the ground, painfully.")
            print("You're prone on the ground, and everything hurts, but worse than the pain is the certainty that your human experience is at an end.")
            print("You brace for jaws and claws, but... it doesn't come. One second, two seconds, 10 seconds, nothing.")
            print("You open your eyes, which you just realize were clenched tight. You look up, and the bear is there, tall on it's hind legs, looking at you.")
            print("The bear ambles away. You can't belive your luck. You see a trail through the forest nearby on your right, leading to a bridge over the raging\n river winding around to your left.")
            print("As you think about which way to go, you see two wide eyes gleaming from beneath the bridge. You stand up, brush yourself off,\n and call out, grateful assistance was nearby.")
            print("A figure shuffles out from the shadows, and you see that wow, that's quite a large fellow.")
            print(" Except then the eyes keep going higher, and the figure steps into the light. It's a gargantuan TROLL! Green scaly skin, ape-like\n arms, long, greasy hair in patches across it's body, and FAT, with an enormous belly.")
            print("Once again, you brace yourself, and look around for options. Nearby, you see an actual SWORD, albeit an incredibly rusty one.")
            print("On your other side, you see a few scattered GOLD COINS amid the underbrush. Or maybe... do you just TALK to him?")

            #third choice
            choices_3 = ["SWORD", "GOLD COINS", "TALK", "AWAKE"]
            user_choice_3 = make_choice(choices_3).upper()

            if user_choice_3 == "GOLD COINS":
                #narrative
                print("You scrabble to dig through the leaves to find these scattered coins. Thoughts race through your mind: Will this work? Is the troll \ninterested in gold? Will you be able to keep some for yourself?")
                print("The troll picks up his club, and charges toward you. You immediately fall to your knees, extending the gold coins in your cupped hands,\noffering them in exchange for your life.")
                print("The troll pauses, intrigued by your offering, once bloodthirsty eyes now glinting with greed. He reaches out, and snatches the gold coins.")
                print("Then he nods at you and turns away, satisfied with the business transaction.")
                print("As he starts to walk back towards the bridge, you eye the gold with longing. You didn't have time to hide any for yourself.")
                print("He shoots a gloating look over his shoulder, looks you square in the eye, and flips a coin towards you.")
                print("Surprised, you catch the coin, the glinting gold holding your attention for a moment. When you look up again, to your surprise,\n the troll is gone! You look around in confusion, and in it's place you see a tiny figure.")
                print("About two and a half feet tall, but with enormous, hairy, bare feet, and wearing a glowing blue amulet. 'Thank you for your patronage!' he called.")
                print("Tricked! This, this, this MIDGET tricked you! You start for the sword to get that gold back and make that trickster pay, AND")

                #starting over!
                main()