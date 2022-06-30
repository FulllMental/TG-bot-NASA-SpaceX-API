import os
directory = 'images'


def choose_file():
    response = [i for i in os.walk(fr'{os.getcwd()}\{directory}')]
    pictures_list = response[0][2]
    return pictures_list
