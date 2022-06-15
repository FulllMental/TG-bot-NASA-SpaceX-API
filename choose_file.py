import os
import random

def choose_file():
    all_dirs = ['images', 'NASA']
    directory = random.choice(all_dirs)
    response = [i for i in os.walk(f'{os.getcwd()}\{directory}')]
    picture = random.choice(response[0][2])
    return directory, picture