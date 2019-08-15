'''Sort'''
# Merge Sort(used recursion)
from arrays import Array
## recursion function
def mer_fun(lyst, ary, low, high):
    if low<high:
        mid = (low+high)//2
        mer_fun(lyst, ary, low, mid)
        mer_fun(lyst, ary, mid+1, high)

## merge small arrays to a large array
def mer(lyst, ary, low, mid, high):
    x, y = low, mid+1
    for i in range(low, high+1):
        if x>mid:
            ary[i] = lyst[y]
            y += 1
        elif y>high:
            ary[i] = lyst[x]
            x += 1
        elif lyst[x]<lyst[y]:
            ary[i] = lyst[x]
            x += 1
        else:
            ary[i] = lyst[y]
            y += 1
    for i in range(low, high+1):
        lyst[i] = ary[i]

## main process
def mer_sor(l):
    copy_arrray = Array(len(l))
    mer_fun(l, copy_arrray, 0, len(l)-1)

# Quick Sort
def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

# Insertion Sort


# Bubble Sort


# Selection Sort


# Heap Sort



'''Binary Search'''
# for Ordered Array
def bi_sea(target, ord_ary):
    low, high = 0, len(ord_ary)-1
    
    while low<=high:
        mid = (low+high)//2
        if ord_ary[mid]==target:
            return mid
        elif ord_ary[mid]<=target:
            low = mid+1
        elif ord_ary[mid]>=target:
            high = mid-1
    return -1
    

# Fuzzy Binary Search
def fuzzy_bi_sea(target, ord_ary):
    low, high = 0, len(ord_ary)-1
    if target>ord_ary[high]:
        return -1
    if target<ord_ary[low]:
        return 0
    while low<=high:
        mid = (low+high)//2
        if ord_ary[low]<target<ord_ary[mid]



if __name__ == "__main__":
    target, ord_ary = 10, [1,2,4,5,7,9,10,10,14,15,17]
    assert bi_sea(target, ord_ary)==6, 'bi_sea is not true'
    assert fuzzy_bi_sea(target, ord_ary)==8, 'fuzzy_bi_sea is not true'
    print('ALL tests passed')
    pass