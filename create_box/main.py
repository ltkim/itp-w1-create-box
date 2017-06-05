"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    while height > 0:
       for x in range(0,width):
            box = box + character
       height = height - 1
       box = box + '\n'
    return box
