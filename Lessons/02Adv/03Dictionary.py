# Dictionary is a collection which is ordered and changeable. No duplicate members.
# Collection of Key-Value pairs,

my_dict ={"name":"Max", "age" :28, "city" : "New York"}
# print(my_dict)

# value = my_dict["name"]
# print(value)

# my_dict["email"] = "hpek1980@gmail.com"
# print(my_dict)

# del my_dict["name"] 
# print(my_dict)

# my_dict.pop("name" )
# print(my_dict)   # or alternative

# my_dict.popitem()   #Bydefault pop the last element
# print(my_dict)

# Checking

# if var1 in  my_dict :
#     print(my_dict["name"], "is in Dictionary")
# else : print(my_dict["name"], "is not in Dictionary")

# try:
#     print(my_dict["lname"])
# except:
#     print("Error !")

# Loop through dictionary

# for key in my_dict:
#     print (key)

# for value in ( my_dict.values()):
#     print (value)
    
# Copy a dictionary
# my_dict_copy = dict(my_dict) #Don't change the original dictionary
# print(my_dict_copy)

# my_dict_copy["email"]="max@xyz.gmail.com"
# print(my_dict_copy)
# print(my_dict)

# Update process
my_dict ={'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.gmail.com'}
my_dict_2 = {'name': 'Mary', 'age': 18, 'city': 'Boston'}

# Merge
my_dict.update(my_dict_2)
print(my_dict)
print(my_dict_2)




    