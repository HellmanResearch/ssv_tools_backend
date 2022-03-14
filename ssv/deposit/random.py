
import random


def get_password():
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected = [random.choice(characters) for i in range(10)]
    password = "".join(selected)
    return password


def get_dir_name():
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected = [random.choice(characters) for i in range(50)]
    dir_name = "".join(selected)
    return dir_name