
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