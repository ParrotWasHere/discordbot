import random
import time

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def set_time(time):
    time.sleep(time)
    return('Tempo!')
