# Tuple is a collection which is ordered and unchangeable(diff Lists). Allows duplicate members.

my_tuple=("Max", 28, "Boston")  # () is optinal

my_tuple1=tuple(["Max", 28, "Boston"])
print(my_tuple)

# Accessing Index
item = my_tuple[1]
item1= my_tuple[-1]

print(item)
print(item1)

# Assignment : tuple' object does not support item assignment
my_tuple[0]="Dav" #Returns error. since tuples immutable


