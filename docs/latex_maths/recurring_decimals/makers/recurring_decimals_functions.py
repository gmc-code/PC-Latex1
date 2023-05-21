"""
Module of functions to return decimals dictionary for LaTeX
"""
import random


def get_rec_dec_dict(num, numdp):
    if num is None or num == 3:
        num = random.randint(1, 2)
    match num:
        case 1:
            return add_dict(numdp)
        case 2:
            return sub_dict(numdp)
    

def rec_dec_dict(numdp):
    # na + nb = nc
    # Generate a random decimal number between 0.01 and 100
    na = random.uniform(0.001, 100)
    nb = random.uniform(0.001, 100 - na)
    # Format the result to 1,2 or 3 decimal places
    format_string = "{:." + str(numdp) + "f}"
    na = format_string.format(na)
    nb = format_string.format(nb)
    nc = float(na) + float(nb)
    nc = format_string.format(nc)
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = f"+"
    kv["answer"] = f"{nc}"
    return kv

