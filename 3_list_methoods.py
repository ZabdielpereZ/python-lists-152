# Some cool things that we can do with lists methods

food = ['taco', 'pizza', 'tiramisu']

#-- list.append(item)

print("Adding ice cream")
food.append("ice cream")
print(food)

#-- list.insert(index, item) : allows us to add an item to a specific index
# adding to a list at an index that doesnt exist will simply add it to the end of the list

print("Inserting a potato into our lists of food")
food.insert(2, "potato")
print(food)

food.insert(6, 'cheese') # index 6 doesn't exist in our food lits at this point in our code, so 'cheese' is appended to the end
print(food)

#-- list.remove(item)
print('removing pizza... :(')
food.remove('pizza')
print(food)

print('='*50)

#-- list.pop () : removes and returns the last item on the list
# just because the .pop() methood also returns the value removed, doesnt mean we have to store it or use it

print("putting our cheese in the fridge")
fridge = food.pop()
print("What's in the fridge: ", fridge)
print(food)

#-- list.pop(index) : removes an item at a specific index 

print("Popping our potato in the oven")
oven = food.pop(1)
print("oven: ", oven)
print(food)

print('='*50)

# just playing around dont need to undertand yet!
print(f"I really like {food[0]}. I also love {food[1]}. and im obsessed with {food[2]}") # <--- formatted strings (not there yet!)

# Hit up the grocery store

food.append('key lime pie')
food.append('cheese burger')
food.append('fish')
food.append('sushi')
food.append('beer')
food.append('salad')

print("we went to the grocery store")
print(food)

#-- list.index(item) : will return the index of a particular item 
print('Finding the index of beer using .index()')
beer_idx = food.index('beer')
print("the indexical position of beer in our food list is: ", beer_idx)

#-- Modify data at a specific index/position.    MUTABILITY :" list[index] = new_item
print("change beer into juice?")
food[7] = 'juice'
print(food)


print('='*50)

food.append('cheese burger')

#-- list.count(item) : will count the occurances of an item in a list and return an integer
burger_count = food.count('cheese burger')
print(food)
print("burger count: ", burger_count)

print('='*50)

#-- list.reverse() : will reverse the order of your list
print("Original food list: ", food)
food.reverse()
print("Our food list reversed: ", food)

print('='*50)

#-- list.sort() : will sort your list in either alphabetical order or numerical order
# when sorting a list, all itmes within it must be of the same data type
print("Sorting our food list alphabetical order")
food.sort()
print(food)

# Multiple data types do not work together when sorting a list
# test = [1, 'stringgg', 3.14, food]
# test.sort()
# print(test)

print('='*50)

#-- list.reverse()
food.sort(reversed= True)
print(food)

print('='*50)
#--------- List functions

#-- len(item) : retuen the length of the list aka how many items are in the list 
print("the length of our list is: ", len(food))

#-- sum(item) : give us the sum total of all the numbers in a list
# The list must be made up of entirely numbers- ints and floats 


nums = [1,2,3,4,5,6,7,8,9]
total = sum(nums)
print("the sum of all the nums in our nums list : ", total)
