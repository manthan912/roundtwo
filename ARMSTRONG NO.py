# function to calculate a raised to power b
def power(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    return a * power(a, b-1)

#function to calculate order of the number
def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = int(x / 10)
    return n

# Function to check whether the given number is
# Armstrong number or not
def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10

        sum1 = sum1 + power(r, n)
        temp = int(temp/10)
    return sum1 == x

# driver Program
z = 153
if isArmstrong(z):
    print(z,"is a ARMSTRONG NUMBER")
else:
    print(z, "is a NOT ARMSTRONG NUMBER")


