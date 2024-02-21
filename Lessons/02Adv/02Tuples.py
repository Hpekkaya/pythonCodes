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
# a= [1,2,3,4,5,6,7,8,9,10]

# b= a[2:5]  # from 1(inc) to 5(exc)
# c= a[1::2] # from 1(inc) to the end step 2
# d= a[::-1] # reverse the list
# e= a[1::-1] # reverse the list from the index[1]


# print(a)
# print(b)
# print(d)
# print(e)

# Unpacking
# my_tuple=("Max", 28, "Boston")

# name, age, city = my_tuple

# print(name)
# print(age)
# print(city)

# my_tuple_num =(0,1,2,3,4,5,6)

# i1,*i2,i3 =my_tuple_num

# print(my_tuple_num)
# print(i1)
# print(i2)
# print(i3)

# Compare List and Tuples
# When deal with large amount of data Tuples more efficient 
import sys, timeit

my_list = [0,1,2, "hello", True]
my_tuple = (0,1,2, "hello", True)
print(sys.getsizeof(my_list),"bytes")   # 104 bytes
print(sys.getsizeof(my_tuple),"bytes")  #  80 bytes

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  #0.24801
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  #0.09346  Tupples Much more efficient

