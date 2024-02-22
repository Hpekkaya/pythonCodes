fruits =["apples", "bananas","cherry"]
new_fruits =[]

for f in fruits: 
    print((f.capitalize()+"-")*3)
    new_fruits.append(f.capitalize())

print("")
print(new_fruits)

[print(f.capitalize()) 
 for f in fruits]