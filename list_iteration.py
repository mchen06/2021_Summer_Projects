list_1 = [2, 5, 12, 23, 7, 19, 32]
length = len(list_1)
for x in range(0, length):
    y = list_1[x]
    if y < 10:
        print("small")
    if y >= 10 and y =< 20:
            print("medium")
    if y > 20:
        print("large")
