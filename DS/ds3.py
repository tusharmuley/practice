
def largest(arr):
    # largest=arr[0]
    largest=float("-inf")
    sec_largest=float("-inf")
    for i in range(len(arr)):
        if arr[i] >largest:
            sec_largest = largest
            largest=arr[i]
        elif arr[i]>sec_largest and arr[i] != largest:
            sec_largest=arr[i]
    
    return largest, sec_largest




arr = [3,4,5,5,66,44,22]
print(largest(arr))