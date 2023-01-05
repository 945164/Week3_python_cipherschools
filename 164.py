names = ['Ranjeet Gupta', 'Ritik', 'ab', 'z']
print(max(names, key = lambda item : len(item)))

students = {
    'Ranjeet' : {'score':90, 'age':24},
    'Ritik' : {'score':75, 'age':19},
    'Rahul' : {'score':76, 'age':25}
}

students2 = [
    {'name':'Ranjeet', 'score':90, 'age':24},
    {'name':'Ritik', 'score':70, 'age':19},
    {'name':'Rohit', 'score':60, 'age':25}
]
print(max(students2, key = lambda item:item.get('age'))['name'])


