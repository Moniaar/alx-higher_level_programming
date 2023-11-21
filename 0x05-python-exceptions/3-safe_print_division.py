#!/usr/bin/python3
def safe_print_division(a, b):
    Divres = 0

    try:
        Divres = a / b
    except ZeroDivisionError:
        Divres = None
    finally:
        print('Inside result: {}'.format(Divres))
        return Divres
