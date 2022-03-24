
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")


def nickname(firstName, lastName):
    sayHello = print("Hello ", firstName, lastName)
    return sayHello
    
nickname(firstName, lastName)