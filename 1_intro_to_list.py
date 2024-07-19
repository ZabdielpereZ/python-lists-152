# python list 

# list are just collections of items. Lists are muteable, ordered, dynamic

# -- mutable : we have the ability to mutate list; remove, manipulate data
# -- Ordered : Each iteam in list has a specific position, which allows us to know where each item is (indecies/indexs)
# #-- dynamic : we can add and remove data from lists allowing them to grow and shrink as needed


# List are created with [] square brakets, and each iteam inside of a list is seperated by a comma --> , 

# empty list
empty_list = []

# populated list

person = 'Jill'

people = [person, 'Bob', 'Barry', 'Bill']

# python lists can contain many diffrent data types

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis', ['tacos']]]

#---- list Indecies

# Each item is marked by a specific index
# Indecies are in numeric order starting from 0, we can use them to access, modify, and remove items from our lists

#idecies    0        1        2         3
alist = ['item1', 'item2', 'item3', 'item4']
print(alist)

# grab item 3 with index 2
print("third iteam:", alist[2])

# grab the first iteam with index 0
print("Item 1, first item: ", alist[0])

# grab the last iteam 
print("the last item: ", alist[3])

# grab the last item with the index -1
print("The last item accessed with index -1: ", alist[-1])

# grab the third item in alist with index -2
print("Grabbing the second to last item with index -2: ", alist[-2])

# potential pitfall

# IndexError  
#-- index out of range, trying to access an index that doesnt exist in a spific index that  

# print(alist[4])