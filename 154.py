def is_even(a):
    return a%2 == 0

print(is_even(5))

iseven2 = lambda a : a%2==0
print(iseven2(6))

def last_chr(s):
    return s[-1]

last_char = lambda s : s[-1]
print(last_chr('Ranjeet'))

def func(s):
    return  len(s) > 5
func = lambda s : True if len(s) > 5 else False
print(func('abcdefg'))

    
