from ctypes import sizeof
import random


def password_genrator(t_num =5, size = 10, string_size = 5):

    total_password_size = size
    total_int = t_num
    string_size = 5

    password = random.randint(total_int) +