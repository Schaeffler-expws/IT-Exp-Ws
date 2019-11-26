
# Welcome! This is a Python program file.

# The content is adapted from a course from https://raw.githubusercontent.com/
# raspberrypilearning/python-intro/master/code/intro.py
# But, it's more fancy to use the LEDs. Actually, ignore the next 2 lines.

from sense_hat import SenseHat
sense = SenseHat()

# The lines that start with a hash "#" are comments
# They are for you to read and are ignored by Python

# When you see 'GO!', save and run the file to see the output
# When you see a line starting with "#" follow the instructions
# Some lines are python code with a "#" in front
# This means they're commented out - remove the "#" to uncomment
# Do one challenge at a time, save and run after each one!

# If it is too boring to see all former output of your work,
# set a "#" in front of the former output task.

# 1a. This is the print statement on the screen

print("Hello LearningLab")

# 1b. Show Message on our LEDs

sense.show_message("Hello Learning Lab")

# GO!

# 2. This is a variable. A variable has a value that can change.

message = "Success"

# Add a line below to print this variable on our LEDs. Try to add
# , text_colour=[255,0,255]  after the variable, but still in the bracket.

# GO!

# 3. The variable above is called a string
# You can use single or double quotes (but must close them)
# You can ask Python what type a variable is. Try uncommenting the next line:
# print(type(message))
# Could you write the same code for the LEDs?

# GO!

# 4. Another type of variable is an integer (a whole number)
a = 123
b = 654
c = a + b

# Try printing the value of c below to see the answer - of course on the
# LEDs with a yellow background!
# GO!

# 5. Variables keep their value until you change it

a = 100
# print(a)  # think - should this be 123 or 100?

c = 50
# print(c)  # think - should this be 50 or 777?

age = 10 + a - c
# print(age)  # think - what should this be now?

# GO!

# 6. You can also use '+' to add together two strings

greeting = 'Hi '
name = ''  # enter your name in this string

message = greeting + name
# sense.show_message(message)

# GO!

# 7. We can convert numbers to strings like this. I'm sorry,
# you can't mix numbers and strings.

# print(name + ' is ' + str(age) + ' years old')

# GO!

# 8. Another variable type is called a boolean
# This means either True or False

raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False

# We can also compare two variables using ==

bobs_age = 15
# your_age =  # fill in your age

# print(your_age == bobs_age)  # this prints either True or False.
# Again, we can't use our LED for this "complex" calculation in the brackets.

# GO!

# 9. We can ask questions before printing with an if statement

money = 500
phone_cost = 240
tablet_cost = 200

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:# is a true value
   message = "You have enough money for both"
else:
   message = "You can't afford both devices"

# sense.show_message(message, scroll_speed=0.05)
# what do you expect to see here?

# GO!

# Now change the value of tablet_cost to 260 and run it again
# What should the message be this time?

# GO!

# Is this right? You might need to change the comparison operator to >=
# This means 'greater than or equal to'

raspberry_pi = 25
pies = 3 * raspberry_pi

total_cost = total_cost + pies

if total_cost <= money:
    message = "You have enough money for 3 raspberry pies as well"
else:
    message = "You can't afford 3 raspberry pies"

# sense.show_message(message)
# what do you expect to see here?

# GO!

# 10. You can keep many items in a type of variable called a list

colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# You can check whether a colour is in the list

# print('Black' in colours)  # Prints True or False

# GO!

# Is it possible to print a bool value on the LEDs?

# GO!

# You can add to the list with append

colours.append('Black')
colours.append('White')

# print('Black' in colours)  # Should this be different now?

# GO!

# You can add a list to a list with extend

more_colours = ['Gray', 'Navy', 'Pink']

colours.extend(more_colours)

# Try printing the list to see what's in it

# GO!

# 11. You can use a loop to look over all the items in a list

my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']

# Below is a multi-line comment
# Delete the '''from before and after to uncomment the block

'''
for student in my_class:
    print(student)
'''

# Add two the names of people in your group to this list

# Remember the difference between append and extend. You can use either.

# Now write a loop to print a number (starting from 1) before each name

# GO!

# 12. Another useful data structure is a dictionary

# Dictionaries contain key-value pairs like an address book maps name
# to number

addresses = {
    'Lauren': '0161 5673 890',
    'Amy': '0115 8901 165',
    'Daniel': '0114 2290 542',
    'Emergency': '999'
}

# You access dictionary elements by looking them up with the key:

# print(addresses['Amy'])

# You can check if a key or value exists in a given dictionary:

# print('David' in addresses)  # [False]
# print('Daniel' in addresses)  # [True]
# print('999' in addresses)  # [False]
# print('999' in addresses.values())  # [True]
# print(999 in addresses.values())  # [False]

# GO!

# Note that 999 was entered in to the dictionary as a string, not an integer
# Think: what would happen if phone numbers were stored as integers?
# Try changing Amy's phone number to a new number

# addresses['Amy'] = '0115 236 359'
# print(addresses['Amy'])

# GO!

# Delete Daniel from the dictinary

# print('Daniel' in addresses)  # [True]
# del addresses['Daniel']
# print('Daniel' in addresses)  # [False]

# GO!

# You can also loop over a dictionary and access its contents:
'''
for name in addresses:
  print(name, addresses[name])
'''
# GO!

# 13. Sometimes we need a endless loop

# Below is a multi-line comment
# Delete the '''from before and after to uncomment the block

'''
while True:
   print(my_class)
'''

# What is 'while' doing? How can I stop that?

# GO!

# 14. Additional to internal functions, we build our own functions

# - first, we need a definition part to define the function

# - afterwards we have to excute it
'''
def goodwork(person):
    sense.show_message("Good work, " + person + ".")

goodwork('Lars')
goodwork('Holger')
'''
# GO!
