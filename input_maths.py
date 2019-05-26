hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
   h = float(hrs)
   r = float(rate)
except:
    print("Error, please enter a numeric value")
    quit()

if h > 40:
    exhrs = h - 40
    ot = r * 1.5
    overtime = exhrs * ot
    pay = (h - exhrs) * r + overtime
else:
    pay = h * r

print(pay)