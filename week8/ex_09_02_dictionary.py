count = dict()
names = ['den', 'bob', 'den', 'steve', 'bob']
for name in names:
    count[name] = count.get(name, 0) +1
print(count)