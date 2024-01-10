#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 
import ipdb
class Pet:
    def __init__(self, name, age, breed, temperament):

        #4 instance attributes
        self.name = name 
        self.age = age
        self.breed = breed
        self.temperament = temperament
    def print_details(self):
        print(f'''
              name: {self.name},
              age: {self.age},
              breed: {self.breed},
              temperament: {self.temperament}
              ''')
tyler = Pet('tyler', 31, 'beagle', 'sassy') #tyler.name = 'Tyler Kim' - can use dot.notataion to access attributes or change it
(tyler.print_details())
# ipdb.set_trace()

jindo = Pet('jindo', 3, 'jindo dog', 'happy')
# ipdb.set_trace()# breakpoint - now we can enter ipdb in terminal and try out different things
class Flower:
    def __init__(self, name, color, region):
        self.name = name
        self.color = color
        self.region = region

tulip = Flower('Tulip', 'red', 'Europe')
sunflower = Flower('Sunflower', 'yellow', 'South America')
rose = Flower('Rose', 'yellow', 'Asia')
# ipdb.set_trace()

# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 


# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg


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

