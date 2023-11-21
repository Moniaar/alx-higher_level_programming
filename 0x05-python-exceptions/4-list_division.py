#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Divres = []
    for i in range(list_length):
        try:
            # Try to perform the division
            operation = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by 0
            print("division by 0")
            operation = 0
        except IndexError:
            # Handle index out of range
            print("out of range")
            operation = 0
        except (TypeError, ValueError):
            # Handle wrong type (non-integer or non-float)
            print("wrong type")
            operation = 0
        finally:
            # Append the result to the new list
            Divres.append(operation)

    return Divres
