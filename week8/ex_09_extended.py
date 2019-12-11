fname = input('enter file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

largest = -1
theword = None

for k,v in di.items():
    #print(k,v)
    if v > largest:
        largest = v
        theword = k

print(theword, largest)
