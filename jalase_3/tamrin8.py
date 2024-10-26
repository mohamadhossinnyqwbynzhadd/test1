
input_data = input("pleas enter a list of tuples (e.g., [(1, 2),(3, 1),(5, 0)]:) ")

tuple_list = eval(input_data)

sorted_list = []

while tuple_list:
    min_tuple = tuple_list
    for t in tuple_list:
        if t[1] < min_tuple[1]:
            min_tuple = t
    sorted_list.append(min_tuple)
    tuple_list.remove(min_tuple) 

print("sorted list:", sorted_list)           