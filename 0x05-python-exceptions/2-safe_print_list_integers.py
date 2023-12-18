#!/usr/bin/python3

def safe_print_list_integers(my_list, max_index):
    printed = 0
    for i in range(max_index):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        except IndexError:
            break
    print()
    return (printed)
