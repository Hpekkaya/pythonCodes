#Strings ordered, immutable, text representation

# my_string = "Hello World"
# my_string[8] = "T"  #TypeError: 'str' object does not support item assignment
# my_string = "Hello Turkey"  #Support assignment 
# print(my_string)

# sub_string = my_string[3:9]
# print(sub_string)

# sub_string2 = my_string[6::2] #from 6 Step 2
# print(sub_string2)

# sub_string3 = my_string[4::] #from 4 Step 1 (Default)
# print("3 :", sub_string3)

# sub_string4 = my_string[::-1] #Reverse
# print("4 :", sub_string4)

#String Iteration
greeting = "Hello "
name = "Hakan"

sentence = greeting + " " + name
print(sentence)

# for i in greeting:
#     print(i)
    
# if "e" in sentence:
#     print("Yes")
# else : print("No")

# my_string = "    Hello   "
# my_string= my_string.strip() #remove the space at the beginning and end

# print(my_string)
# print(my_string.upper())
# print(my_string.lower())
# print(my_string)
# my_string = my_string.upper()
# print(my_string)

# my_string = "Hello World"
# print(my_string.startswith("H")) 
# print(my_string.endswith("d")) 

# print(my_string.find("llo")) 
# print(my_string.find("k")) # If there is not returns -1

# print(my_string.count("l")) 

# print(my_string.replace("World","Dears"))

my_string = "How are you doing ?"
my_list = my_string.split()  #Split into words
print(my_string, my_list)

my_string1 = "How, are, you, doing ?"
my_list1 = my_string1.split()  #Split into words and ","
my_list11 = my_string1.split(",")  #Split into words and ","
print(my_string1, my_list11)




