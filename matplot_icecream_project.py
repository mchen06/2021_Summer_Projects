import matplotlib.pyplot as plt
import pandas as pd

def seperate_data(file):
    full_list = pd.read_csv(file)
    list_1 = []
    print(full_list.keys)
    keys = full_list.keys
    print(type(keys))
    length = len(keys)
    
    for x in range(0, length):
        key = keys[x]
        append = full_list[key]
        list_1.append(append)
    
    x = full_list["id"]
    list_1.append(x)
    print(type(list_1))
    print(list_1)


def run_program():
    seperate_data('/Users/mileychen/Downloads/Ice_cream_R.csv')



