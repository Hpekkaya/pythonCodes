# Traditional Map Function

num=[1,2,3,4,5]

def count(x):
    y=x*2
    return y

add = map(count, num)

print(list(add))

# Lambda Map Function


add_L = map(lambda x:x*8,num)
print(list(add_L))

