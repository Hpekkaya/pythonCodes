fruits =["apples", "bananas","cherry"]
new_fruits =[]

# [print(f.capitalize()) for f in fruits]
new_fruits =[f.upper() for f in fruits]
print(new_fruits)

for i in range(len(new_fruits)): 
    print(i+1, ":", (new_fruits[i]))
    



