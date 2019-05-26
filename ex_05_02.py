largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        ival = int(num)
        if smallest is None or ival < smallest:
            smallest = ival
        if largest is None or ival > largest:
            largest = ival
    except:
        print('Invalid input')
        continue

print("Maximum is", int(largest))
print("Minimum is", int(smallest))

