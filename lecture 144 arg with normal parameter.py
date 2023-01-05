def multiply_nums(*args, num):
    multiply = 1
    #print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,4,3,4))