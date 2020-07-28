import time
from binary import BSTNode as BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# binary = BST(names_1[0])                        # runtime: 0.10870909690856934 seconds
# for name_1 in names_1:
#     binary.insert(name_1)
# for name in names_2:
#     if binary.contains(name):
#         duplicates.append(name)
set_1 = set(names_1)                        # runtime: 0.007978439331054688 seconds
set_2 = set(names_2)
duplicates = set_1.intersection(set_2)

# cast each input list to a set
# a set in Python is an unordered collection with no duplicate elements
# sets have an intersection method to return unique elements found in both sets  
# intersection_set = set1.intersection(set2)
# cast intersection_set as list
# return list
# https://dfrieds.com/python/intersection-two-arrays.html
# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/ref_set_intersection.asp

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
