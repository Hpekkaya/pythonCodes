# Dictionary is a collection which is ordered and changeable. No duplicate members.
# Collection of Key-Value pairs,

my_dict ={"name":"Max", "age" :28, "city" : "New York"}
print(my_dict)

value = my_dict["name"]
print(value)

my_dict["email"] = "hpek1980@gmail.com"
print(my_dict)

del my_dict["name"] 
print(my_dict)

my_dict.pop("name" )
print(my_dict)   # or alternative

my_dict.popitem()   #Bydefault pop the last element
print(my_dict)




