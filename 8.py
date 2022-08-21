def three_dividends (x,y):
    three_dividends_list = []
    for i in range(x,y):
        if i % 3 == 0:
            three_dividends_list += [i]
    return three_dividends_list

print(three_dividends(1,50))