umbers = [int(y) for y in input("pleas enter your list:(pleas split numbers)").split()]n
squared_numbers = list(map(lambda y: y**2, numbers))
print("list of powers of two", squared_numbers)