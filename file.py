with open('hello.py', 'w') as f:
    f.write('print("hello world!")')

with open('hello.py', 'r') as f:
    exec(f.read())

numbers = [1, 2, 3, 4]
with open('numbers.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + '\n')
with open('numbers.txt', 'r') as f:
    print(f.read())
