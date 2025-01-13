# Enhancements: Added extra sentences to the story for more user input and creativity. Dynamically determine whether to use "a" or "an" based on the user's input.

print("\nPlease enter the following :\n")

# Prompt user for words
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")
verb3 = input("Enter a third verb: ")

# Additional inputs for enhanced story
place = input("Enter a place: ")
food = input("Enter a type of food: ")
color = input("Enter a color: ")
object = input("Enter an object: ")


# Determine "a" or "an" for adjective
if adjective[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"


print("\nYour story is:")

# Build and display the story
story = f"""
The other day, I was really in trouble. It all started when I saw {article} {adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.

Later that day, I went to {place} to calm down. I treated myself to some {food} and thought about how {color} the {object} looked in the sunlight. What a strange day it was!
"""

print(story)

