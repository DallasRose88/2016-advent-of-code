f = open('Trial','r')

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
for line in f:
    one.append(line[0])
    two.append(line[1])
    three.append(line[2])
    four.append(line[3])
    five.append(line[4])
    six.append(line[5])
    seven.append(line[6])
    eight.append(line[7])
count = 1000
letter1 = 'p'
print(one)
for x in one:
    m = one.count(x)
    if m < count:
        print(count)
        count = m
        letter1 = x 
count = 1000
letter2 = ''
for x in two:
    m = two.count(x)
    if m < count:
        count = m
        letter2 = x 
count = 1000
letter3 = ''
for x in three:
    m = three.count(x)
    if m < count:
        count = m
        letter3 = x 
count = 1000
letter4 = ''
for x in four:
    m = four.count(x)
    if m < count:
        count = m
        letter4 = x 
count = 1000
letter5 = ''
for x in five:
    m = five.count(x)
    if m < count:
        count = m
        letter5 = x 
count = 1000
letter6 = ''
for x in six:
    m = six.count(x)
    if m < count:
        count = m
        letter6 = x 
count = 1000
letter7 = ''
for x in seven:
    m = seven.count(x)
    if m < count:
        count = m
        letter7 = x
count = 1000
letter8 = ''
for x in eight:
    m = eight.count(x)
    if m < count:
        count = m
        letter8 = x 
print(letter1,letter2,letter3,letter4,letter5,letter6,letter7,letter8)
