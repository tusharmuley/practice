
def func1(count):
    if count == 0:
        return
    print("tushar")
    func1(count-1)
    
func1(4)

def func4(i,n):
    if i >n:
        return
    func4(i+1,n)
    print(i)
    
func4(1,4)

def func2(sum,i,n):
    if i>n:
        print(sum)
        return
    sum+=i
    func2(sum,i+1,n)
func2(0,1,10)

def func3(n):
    # print(n)
    if n ==1:
        return 1
    return n+ func3(n-1)
    

print(func3(4))



# print factorial of a number using recursion
def factorial(no):
    if no ==1:
        return 1
    return no*(factorial(no-1))

print("factorial of 5 is: ",factorial(5))



#Reverse an array using recursion

def reverse(arr, left, right):
    if left >= right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse(arr,left+1, right-1)
    return arr


arr=[1,2,3,4,5,5,6]
print("reverse array is:",reverse(arr,0,len(arr)-1))


def reverse1(arr,left,right):
    while left<=right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    
    return arr 

print("reverse using while loop",reverse1(arr,0,len(arr)-1))