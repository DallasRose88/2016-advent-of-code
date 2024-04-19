f = open('trial','r')
start = 5
sequence = []
for line in f:
    x = line.strip()
    a = 0
    while a < len(x):
        if x[a] == 'U':
            if start == 1 or start == 2 or start == 3:
                a += 1
                continue 
            else:
                start -= 3 
        if x[a] == 'L':
            if start == 1 or start == 4 or start == 7:
                a += 1
                continue 
            else:
                start -= 1 
        if x[a] == 'R':
            if start == 3 or start == 6 or start == 9:
                a += 1
                continue  
            else:
                start += 1 
        if x[a] == 'D':
            if start == 7 or start == 8 or start == 9:
                a += 1
                continue
            else:
                start +=3 
        a += 1
    sequence.append(start)
print(sequence)
#part 2
f = open('trial','r')
start = 5
sequence = []
for line in f:
    x = line.strip()
    a = 0
    while a < len(x):
        if x[a] == 'U':
            if start == 1 or start == 2 or start == 4 or start == 5 or start ==9:
                a += 1
                continue 
            if start == 6 or start == 7 or start == 8 or start == 10 or start == 11 or start == 12:
                start -= 4
                a += 1
                continue
            if start == 3 or start == 13:
                start -= 2
                a += 1
                continue
        if x[a] == 'L':
            if start == 1 or start == 2 or start == 5 or start == 10 or start == 13:
                a += 1
                continue 
            else:
                start -= 1 
                a += 1
                continue
        if x[a] == 'R':
            if start == 1 or start == 4 or start == 9 or start == 12 or start == 13:
                a += 1
                continue  
            else:
                start += 1 
                a += 1
                continue
        if x[a] == 'D':
            if start == 5 or start == 9 or start == 10 or start == 12 or start == 13:
                a += 1
                continue
            if start == 2 or start == 3 or start == 4 or start == 6 or start == 7 or start == 8:
                start += 4
                a += 1
                continue
            if start == 1 or start == 11:
                start += 2
                a += 1
                continue
    if start == 10:
        sequence.append('A')
    if start == 11:
        sequence.append('B')
    if start == 12:
        sequence.append('C')
    if start == 13:
        sequence.append('D')
    if start < 10:
        sequence.append(start)
print(sequence)
    

    
