"""
Module of functions to return decimals dictionary for LaTeX
"""
import random


def get_add_sub_dec_dict(num, numdp):
    if num is None or num == 3:
        num = random.randint(1, 2)
    match num:
        case 1:
            return add_dict(numdp)
        case 2:
            return sub_dict(numdp)
    

def add_dict(numdp):
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


def sub_dict(numdp):
    # na + nb = nc
    # Generate a random decimal number between 0.01 and 100
    nc = random.uniform(0.001, 100)
    nb = random.uniform(0.001, 100 - nc)
    # Format the result to 1,2 or 3 decimal places
    format_string = "{:." + str(numdp) + "f}"
    nc = format_string.format(nc)
    nb = format_string.format(nb)
    na = float(nc) + float(nb)
    na = format_string.format(na)
    #   
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = f"-"
    kv["answer"] = f"{nc}"
    return kv


def times_dict():
    # na + nb = nc
    # Generate a random decimal number between 0.01 and 100
    na = random.uniform(0.01, 100)
    nb = random.uniform(0.01, 100 - na)
    # Format the result to 2 decimal places
    na = "{:.2f}".format(na)
    nb = "{:.2f}".format(nb)
    nc = float(na) + float(nb)
    nc = "{:.2f}".format(nc)
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = f"+"
    kv["answer"] = f"{nc}"
    return kv


def div_dict():
    # na + nb = nc
    # Generate a random decimal number between 0.01 and 100
    na = random.uniform(0.01, 100)
    nb = random.uniform(0.01, 100 - na)
    # Format the result to 2 decimal places
    na = "{:.2f}".format(na)
    nb = "{:.2f}".format(nb)
    nc = float(na) + float(nb)
    nc = "{:.2f}".format(nc)
    kv = dict()
    kv["num1"] = f"{na}"
    kv["num2"] = f"{nb}"
    kv["process"] = f"+"
    kv["answer"] = f"{nc}"
    return kv

