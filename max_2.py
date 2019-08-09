def sumDigit(num):
    sum = 0
    while(num):
        sum += num%10
        num = num/10
    return sum
print('maximum value is', max(4,454,1109,980,889,key = sumDigit))
        
