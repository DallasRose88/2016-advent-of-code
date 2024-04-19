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
    
