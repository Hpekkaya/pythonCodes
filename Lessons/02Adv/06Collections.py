#  Collections: counter, namedTuple, orderdDict, defaultDict, deque

# from collections import Counter

# # Conter ***************
# a = "aaabbbbccccccddeeeeeee"
# my_counter = Counter(a)

# print(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][1])
# print(list(my_counter.elements()))

from collections import namedtuple

# # namedtuple ***************

Point = namedtuple("Point", "x,y")
pt = Point(-1, 4)
print(pt)
print(pt.x, pt.y)


from collections import OrderedDict

# # OrderdDict ***************
