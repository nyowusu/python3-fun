##  create a dictionary from a list of lists

keys = list(range(1, 5))
values = ["one", "two", "three", "four"]

for key, value in zip(keys, values):
    print((key, value))

my_dict = dict(zip(keys, values))

for key in my_dict:
    print((key, my_dict[key]))
