line = 'From den.mcc@email.com Sat Jan 18  09:54:23 2020'
words = line.split()
print(words)
piece = words[1].split('@')
print(piece)
print(piece[1])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))