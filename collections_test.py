# global vars
from config import developer




# functions

def print_menu():
    print('---------------------')
    print('---- PySoft 3000 ----')
    print('---------------------')



def dictionary_1():
    pet = {
        "type": "rabbit",
        "name": "luna",
        "color": "white",
        "age": 2
    }

    print(pet)
    # read
    print("My pet is: " + pet["name"])
    # modify
    pet["age"] = 3
    # add
    pet["size"] = "small"
    # remove
    pet.pop("type")
    print(pet)


def dictionary_2():
    print(developer)

    # 1 - print the full name like: first last
    
    print(developer["first"] + " " + developer["last"])

    # 2 - print the full address: street #, city

    address = developer["address"]
    print(address)

    print(developer["address"])
    print(developer["num"] + " " + developer["street"] + ", " + developer["city"])

    location = {
        "num": 1017,
        "street": "athens",
        "city": "raleigh",
    }

    print(developer["location"])



# plain instructions
# function calls
print_menu()

dictionary_1()
dictionary_2()
