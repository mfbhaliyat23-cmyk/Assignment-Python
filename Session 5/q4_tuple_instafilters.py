insta_filters = ("Clarendon", "Gingham", "Lark", "Lo-Fi")

insta_filters[1] = "Juno"
print(insta_filters)


"""
Comment for the Why Tuple gets an Error!!?

Answer : Tuple gets an error when we try to change the 2nd filter or item in the list,
        because tuple cannot be changed.
            It is unchangeable and it's a immutable data type.
        So,
            that's why it gets an typeerror : tuple - doesn't support item assignment.
"""