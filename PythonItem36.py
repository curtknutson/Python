# -*- coding: utf-8 -*-

# Python: 2.7.13

# Author: Curt Knutson

#Purpose: Learning Python Tech Academy Item 36


def start(name=""):
   #1. Assign an integer to a variable
    x=36

    #2. Assign a string to a variable
    course="Python item "

    #3. Assign a float to a variable
    y=52.9

    #4. Use the print function and .format() notation to print out the variable you assigned
    print ("{} {} is {} percent of the way done with Python course.").format(course,x,y)

    operators(x,y)
    logical()
    loopy()
    #13. Call the function you defined above and print the result to the shell
    name = get_name(name)
    print(name)
    print("\nI received the name {} from the function.").format(name)

def operators(x,y):
    #5. Use each of these operators +, - , * , / , +=, ­= , %
    addition = x + y
    print("Addition: "+ str(addition))
    aubtraction = addition - x
    multiplication = x * 2
    division = multiplication / 2
    addToSelf = 0
    addToSelf += 1
    modulus = 7 % 2
    print(modulus)

def logical():
    #6. Use of logical operators: and, or, not
    booleanand = False
    booleanand = True and True
    print (booleanand)
    booleanor = False
    booleanor = True or False
    print (booleanor)
    booleanora = not True or False
    print (booleanora)

def loopy():
    #9. Use of a for loop
    #10. Create a list and iterate through that list using a for loop to print each item out on a new line
    fruit =["apples","bananas","clementines","dates",]
    for counter in range(0,4):
        # Show the value of fruit in position counter
        print fruit[counter]
    #11. Create a tuple and iterate through it using a for loop to print each item out on a new line
    fibonacci = (0,1,1,2,3,5,8,13,21);
    for counter in range(0,9):
        # Show the value of fibonacci in position counter
        print fibonacci[counter]
        
#12. Define a function that returns a string variable
def get_name(namel):
    needName = True
    #8. Use of a while loop
    while needName == True:
        #7. Use of conditional statements: if, elif, else
        if namel == "":
            namel = raw_input("\nWhat is your name? ").capitalize()
            if namel == "":
                print("\nWe really do need your name!")
                needName = True
            elif (namel == 'Curt') or (namel == 'Ck'):
                print("\nWelcome, {}, you wrote this code.").format(namel)
                needName = False
            else:
                needName = False
                print("\nWelcome, {}, good to meet you.").format(namel)
    return namel  



if __name__ == "__main__":
    start()
