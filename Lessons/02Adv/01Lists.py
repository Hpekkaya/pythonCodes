# List is a collection which is ordered and changeable(mutable). Allows duplicate members.

# my_list = ["apple", "banana", "cherry"]
# print(my_list)

# for i in my_list:
#     print(i)
    
# print("-- --") 

# if ("baana") in my_list: print("Yes") 
# else : print("No")

# my_list.append('lemon')
# print(my_list)

# my_list.insert(1, "appricot")
# print(my_list)

# item = my_list.pop(1) # Remove and return item at index (default last).
# item2 = my_list.remove('apple') # Remove first occurrence of value.
# print(item)
# print(item2)
# print(my_list)

# my_list.clear() # Remove all the elements, takes no arguments

# my_list.reverse()

# my_list_num = [4,3,5,8,-3,9]
# item = my_list_num
# print(my_list_num)
# sorted_numbers=item.sort()
# print(my_list_num)
# print(item)

# new_list = my_list +my_list_num
# print(new_list)
 
# # Slicing :
# # Taking elements from one given index to another given index
# my_list = [1,2,3,4,5,6,7,8,9]
# a=my_list[1:5]  # from 1(inc) to 5(exc)
# print("a :",a)

# b=my_list[1::]  # from 1(inc) to the end
# print("b :",b)

# c=my_list[::3]  # from the beginning to the end step 3
# print("c :",c)

# d=my_list[::2]  # from 1(inc) to the end step 2
# print("d :",d)

# e=my_list[::-1]  # reverse the list
# print("e :",e)

# print("Length of List :", len(my_list))

# Copying the List 

# list_org = ["apple", "banana", "cherry"]

# list_copy = list_org 
# list_copy.append("lemon")
# print(list_org) #since it refers the same adress the same with _copy
# print(list_copy)

# #to make change
# # list_copy = list_org.copy() # or
# # list_copy = list(list_org)  # or
# list_copy = list_org[:]

# list_copy.append("appricot")
# print(list_org) 
# print(list_copy)

#  List Comprehension

my_list = [1,2,3,4,5,6,7,8,9]
b= [i*i**i for i in my_list]
c= [(i*i)**i for i in my_list]

print(my_list)
print(b)
print(c)
