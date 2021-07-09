x = [
    10, [3.141, 20, [30, {"computer": "hp", "shop": "Ibrahims"}, 2.718]], 'foo']
print(x[2])


x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x': 10,
            'y': 20,
            'z': 30
        },
        'baz': 3
    },
    'c',
    'd'
]
print(x[2]["bar"]["z"])


task = [23, "jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76,"John")]
print(type(task))
print(task[2][1])
print(len(task))

x=str(task[3])[::-1]
print(x)

task[3]=int(x)
print(task[3])

# assignment
# print(task[3])
# task[3]="789"
# reversed
# print(task[3])
# print(task[1])
# task[1]="john"
# print(task[1])

# join
# task[3]="987"
# reversed=''.join(reversed(task[3]))
# print(reversed)

# this is my change








