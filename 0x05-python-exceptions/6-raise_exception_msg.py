#!/usr/bin/python3
def raise_exception_msg(message=""):
    class NameException(Exception):
        pass

    raise NameException(message)
