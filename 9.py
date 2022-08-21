def even_numbers (x,y):
    even_list = []
    for i in range(x,y):
        if i % 2 == 0:
            even_list += [i]
    return even_list

print(even_numbers(1,10))