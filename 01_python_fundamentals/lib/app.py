#!/usr/bin/env python3

# 📚 Review With Students:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb" iPython debugger
import ipdb

#js camelCase
#python snake_case

#js can declare variables  without assignment
#python cannot declare variable without assignment

def hello_world():
    monday = " need coffee bear"
    print(monday)
    #ipdb.set_trace() #pause the execution of code 
    #debugger here

    not_interpreted_yet = " lunch "
    print(not_interpreted_yet)

hello_world()


# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

# if time is morning, print eat breakfast
# if time is afternoon print eat lunch 
# if time is dinner print eat dinner 
# In all other cases, print go to sleep 

pet_mood = "Hungry!"
pet_name = "Rose"

#conditional syntax

if pet_mood == "Hungry!":
    print("Rose needs to be fed.")
elif pet_mood == "Rowdy":
    print("Rose needs a walk")
else: 
    print("Rose is all good.")


# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_mood is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

# if time is morning, print eat breakfast, all other cases study python 
    
# JS 
    #condition? true: false
# python 
    # true, if condition else default val 
print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

def say_hello(param = "hello"): #default argument 
    print("hello, world!") # indentation is important 

say_hello()



# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

    # schedule("morning") => " it's morning, let's eat breakfast! "
    # f " it's {time}, let's eat breakfast! "
def pet_greeting(name):
    return f"{name} says hello!"

print(pet_greeting("Rose"))

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


