def fib_gen(num):
    a = 0
    b = 1
    counter = 0
    while counter < num:
        a, b = b, a + b
        yield b
        counter += 1


for index in fib_gen(10):
    print(index)
