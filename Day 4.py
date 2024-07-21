import numpy

f = open('Trial','r')

IDS = 0 
for x in f:
    m = x.replace('-',' ')
    split = m.split('[')
    b = split[0]
    times = []
    letters = []
    for letter in b:
        if letter.isalpha():
            num = b.count(letter)
            if num != 0:
                times.append(num)
                letters.append(letter)
                b = b.replace(letter,'')

    code = []
    s = 0
    while s < 5:
        d = max(times)
        lst = numpy.array(times)
        a = numpy.where(lst == int(d))[0]
        length = len(a)
        if length == 1:
            index = int(a)
            code.append(letters[index])
            times[index] = 0
            s += 1 
        else:
            poss = []
            yo = 0
            while yo < len(a):
                g = a[yo]
                poss.append(letters[g])
                times[g] = 0
                yo += 1 
            order =sorted(poss)
            for let in order:
                if len(code) < 5:
                    code.append(let)
            s += length
    if code == list(split[1][:-2]):
        r = (split[0][-3:])
        IDS += int(r)
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        name = ''
        for letter in split[0]:
            if letter.isalpha():
                shift_pos = alphabet.index(letter)
                moves = int(r) % 26
                name+=str(alphabet[shift_pos + moves])
            else:
                name+=str(' ')
        if 'north' in name and 'pole' in name: 
            print('Part 2',r)
print('Part 1', IDS)
