#This is a function I'm using to specify if an 'a' or an 'an' should come before a noun.
def choose_article(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if sound[0].lower() in vowels:
        return 'an'
    else:
        return 'a'


adjective=input("Choose an adjective: ")
animal=input("Choose an animal: ")
verb1=input("Choose a verb: ")
exclamation=input("Choose an exclamation: ")
verb2=input("Choose another verb: ")
verb3=input("Choose one more verb:")
adjective2=input("Choose another adjective: ")
plural_noun=input("Choose a plural noun found in your house: ")
sound=input("Choose a sound: ")
article1=choose_article(sound)
noun2=input("Choose a noun: ")
adverb=input("Choose an adverb: ")
sound2=input("Choose another sound: ")
article2=choose_article(sound2)
room=input("Choose a room in your house: ")
animal2=input("Choose another animal: ")
article3=choose_article(animal2)
verb4=input("Choose a verb that is difficult to do: ")
verb5=input("Choose a verb that is EASY to do: ")
emotion=input("Choose an emotion: ")
past_verb=input("Choose a verb in the past tense: ")
number=input("Choose a number: ")


print("The other day, I was really in trouble. It all started when I saw a very")
print(f'{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print("right in front of my family.")
print(" ")
#making the story longer, and adding more options.
print("With my heart still racing, I realized that my quick thinking had only been the beginning of")
print(f"this wild adventure. As the {animal} retreated, it left behind a trail of {number} {adjective2} {plural_noun} in it's")
#I apply my function in this next line
print(f"wake. All of a sudden, there was {article1} {sound}, and everybody stopped in their {noun2}, ")
print(f"and we all just stood there, {adverb} trying to figure out what was going on. ")
#Using the function again
print(f"Just as we thought the chaos was over, there was {article2} {sound2} coming from the {room}. It seems ")
#Using the function again with a different kind of word
print(f"the {animal} had a partner in crime: {article3} {animal2}. ")
print(" ")
print("I knew I had to take charge of the situation. With determination in my heart, I decided to")
print(f"{verb4} to catch the {animal2} and {verb5} to get the {room} clean. My family pitched in too,")
print(" and together we were able to get the house back in order. At the end of the day, we were filled with")
print(f"{emotion}, and we all {past_verb} together.  It was a day filled with unexpected surprises and unforgettable memories.")