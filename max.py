def sumDigit(num):
    sum = 0
    while(num):
        sum += num%10
        num = int(num/10)
    return sum
# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))
num = 15, 300, 2700, 821, 52, 10, 63w 8v
print('Maximum is:', max(num, key=sumDigit))
