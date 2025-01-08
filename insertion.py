def insertion(arr):
    for i in range(1,n-1):
        pivot=arr[i]
        loc=i-1
        while(arr[loc]>pivot):
            arr[loc+1]=arr[loc]
            loc -= 1
        arr[loc+1]=pivot
arr=list(map(int,input('Enter elements: ').split()))
n=len(arr)
print("\nOriginal array: ",arr)
insertion(arr)
print("\nAfter sorted array: ",arr)