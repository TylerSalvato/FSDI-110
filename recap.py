

def variables():
    status = "found"
    price = 212.99

    print(status)

    if price > 99:
        print("but it's expensive")

def say_hi(name):
    print("Hi " + name)

def sum(num1, num2):
    result = num1 + num2
    print("The result is " + str(result))


# division receive 2 params
# if num2 is zerop, it should an error
# otherwise, divide and show result

def divide(num1, num2):
    if num2 == 0:
        print("Error: you can not divide by zero")
    else:
        result = num1 / num2
        print("The result is " + str(result))


def sum_all_numbers():
    numbers = [3123,509,-23,45,1405,44,-2456,45,1234,778,1124,70,2956,82]

    # print each number on a line
    count = 0
    total = 0
    for num in numbers:
        total+= num
        
        if num < 100:
            count += 1
            print(num)
            
    # print numbers that are lower than 100
    # count how many numbers are lower than 100
    # sum all numbers
    print("The result is: " + str(count))
    print("The result is: " + str(total))






# calls
variables()

say_hi("Cool name")
say_hi("Forrest Gump")

sum(21, 21)

divide(10, 2)
divide(-19, -2)
divide(-10, 2)
divide(10, -2)
divide(0, 2)
divide(2, 0)


sum_all_numbers()