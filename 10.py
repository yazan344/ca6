def my_function (my_string):
    repeated_string = ""
    for char in my_string:
        repeated_string += char * 3
    print(repeated_string)

my_function("abc")