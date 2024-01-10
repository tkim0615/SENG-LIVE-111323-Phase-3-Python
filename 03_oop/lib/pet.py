#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 

import ipdb

# class: blueprints --- instances: we create  instances from blueprints 
# class : cookie cutter --- instances: cookie 

#define Pet class using class keyword
class Pet: # UpperCamelCase # PascalCase 

    # 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

    def __init__(self, name, age, breed, temperament): # initialization method
        #what is self? instance of Pet class
        #to provide obj(instance) with unique attributes upon the instantiation
        print(name, age, breed, temperament) 

        # attached incoming parameter to the self's attributes 

        #set each pet instance's attributes
        self.name = name #instance attribute#1 
        self.age = age #instance attribute#2
        self.breed = breed 
        self.temperament = temperament 

        # 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes

    #instance method
    def print_pet_details(self): #what is self? self is the instance 
        print( f'''
            name: {self.name}    
            age: {self.age}
            breed: {self.breed}
            temperament:{self.temperament}
            ''')
        pass  

    pass

milo = Pet("Milo", 5, "Great Pyrenees", "calm")
clementine = Pet("Clementine", 12, "corgi mix", "sassy")

ipdb.set_trace() # breakpoint

# clementine = Pet() # instantiate a new instance 
# ipdb> clementine # call the instance
# <__main__.Pet object at 0x1074da430> # instance info
# milo = Pet()
# ipdb> milo
# <__main__.Pet object at 0x107449fd0>
# clementine == milo # clementine and milo are two different instances # they hold different memory 

# using doc notation to access their attributes/ 
# ipdb> milo.temperament
# 'calm'
# ipdb> clementine.age
# 12
# ipdb> clementine.temperament

#ipdb> milo.print_pet_details() # invoke the instance method using the dot notation




# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

