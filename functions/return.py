# Use of return
x = 20
y = 10

def add(x, y):
    a = x + y
    return a

def sub(x, y):
    a = x - y
    return a

def div(x, y):
    a = x / y
    return a

def mul(x, y):
    a = x * y
    return a

print (f"The addition is {add(x,y):.2f}, the subtraction is {sub(x,y):.2f}, the multiplication is {mul(x,y):.2f} and the division is {div(x,y):.2f}")

def name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = name("lord", "hamza")
print(full_name)