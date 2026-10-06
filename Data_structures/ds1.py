

def sum_of_digits(num):
    total=0
    while num > 0:
        last_digit = num%10
        # print(last_digit)
        num = num //10
        total +=last_digit
        # break
        
    return total
n = 5873
print("sum of digits is: ",sum_of_digits(n))
