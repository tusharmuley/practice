


def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
        


def bubble_sort(nums):
    n=len(nums)
    # print(nums)
    is_swap=False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
    if is_swap == False:
        return nums
    return nums


nums=[5,4,3,56,7,1,2,8,9]
# print(selection_sort(nums))
print(bubble_sort(nums))