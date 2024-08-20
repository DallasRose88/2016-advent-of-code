TLS = 0

for line in f:
    replace2= line.replace('\n', '')
    replace = replace2.replace(']','[')
    split = replace.split('[')
    good = 0
    bad = 0
    x = 0
    while x < len(split):
        t = 0
        while t < len(split[x])-3:
            if x == 0 or x%2 == 0:
                if (split[x][t]) == split[x][t+3]:
                    if split[x][t +1] == split[x][t+2]:
                        if split[x][t] != split[x][t+1]:
                            good += 1 
            else:
                if (split[x][t]) == split[x][t+3]:
                    if split[x][t +1] == split[x][t+2]:
                        if split[x][t] != split[x][t+1]:
                            bad += 1 
            t += 1 
        x += 1
    if good > 0 and bad == 0:
        TLS += 1
print('Part 1', TLS)
