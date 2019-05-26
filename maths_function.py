def computepay(h,r):
   if h > 40:
       exhrs = h - 40
       ot = r * 1.5
       overtime = exhrs * ot
       total = (h - exhrs) * r + overtime
   else:
        total = h * r
   return total

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print(p)

