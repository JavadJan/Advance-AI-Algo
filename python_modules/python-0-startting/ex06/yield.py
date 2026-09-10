def counter():
    print("starting")
    yield 1
    print("resumed after first yield")
    yield 2
    print("resumed after second yield")
    yield 3
    print("function ending")




gen = counter()

input("press enter 1")

print(next(gen))

#print("generator created, nothing printed yet")

input("press enter 2")
print(next(gen))

input("press enter 3")
print(next(gen))