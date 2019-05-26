largest_so_far = 1
print('Before', largest_so_far)
for the_num in [9,41,12,2,74,15,88,34,22,4,6,7,888,90]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
