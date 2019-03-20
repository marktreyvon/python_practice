# 各种排序算法
# 插入、冒泡、选择、归并、快排
# 需要注意的主要是：分而治之的思想、递归的应用

def insertSort(arr):
    flag = 0
    for i in range(len(arr)):

        pos = -1
        for j in range(0,i):
            pos = j
            if arr[j] > arr[i]:
                break
        if pos == i-1 and arr[i]>=arr[pos]:
            continue
        if not i:
            continue
        x = arr[i]
        arr.remove(arr[i])
        arr.insert(pos,x)

def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                (arr[i],arr[j]) = (arr[j],arr[i])

def selectSort(arr):
    for i in range(len(arr)):
        m = -1
        val = max(arr)
        for j in range(i,len(arr)):
            if arr[j] < val:
                val = arr[j]
                m = j
        (arr[i], arr[m]) = (arr[m], arr[i])

def mergeSort(arr,begin,end):
    if begin< end:
        mid = (begin + end)//2
        mergeSort(arr,begin,mid)
        mergeSort(arr,mid+1,end)
        littleMerge(arr,begin,end)
def littleMerge(arr,begin,end):
    if begin == end:
        return
    else:
        temparr = []
        for i in range(begin,end+1):
            temparr.append(arr[i])
        temparr.sort()
        arr[begin:end+1] = temparr

def quickSort(arr,begin,end):
    if begin < end:
        mid = cut(arr,begin,end)
        quickSort(arr,begin,mid-1)
        quickSort(arr,mid+1,end)
def cut(arr,begin,end):
    node = arr[begin]
    left = begin+1
    right = end
    while left < right:
        while arr[left] < node and left < end:
            left+=1
        while arr[right] > node and right > begin:
            right-=1
        if left < right:
            (arr[left],arr[right]) = (arr[right],arr[left])
    # arr[begin:right-1] = arr[begin+1:right]
    # arr[right] = node
    arr.remove(node)
    arr.insert(right,node)
    return right


arr = [4,3,1,5,7,9,2,8,0]
print(arr)
# insertSort(arr)
# bubleSort(arr)
# selectSort(arr)
# mergeSort(arr,0,len(arr)-1)
quickSort(arr,0,len(arr)-1)
print(arr)
a = [1,3,2]
quickSort(a,0,2)
print(a)

