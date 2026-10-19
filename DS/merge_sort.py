

# write a Program to merge two array in sorted order 

def merge_array(left, right):
    result =[]
    i,j=0,0
    n,m=len(left),len(right)
    while i < n and j < m :
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def sort_arr(arr):
    if len(arr)== 1:
        return arr
    
    mid=len(arr)//2
    left_arr = arr[:mid]
    right_arr= arr[mid:]
    left_sorted = sort_arr(left_arr)
    right_sorted=sort_arr(right_arr)
    return merge_array(left_sorted,right_sorted)
    


# left_arr=[1,3,5,6]
# right_arr=[7,8,9,11]

# print(merge_array(left_arr,right_arr))

array=[1,4,3,6,4,8,8,2,3]
print(sort_arr(array))