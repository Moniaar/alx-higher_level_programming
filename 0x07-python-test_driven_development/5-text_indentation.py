#!/usr/bin/python3
"""Module for a method that adds new lines after certain chars"""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
