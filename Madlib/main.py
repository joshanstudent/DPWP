# My MadLib Program by Joseph Handy

print "Welcome to my game!"

import random

guesses = 0
first = raw_input("What is your first name? ")
number = random.randint(1,5)
print first + ", I am thinging of a number between 1 and 5 "
while guesses < 3:
    guess = int(raw_input("Take a guess. "))
    guesses = guesses + 1

    if guess < number:
        print "Your guess is too low!"
    if guess > number:
        print "Your guess is too high!"
    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print "Good job, " + first + " You guessed my number in " + guesses + " guesses"
if guess != number:
    number = str(number)
    print "Nope. The number I was thinking about was actually " + number


last = raw_input("Enter last name: ")
city = raw_input("Enter your city: ")
state = raw_input("Enter your state: ")
address = raw_input("Enter your address: ")
zip = raw_input("Enter your zip code: ")
bathroom = ['floor', 'tube', 'wall']
additional = raw_input("Please add another task to do within your bathroom: ")


print "Hello ", first, last, "I see that you are looking for repairs within your house in", city, state, "at", address, zip,
print bathroom
print " additional task to fix within your bathroom is", additional,

def calcArea(h, w):
    area = h * w
    return area

a = calcArea(40, 60);
print "with an area space of " + str(a) + "sqft"








