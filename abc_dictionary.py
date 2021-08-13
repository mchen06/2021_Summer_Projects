d1 = {'a' : 100, 'b' : 200, 'c' : 300, 'e' : 700}
d2 = {'a' : 300, 'b' : 200, 'c' : 400, 'd' : 500}
d3 = {}

for key in d1:
    if key in d2:
        x = d1 [key]
        y = d2 [key]
        z = x + y
        d3 [key] = z
    else:
        x = d1 [key]
        d3 [key] = x
for key in d2:
    if key in d3:
       pass
    else:
        x = d2 [key]
        d3 [key] = x
print(d3)

    
