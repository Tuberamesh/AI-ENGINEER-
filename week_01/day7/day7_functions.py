# def calculate_total(price, quantity):
#     total = price * quantity
#     return total


# result = calculate_total(499, 13)

# print(result)



# def calculate_total(price, quantity):
#     return price * quantity

# def greet(name, message="Hello"):
#     print(message, name)

# print(calculate_total(500, 3))

# greet("Ramesh")
# greet("Ramesh", "Welcome")


# def add(*args):
#     total = 0

#     for number in args:
#         total += number

#     return total


# print(add(10, 20))
# print(add(10, 20, 30, 40))

# def create_user(**kwargs):
#     print(kwargs)

    
# create_user(name="Ramesh", age=20, city="Bengaluru")


def show_user(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


show_user(name="Ramesh", age=20, city="Bengaluru")