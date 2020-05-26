from time import time
values = {}


while True:
    n = int(input())
    t = int(1000*time())
    values[t]=n
    for key in list(values.keys()):
        if t - key > 30000:
            del values[key]
    print(values.values())
