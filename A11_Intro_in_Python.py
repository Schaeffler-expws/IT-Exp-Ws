# Welcome to our Schaeffler Training Center! This is a Python program file. It is not really beautiful and structured, but good enough to see (!) and feel Python.

# The main idea is adapted from a course from https://raw.githubusercontent.com/raspberrypilearning/python-intro/master/code/intro.py
# The next two lines you should already know.

from sense_hat import SenseHat
sense = SenseHat()

# The lines that start with a hash "#" are comments
# When you see 'Start!', save and run the file to see the output
# When you see a line starting with "#" follow the instructions
# Some lines are python code with a "#" in front
# This means they're commented out - remove the "#" to uncomment
# Do one challenge at a time, save and run after each one!

# If it is too boring to see all former output of your work, 
# set a "#" in front of the former output (only output!) task. 

# 1a. This is the print statement on the screen

print("Hello IT-Experience Workshop")

# 1b. Show Message on our LEDs (we had that already).
# Of course, you are forced to change the text as well.

sense.show_message("Hello Kanban")

# Start!


# === NEXT ===
# 2. Now, we come to a variable. A variable has a value that can change. 

message = "Kanban Empty"

# Add a line below to print this variable on our LEDs. Try to add 
# ", text_colour=[255,0,255]"  after the variable, but still in the bracket.
# Have a look in the documentation for senseHAT to change the background, colour, etc.

# Start!


# === NEXT ===
# 3. The variable above is called a string (i.e. consists of characters)
# You can use single or double quotes (but must close them)
# You can ask Python what type a variable is. Try uncommenting the next line:

# print(type(message))

# Could you write the same code for the LEDs?

# Start!


# === NEXT ===
# 4. Another type of variable is an integer (a whole number)

a = 123
b = 654
c = a + b

# Try printing the value of c below to see the answer - of course on the 
# LEDs with a yellow background! It will not work! Be careful: show_message will only accept text. Therefore, numbers have to be converted to string outside of the show_message command. We will come back in step 7.

# Start!



# === NEXT ===
# 5. Variables keep their value until you change it

a = 100
# print(a)  # think - should this be 123 or 100?

c = 50
# print(c)  # think - should this be 50 or 777?

weight = 10 + a - c
# print(weight)  # think - what should this be now?

# Start!



# === NEXT ===
# 6. You can also use '+' to add together two strings

greeting = 'Hi '
name = 'SBOT'  

message = greeting + name
# sense.show_message(message)

# Start!


# === NEXT ===
# 7. We can convert numbers to strings like this. I'm sorry, 
# you can't mix numbers and strings.

# print(name + '`s load' + ' is ' + str(weight) + ' kg heavy')

# Start!


# === NEXT ===
# 8. Another variable type is called a boolean
# This means either True or False

experience_workshop_is_fun = True
experience_workshop_is_boring = False

# We can also compare two variables using ==

sbot1_weight = 15
sbot2_weight = 20

# print(sbot1_weight == sbot2_weight)  # this prints either True or False. 
# Again, we can't use our LED for this "complex" calculation in the brackets.

# Start!



# === NEXT ===
# # 9. We can ask questions before printing with an if statement

max_weight = 500
skrew_weight = 240
nut_weight = 200

total_weight = skrew_weight + nut_weight
can_afford_both = max_weight > total_weight

if can_afford_both:   # is a true value
    message = "we can carry both"
else:
    message = "You can't carry both"

# sense.show_message(message, scroll_speed=0.05)  
# what do you expect to see here?

# Start!

# Now change the value of nut_weight to 260 and run it again
# What should the message be this time?

# Start!

# Is this right? You might need to change the comparison operator to >=
# This means 'greater than or equal to'

tire_weight = 25
count = 3	
tires_weight = count * tire_weight

total_weight = total_weight + tires_weight

if total_weight <= max_weight:
    message = "You can carry the tires as well"
else:
    message = "You can't carry " + str(count) + "tires as well"

# sense.show_message(message)  
# what do you expect to see here?

# Start!



# === NEXT ===
# 10. You can keep many items in a type of variable called a list

colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# You can check whether a colour is in the list

# print('Black' in colours)  # Prints True or False

# Start!

# Is it possible to print a bool value on the LEDs?

# Start!

# You can add to the list with append

colours.append('Black')
colours.append('White')

# print('Black' in colours)  # Should this be different now?

# Start!

# You can add a list to a list with extend

more_colours = ['Gray', 'Navy', 'Pink']

colours.extend(more_colours)

# Try printing the list to see what's in it

# Start!



# === NEXT ===
# 11. You can use a loop to look over all the items in a list

my_items = ['nut', 'skrew', 'tire', 'shock absorber']

# Below is a multi-line comment
# Delete the '''from before and after to uncomment the block

'''
for item in my_items:
    print(item)
'''

# Add two additional items to this list

# Remember the difference between append and extend. You can use either.

# Now write a loop to print a number (starting from 1) before each item

# Start!



# === NEXT ===
# 12. Another useful data structure is a dictionary

# Dictionaries contain key-value pairs like the item weight relationships 

weight_items = {
    'nut': 100,
    'skrew': 124,
    'show absorber': 250
}

# You access the elements by looking them up with the key:

# print(weight_items['nut'])

# You can check if a key or value exists in a given dictionary:

# print('wheel' in weight_items)  # [False]
# print('nut' in weight_items)  # [True]
# print('250' in weight_items)  # [False]
# print(250 in weight_items.values())  # [True]

# Start!

# Note that 250 was entered in to the dictionary as an integer
# Try changing skew weight to a new amount

# weight_items['skrew'] = 140
# print(weight_items['skrew'])

# Start!

# Delete nut from the dictionary

# print('nut' in weight_items # [True]
# del weight_items['nut']
# print('nut' in weight_items)  # [False]

# Start!

# You can also loop over a dictionary and access its contents:
'''
for item in weight_items:
    print(item, weight_items[item])
'''
# Start!



# === NEXT ===
# 13. Sometimes we need an endless loop 

# Below is a multi-line comment
# Delete the '''from before and after to uncomment the block

'''
i = 1
while i < 6:
    print(i)
    i += 1
''' 

# What is 'while' doing? How can I stop that?
# i += 1 is a shortcut for i = i + 1 

# Start!



# === NEXT ===
# 14. Additional to internal functions, we build our own functions

# - first, we need a definition part to define the function

# - afterwards we have to execute it

def good_work(bot):
    sense.show_message("Good work, " + bot + "!")

# good_work('Sbot')

# Start!