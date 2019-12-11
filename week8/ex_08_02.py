t = [2, 6, 77, 99, 103, 1, 9]

print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t)/len(t))

numlist= list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
