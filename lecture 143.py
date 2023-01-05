def total(a,b):
    return a+b

def all_total(*args):
    total = 433
    for num in args:
        total += num
        return total
print(all_total(1,2,3))

