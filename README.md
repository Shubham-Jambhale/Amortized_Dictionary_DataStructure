# Amortized_Dictionary_DataStructure

# Question

Let us implement the amoritized dictionary in python as a class using python dicitonary. The
dictionary keys acts levels and values of the dicitonaries are list of elements. The level i contains
either 2i elements or no elements at all. If the level has elements , then all the elements are in
sorted order.For this class implement search, insert, print methods.

# Example 

ad_obj = amor_dict([23, 12 ,24, 42])

ad_obj.print()

 0:empty
 
 1:empty

 2:[12, 23, 24, 42]

ad_obj.insert(11)

ad_obj.print()

0:[11]

1:empty

2:[12, 23, 24, 42]

ad_obj.insert(74)
ad_obj.print()

0:empty

1:[11, 74]

2:[12, 23, 24,42]

ad_obj.search(74)
level 1
ad_obj.search(77)
level -1
