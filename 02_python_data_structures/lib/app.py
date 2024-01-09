# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = [ "Rose", "Cup", "Hammie", "Hazel", "Sadie", "Gigi", "Pinky", "Hammie", "Japhy", "Jappy"]

# Reading Information From Lists
#2. ✅ Return the first pet name 
# print(pet_names[0])

# #3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:])

# #4. ✅ Return all pet names before the 3rd index
# print(pet_names[:3])

# #5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[3:7])

# #6. ✅ Find the index of a given element
# print(pet_names.index('Gigi'))

# #7. ✅ Reverse the original list
# print(pet_names.reverse())
# print(pet_names)

# #8. ✅ Return the frequency of a given element 
# print(pet_names.count("Hammie"))

# # Updating Lists
# #9. ✅ Change the first element to all uppercase 
# pet_names[0] = pet_names[0].upper()
# print(pet_names)

# #10. ✅ Append a new name to the list
# pet_names.append("Clementine")
# print(pet_names)

# #11. ✅ Add a new name at a specific index
# pet_names.insert(3, "Ken")
# print(pet_names)

# #12. ✅ Add two lists together 
# #option 1
# new_list = ['winter', 'lucy']
# combine_list = pet_names + new_list
# print(combine_list)

# #mutate the original list
# new_list_2 = [1, 2, 3, 4] 
# pet_names.extend(new_list_2)
# print(pet_names)


# #13. ✅ Remove the final element from the list
# pet_names.pop()
# print(pet_names)

# #14. ✅ Remove element by specific index
# print(pet_names.pop(6))
# pet_names.remove(pet_names[6])

# #15. ✅ Remove a specific element 
# pet_names.remove("Rose")
# print(pet_names)

# #16. ✅ Remove all pet names from the list
# pet_names.clear()

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable
    # List : Mutable
    # Tuple : Immutable

# Tuple is an immutable data type that can also store many types of data.

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = ( 1, 2, 3, 4, 5, 6, 7, 7, 7, 7 )

#18. ✅ Print the first pet age
pet_ages[0]

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)


#20. ✅ Attempt to change the first element (should error)


# Tuple Methods
#21. ✅ Return the frequency of a given element
pet_ages.count(7)

#22. ✅ Return the index of a given element 
# print(pet_ages.index(5))



#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops


# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info = { "name": "Hammurabi", "age": "8 months", "breed": "golden doodle"}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_2 = dict(name="Hazel", age=2, breed="labdoodle")


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info["name"])

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# print(pet_info.get('age'))

# Updating 
#29. ✅ Update the pets age to 12
# pet_info['age'] = 12
# print(pet_info)

#30. ✅ Update the other pets age to 26
# pet_info_2.update({'age': 26})

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del pet_info_2['age']

#31. ✅ Delete the other pets age using ".pop"
# pet_info.pop('age')

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
# pet_info.popitem()

# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
# for num in range(10):
#         print(num)

# for num in range(0, 10, 2):
#         print(num ) 

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50, 60, 2):
#         print(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
# for each_pet in pet_info:
#         print(each_pet)

#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
def print_list_items(lst):
    for item in lst:
            print(item)
# print_list_items(pet_names)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
#[{}, {}, {}] #2 
def count_increment(lst):
    counter = 0
    while(counter < len(lst)):
            counter += 1
    return counter
# count_increment(pet_info)


#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

# def update_age(lst, name, age):
#     idx = 0
#     print(len(lst))
#     # check all the names #
#     while(lst[idx].get('name') != name and idx < len(lst)-1):
#            print("every item----")
#            idx += 1 # keep incrementing the index number to look through every items 
#     if lst[idx].get('name') == name: # if the name is the same 
        
#         print(lst[idx])#print the original dict
       
#         lst[idx]['age'] = age # update/ replace the age with the given arg
        
#         return lst[idx] # return the new dict with the new age
#     else:
#         return 'pet not found'    

# update_age(pet_info, 'rose', 120)


# def update_age(lst, name, age):
#     idx = 0
#     print(len(lst), idx)
#     while idx < len(lst) and lst[idx].get('name') != name:
#         print("every item----", lst[idx])
#         idx += 1
#     if idx < len(lst) and lst[idx].get('name') == name:
#         print(lst[idx])
#         lst[idx]['age'] = age
#         return lst[idx]
#     else:
#         return 'pet not found'


# pet_info = [{'name': 'rose', 'age': 100}, {'name': 'lily', 'age': 80}]
# result = update_age(pet_info, 'rose', 120)
# print(result)

                 
# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
def upper_name(pet_info):
    for each_pet in pet_info: 
        each_pet['name'] = each_pet['name'].upper()
        print(each_pet)     

pet_names = [ each_pet.get('name').upper() for each_pet in pet_info]

# find like
#40. ✅ Use list comprehension to find a pet named spot
pet_name_spot = [ each_pet for each_pet in pet_info  
 if each_pet.get('name') == 'spot']

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
pet_under_3 = [ each_pet for each_pet in pet_info 
    if each_pet.get('age') < 3]

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension.
young_pets = ( each_pet for each_pet in pet_info  
    if each_pet.get('age') < 3)

