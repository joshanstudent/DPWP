#Why Python

#print "Hello World"

#one lined comments
'''
Doc strings
'''

first_name = "Kermit"
last_name = "De Frog"

# Remember that "raw_input" has been replace within Python 3, but within this class
#Use "raw_input" for the assignments
#response = raw_input("Enter your name")
# use "print response" to print single statement
# print response

# use "print "what ever you wish to say within this quote", response" will be for multiple statement
# It will print out Hello there along with the name the is enterd
#print "Hello there", response

birth_year = 1923
current_year = 2014
age = current_year - birth_year
#print age

#Dealing with object of different types
#print "You are" + age + "years old"
# To solve the errors with cannot concatenate 'str and 'int' objects, use the
# str() or int()
#print "You are " + str(age) + " years old"

# Talking about Conditional Statements
# You will get errors if you write the code below

#if(condition){
#    //stuff to do
#}
#if condition:
    #stuff to do

# To write Conditional Statements within errors is to write like it is below and
# there are other ways to write these statements but will learn them soon

# This code is to write the "if" "Yay! we can buy cool "
#budget = 200
#
#if budget > 100:
#    brand = "nike"
#    print "Yay! we can buy cool " + brand + " shoes!"
#else:
#    print "No cool shoes for me!"


# This code is to write the "else" "No cool shoes for me!"

#budget = 90
#
#if budget > 100:
#    brand = "nike"
#    print "Yay! we can buy cool " + brand + " shoes!"
#else:
#    print "No cool shoes for me!"

# This is the "else" "if" code statement below, you will notice that the fisrt
# two letters of of "else " and "if " is used to write this

#budget = 90
#
#if budget > 100:
#    brand = "nike"
#    print "Yay! we can buy cool " + brand + " shoes!"
#elif budget > 50:
#    print "We can get some genaric sheakers."
#else:
#    print "No cool shoes for me!"


# If you try to close the conditional statement this way, errors will be created

#budget = 90
#
#if budget > 100:
#    brand = "nike"
#    print "Yay! we can buy cool " + brand + " shoes!"
#elif budget > 50:
#    print "We can get some genaric sheakers."
#else:
#
#
#print "hi"


# To solve this error within the conditional statement when trying to close it.
# Use the "pass" command and it will close the statement within errors. This command can be used with "Loops",
# Functional" and "Conditional" statements.

#budget = 90
#
#if budget > 100:
#    brand = "nike"
#    print "Yay! we can buy cool " + brand + " shoes!"
#elif budget > 50:
#    print "We can get some genaric sheakers."
#else:
#    pass
#
#
#print "hi"

# Creating Arrays

#characters = ["leia", "luke", "chewy", "lando"]
#print characters


# If you want to add to Arrays

#characters = ["leia", "luke", "chewy", "lando"]
#characters.append("obi won")
#print characters


# If you want to print only one within the Array

#characters = ["leia", "luke", "chewy", "lando"]
#characters.append("obi won")
#print characters[0]


# If you want to print associate Array within Python, this is called
# Dictionary

characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi won")

#movies = dict() #create dictionary object
#movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]


# Creating "While Loop"

#i = 0
#while i<9:
#    print "The count is", i
#    i = i+1


# Creating "For Loop"

#for i in range(0,10):
#    print "The count is", i
#    i = i+1


# Creating "For Each Loop"

#rappers = ["tupac", "Nas", "Biggie Smalls"]
#for r in rappers:
#    print r

# Creating "Functions"

#def calcArea(h, w):
#    area = h * w
#    return area
#
#a = calcArea(20, 40);
#print a


# Creating "Functions"

#def calcArea(h, w):
#    area = h * w
#    return area
#
#a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft"


# Creating "Functions" with varibles above the function, it will be global
# to add more value to the math

#x = 2
#
#def calcArea(h, w):
#    area = h * w
#    return area + x
#
#a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft"


# How to put variables into a large string
# the (**locals()) method is point to the variable which is declaring
# the value within the {}

#weight = 200
#height = 63
#message = '''
#Your height is {height} and your weight is {weight}
#'''
#message = message.format(**locals())
#print message


# Can use this coding type to rewrite or replace codes within HTML for
# setup templates ahead of time and named the content.

#title = "Contact Us"
#body = "You can contact us at contact@us.com"
#message = '''
#<!DOCTYPE HTML>
#<html>
#    <head>
#        <title>{title}</title>
#    </head>
#    <body>
#        {body}
#    </body>
#</html>
#'''
#message = message.format(**locals())
#print message

#Math
#a = 2400
#print "Total for your bathroom reapirs is $",eval('a * .75'), "dollars"
