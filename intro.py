
print('Hello World!')

# this is a comment

# Variables

first_name = "Tyler"
last_name = 'Salvato'

total = 9.99
age = 99
found = False
print(first_name)
print(last_name)
print(total)

print(9 + 1) # sum
print("9" + '1') # str concatenation

# math
print(10 + 1)
print(10 - 1)
print(10 * 10)
print(10 / 2)

# if

if age < 100:
    print("Don't worry you are young")
    print('Still inside the if')
    print("Still inside 2")
elif age == 100:
    print("Congratulations on the Century")
else:
    print('Sorry buddy, you are getting old')


print('Outside')

def say_hello(name):
    print("Hello from a function " + name)

# call fns
say_hello("Juan")
say_hello("Jane")
