# # # # Sequence Types
# # # #Note: use print() to execute the examples. Comment out examples after they've been demoed.

# # # # Creating Lists
# # # #1. ✅ Create a list of 10 pet names
# # # import ipdb
# # # pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
# # # pet_names2 = ['Matt', 'Cute']

# # # # Reading Information From Lists
# # # #2. ✅ Return the first pet name 
# # # print(pet_names[0])

# # # #3. ✅ Return all pet names beginning from the 3rd index
# # # print(pet_names[3:])

# # # #4. ✅ Return all pet names before the 3rd index
# # # print(pet_names[0:3])


# # # #5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# # # print(pet_names[3:7])

# # # #6. ✅ Find the index of a given element
# # # print(pet_names.index('Tom'))

# # # #7. ✅ Reverse the original list
# # # (pet_names.reverse())
# # # print(pet_names)

# # # #8. ✅ Return the frequency of a given element 
# # # print(pet_names.count('Tom'))

# # # # Updating Lists
# # # #9. ✅ Change the first element to all uppercase 
# # # pet_names[0] = pet_names[0].upper()
# # # print(pet_names)

# # # #10. ✅ Append a new name to the list
# # # pet_names.append('Jamie')
# # # print(pet_names)

# # # #11. ✅ Add a new name at a specific index
# # # pet_names.insert(2, 'John')
# # # print(pet_names)

# # # #12. ✅ Add two lists together 
# # # pet_names.extend(pet_names2)  #can do new_list = list + list 2  (this doesn't mutate original list but creates a new list)
# # # print(pet_names)

# # # #13. ✅ Remove the final element from the list
# # # pet_names.pop()
# # # print(pet_names)

# # # #14. ✅ Remove element by specific index
# # # del pet_names[-1]
# # # print(pet_names)

# # # #15. ✅ Remove a specific element 
# # # pet_names.remove('Lea')
# # # print(pet_names)

# # # #16. ✅ Remove all pet names from the list
# # # pet_names.clear()
# # # print(pet_names)

# # #Tuple 
# # # 📚 Review With Students:
# # #     # Mutable, Immutable, Changeable, Unchangeable

# # # #17. ✅ Create a Tuple of pet 10 ages 
# # # pet_age = (1,2,3,4,5,6,7,8,9,10)
# # # print(pet_age)

# # # #18. ✅ Print the first pet age
# # # print(pet_age[4])

# # # # Testing Changeability 
# # #19. ✅ Attempt to remove an element with ".pop" (should error)
# # # print(pet_age.pop(2))

# # #20. ✅ Attempt to change the first element (should error)
# # # pet_age[0] = 22

# # # Tuple Methods
# # #21. ✅ Return the frequency of a given element
# # print(pet_age.count(2))

# # #22. ✅ Return the index of a given element 
# # print(pet_age.index(5))

# # #23. ✅ Create a Range 
# # #Note:  Ranges are primarily used in loops
# # range_10 = range(10)
# # print(range_10)

# # # Demo Sets (Stretch Goal)
# # #24. ✅ Create a set of 3 pet foods
# # pet_foods_set = set(['salmon', 'chicken', 'beef'])
# # print(pet_foods_set)

# # # Demo Dictionaries 
# # # Creating 
# # #25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
# # pet_info_dict = {'name': 'Hank', 'age': 4, 'breed': 'golden retriever'}


# # #26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
# # pet_info = dict(name= 'Hank', age= 4, breed= 'golden retriever')

# # # Reading
# # #27. ✅ Print the pet attribute of "name" using bracket notation 
# # print(pet_info['name'])

# # #28. ✅ Print the pet attribute of "age" using ".get"
# # #Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# # print(pet_info.get('age'))

# # # Updating 
# # #29. ✅ Update the pets age to 12
# # print(pet_info.update({'age': 12}))

# # #30. ✅ Update the other pets age to 26

# # print(pet_info_dict.update({'age': 26}))
# # # Deleting
# # #30. ✅ Delete a pets age using the "del" keyword 
# # del pet_info['age']
# # print(pet_info)

# # #31. ✅ Delete the other pets age using ".pop"
# # pet_info_dict.pop('age')
# # print(pet_info_dict)

# # #32. ✅ Delete the last item in the pet dictionary using "popitem()"
# # pet_info_dict.popitem()
# # print(pet_info_dict)

# # Demo Loops 
# # pet_info = [
# #     {
# #         'name':'rose',
# #         'age':111,
# #         'breed': 'domestic long-haired',
# #     }, 
# #     {
# #         'name':'spot',
# #         'age':25,
# #         'breed': 'boxer',
# #     },
# #     {
# #         'name':'Meow Meow Beans',
# #         'age':2,
# #         'breed': 'domestic long-haired',
# #     }
# #     ]

# # #33. ✅ Loop through a range of 10 and print every number within the range
# # for num in range(10):
# #     print (num)
# # #34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# # for num in range(50, 60, 2):
# #         print (num)

# # #35. ✅ Loop through the "pet_info" list and print every dictionary 
# # for dict in pet_info:
# #       print(dict)

# # #36. ✅ Create a function that takes a list as an argument 
# #     # The function should use a "for" loop to loop through the list and print every item 
# #     # Invoke the function and pass it "pet_names" as an argument
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
# # def print_pet_names(list):
# #     for name in list:
# #         print(name)
# # print_pet_names(pet_names)

# #37. ✅ Create a function that takes a list as an argument. (simple example) 
#     # The function should define a counter and set it to 0
#     # Create a "while" loop 
#         # The loop will continue as long as the counter is less than the length of the list
#         # Every loop should increase the count by 1
#     # Return the counter 
# def loop(list):
#     counter = 0
#     while counter < len(list):
#         counter += 1
#     return counter
# # print(loop(pet_info))
pet_info = [
    {
        'name':'rose',
        'age':111,
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

# #38. ✅ Create a function that updates the age of a given pet
#         # The function should take a list of "dict"s, "name" and "age" as parameters 
#         # Create am index variable and set it to 0
#         # Create a while loop 
#             # The loop will continue so long as the list does not contain a name matching the
#  "name" param and the index is less then the length of the list
#             # Every list will increase the index by 1
#         # If the dict containing a matching name is found, update the item's age with the new age 
#             # Otherwise, return 'pet not found'

def update_age(list, name, age):
    index = 0
    while index < len(list) and list[index].get('name') != name:
        index +=1
    if index < len(list):
        list[index]['age'] = age
        return list
    else:
        return 'pet not found'

print (update_age(pet_info, 'rose', 99))

# for num in range(0, 10, 2):
#         print(num ) 










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


# pet_info = [
#     {
#         'name':'rose',
#         'age':111,
#         'breed': 'domestic long-haired',
#     }, 
#     {
#         'name':'spot',
#         'age':25,
#         'breed': 'boxer',
#     },
#     {
#         'name':'Meow Meow Beans',
#         'age':2,
#         'breed': 'domestic long-haired',
#     }
#     ]
# def update_age(list, name, age):
#     i = 0
#     while i < len(list) and list[i]['name'] != name:
#         i+= 1
#     if i < len(list):
#         list[i]['age'] = age
#         return list
#     else:
#         return 'pet not found'
# print(update_age(pet_info, 'rose', 500))

    
    # i = 0
    # while i < len(list):
    #     if list[i]['name'] == name:
    #         list[i]['age'] = age
    #         i+=1
    #         return list
    # else:
    #     return 'pet not found'
# print(update_age(pet_info, 'rose', 120))

    
        

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# pet_info = [
#     {
#         'name':'rose',
#         'age':11,
#         'breed': 'domestic long-haired',
#     }, 
#     {
#         'name':'spot',
#         'age':25,
#         'breed': 'boxer',
#     },
#     {
#         'name':'Meow Meow Beans',
#         'age':2,
#         'breed': 'domestic long-haired',
#     }
#     ]
# # pet_info=[pet.get('name').upper() for pet in pet_info]
# print(pet_info)

pet_names = [ each_pet.get('name').upper() for each_pet in pet_info]

# # find like
# #40. ✅ Use list comprehension to find a pet named spot
# spot = [pet.get('name') for pet in pet_info if pet.get('name') == 'spot']
# print(spot)


# # filter like
# #41. ✅ Use list comprehension to find all of the pets under 3 years old
# pet_under3 = [pet for pet in pet_info if pet.get('age') < 3]
# print(pet_under3)

# #43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

