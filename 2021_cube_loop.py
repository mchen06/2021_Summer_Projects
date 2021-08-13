cube = input("pick a number: ")
cube = int(cube)
cube = cube + 1
x = 0
for i in range(1, cube):
    i = i**3
    x = x + i
print(x)



