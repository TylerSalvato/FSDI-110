

def test1():
    students = []

    # add
    students.append("Glenda")
    students.append("Eduardo")
    students.append("Irvin")

    print(students)

    # count
    print(len(students))

    # read by index
    print(students[0])

    # read all
    for student in students:
        print(student)


def test2():
    prices = [12,43,2,4,67,132,7,45,13,7,56,3,63,56,40,72]

    # print all numbers
    for num in prices:
        if(num < 50):
            print(num)



# call functions
test1()

test2()