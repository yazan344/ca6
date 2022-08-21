def last_two(astring):
    if len(astring) < 2 :
        return "Error"
    else :
        return tuple(astring[-2:])

print(last_two("hi how's it going"))