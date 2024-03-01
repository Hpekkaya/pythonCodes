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

# Point = namedtuple("Point", "x,y")
# pt = Point(-1, 4)
# print(pt)
# print(pt.x, pt.y)


from collections import OrderedDict

# # OrderdDict ***************
# ordered_dict = OrderedDict()
# ordered_dict["a"] = 1
# ordered_dict["b"] = 2

# ordered_dict["c"] = 3
# ordered_dict["d"] = 4
# ordered_dict["a"] = 5

# print(ordered_dict)

from collections import defaultdict

# d = defaultdict(float)  #Can be int, list
# d["a"] = 1
# d["b"] = 2
# print(d)
# print(d["a"], d["b"])
# print(d["c"])  # If not assigned, Default value 0, if float 0.0

# d = defaultdict(list)
# d["a"] = 1
# d["b"] = 2
# print(d)
# print(d["a"], d["b"])
# print(d["c"])  # If not assigned, Default value []

# d = defaultdict(list)

# for i in range(5):
#     d[i].append(i)

# print("Dictionary with values as list:")
# print(d)


from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extendleft([4, 5, 6, 8])
print(d)

d.reverse()
print(d)

d.rotate(6)
print(d)
