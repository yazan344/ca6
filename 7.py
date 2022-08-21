def sum_or_max(my_list):
    if len(my_list) % 2 == 0:
        return print(sum(my_list))
    else:
        return print(max(my_list))

my_list = [5, 6, 10, 15, 95]

sum_or_max(my_list)