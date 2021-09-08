# chapter1

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

# chapter2

# def quick_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr

def quick_sort(arr):
    for x in arr:
        for y in arr:
            if x < y:
                x,y=y,x
    return arr


arr = [2,5,6,1,2,3,6,11,35,4]