fname = input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
fh = open(fname)
count = dict()
for line in fh:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


