#functionns

def add(a,b):
    return a + b
print("the sum of two values is ",add(2,4))

#default function arguments

def multiply(a,b=2):
    return a * b
print("the multiplication of two values is ",multiply(3))

#no arguments no return
def wish():
    print("I am wishing you a very happy birthday!")

wish()

#with arguments no return
def greet(name):
    print(f"Hello,{name}! Welcome to India")
greet("Saicharan")

#with arguments with return
def square(value):
    return value * value
square(6)
print("the square of the value is ",square(6))

#keyword arguments
def greet(name, message):
    print(f"hello {name} ,  {message}.have a nice day!")

greet (name="Saicharan", message="Good morning!")
