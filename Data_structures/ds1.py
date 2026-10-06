
import math
def sum_of_digits(num):
    total=0
    while num > 0:
        last_digit = num%10
        # print(last_digit)
        num = num //10
        total +=last_digit
        # break
        
    return total
def count_digits(num):
    count=0
    # return int(math.log10(num) +1)
    while num > 0:
        num = num//10
        count+=1
        
    return count


n = 587367
print("sum of digits is: ",sum_of_digits(n))
print("count of digits is: ",count_digits(n))
