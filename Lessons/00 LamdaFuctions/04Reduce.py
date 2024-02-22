import functools



add =functools.reduce( lambda x,y: x + y, range(1,10))
          

print(add)
