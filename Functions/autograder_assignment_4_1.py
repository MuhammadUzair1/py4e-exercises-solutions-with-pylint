'''
This program calculates the pay of an employee based on the number of hours worked 
and the rate per hour using function.
'''

def computepay(h,r):
    '''Calculate pay based on hours worked'''
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hr = float(input("Enter Hours:"))
rphr = float(input("Enter rate per hour:"))

pay = computepay(hr,rphr)
print('Pay',pay)
