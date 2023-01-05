def num_to_string(l):
    return[str(i) for i in l if (type(i) == int or type(i) == float) ]


print(num_to_string([True, False , [9,4,3], 7, 5.0, 3]))