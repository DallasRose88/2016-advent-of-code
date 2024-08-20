split = f.split(', ')

x = 0 
y = 0 

for line in split:
    if line[0] == 'R':
        x,y = -y,x
    else:
        x,y = y,-x 
    x += int(line[1:])
print("Part 1 ", abs(x) + abs(y))
