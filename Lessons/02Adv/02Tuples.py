# Tuple is a collection which is ordered and unchangeable(diff Lists). Allows duplicate members.

my_tuple=("Max", 28, "Boston")  # () is optinal

# my_tuple1=tuple(["Max", 28, "Boston"])
# print(my_tuple)

# # Accessing Index
# item = my_tuple[1]
# item1= my_tuple[-1]

# print(item)
# print(item1)

# Assignment : tuple' object does not support item assignment
# my_tuple[0]="Dav" #Returns error. since tuples immutable

# Iterating
# for i in my_tuple:
#     print(i)
    
# if "Max" in my_tuple:
#     print("Yes")
# else : 
#     print("No")

# my_tuple1 =("a", "p", "p", "l", "e")
# print(my_tuple1)

# print(len(my_tuple1))
# print(my_tuple1.count("p")) # returns the Quantity of the specific element in Tuples
# print(my_tuple1.index("p")) # returns the index of the specific element in Tuples

# Indexing and Slicing :
a= [1,2,3,4,5,6,7,8,9,10]

b= a[2:5]  # from 1(inc) to 5(exc)
c= a[1::2] # from 1(inc) to the end step 2
d= a[::-1] # reverse the list
e= a[1::-1] # reverse the list from the index[1]


print(a)
print(b)
print(d)
print(e)

