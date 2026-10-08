
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

# write a program that returns the factors of given number 
def factors_of_number(num):
    result =[]
    # for i in range(1,num+1):
    # for i in range(1,num//2):
    for i in range(1,int(math.sqrt(num))):
        if num % i ==0:
            result.append(i)
            if i != num//i:
                result.append(num//i)
    # result.append(num)
    return result
# return the frequecy in dictinry.  
def frequecy_dict(arr):
    hashmap ={}
    for i in  arr:
        # if i in hashmap:
        #     hashmap[i] = hashmap[i] +1
        # else:
        #     hashmap[i] = 1
        hashmap[i] = hashmap.get(i,0)+1
    return hashmap

arr = [1,2,2,1,3]

n=36
print("sum of digits is: ",sum_of_digits(n))
print("count of digits is: ",count_digits(n))
print("check palindrome number: ",check_palindrome_number(n))
print("check armstrong number: ",armstrong_number(n))
print("factors of  number: ",factors_of_number(n))
print("frequency of numbers: ",frequecy_dict(arr))


a = 