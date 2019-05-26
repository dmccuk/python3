largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
        if smallest is None or n < smallest:
            smallest = n
        if largest is None or n > largest:
            largest = n
    except ValueError:
        # num cannot be converted to an int
        print ("Invalid input")

print("Smallest is", smallest)
print("Largest is", largest)