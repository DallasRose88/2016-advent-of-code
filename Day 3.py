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

f = open('code','r')

A = []
B = []
C = []

for line in f:
    split = line.strip().split(' ')
    A.append(int(split[0]))
    B.append(int(split[2]))
    C.append(int(split[4]))


possible = 0    
x = 0
while x < 1902:
    count = 0
    if A[x] + A[x+1] > A[x+2]:
        count += 1 
    if A[x+1] + A[x+2] > A[x]:
        count += 1 
    if A[x] + A[x+2] > A[x+1]:
        count += 1 
    if count == 3:
        possible += 1
    x += 3
x = 0
while x < 1902:
    count = 0
    if B[x] + B[x+1] > B[x+2]:
        count += 1 
    if B[x+1] + B[x+2] > B[x]:
        count += 1 
    if B[x] + B[x+2] > B[x+1]:
        count += 1 
    if count == 3:
        possible += 1
    x += 3
x = 0
while x < 1902:
    count = 0
    if C[x] + C[x+1] > C[x+2]:
        count += 1 
    if C[x+1] + C[x+2] > C[x]:
        count += 1 
    if C[x] + C[x+2] > C[x+1]:
        count += 1 
    if count == 3:
        possible += 1
    x += 3


print(possible)
