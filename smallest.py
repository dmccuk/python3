smallest = None
print('Before')
for value in [9,41,12,2,74,15,88,34,22,1,6,7,888,90]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print('After', smallest)