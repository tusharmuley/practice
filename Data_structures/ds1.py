
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

def check_palindrome_number(num):
    n=num
    result = 0
    while num >0:
        last_digit = num%10
        result = (result*10) + last_digit
        num = num//10
        
    if n == result:
        return True 
    else :
        return False

def armstrong_number(num):
    n=num
    total =0
    nod= len(str(n))
    while n > 0:
        last_digit = n%10
        total += last_digit**nod
        n=n//10
    if num == total:
        return True
    else:
        return False
      
    
    
    
n = 153
print("sum of digits is: ",sum_of_digits(n))
print("count of digits is: ",count_digits(n))
print("check palindrome number: ",check_palindrome_number(n))
print("check armstrong number: ",armstrong_number(n))
