name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()

for line in handle:
    if line.startswith("From "):
        line = line.split()
        sender[line[1]] = sender.get(line[1],0) +1

mostsender = None
mostsendervalue = None

for k,v in sender.items():
    if mostsendervalue is None or mostsendervalue < v:
        mostsendervalue = v
        mostsender = k

print(mostsender, mostsendervalue)