f = open('code','r')

possible = 0

for line in f:
    count = 0
    split = line.strip().split(' ')

    if int(split[0]) + int(split[2]) > int(split[4]):
        count += 1 
    if int(split[2]) + int(split[4]) > int(split[0]):
        count += 1 
    if int(split[0]) + int(split[4]) > int(split[2]):
        count += 1 
    if count == 3:
        possible += 1

print(possible)
