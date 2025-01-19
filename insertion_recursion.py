def insertion_rec(arr,n):
    if n<=1:
        return
    insertion_rec(arr,n-1)
    pivot=arr[n-1]
    loc=n-2
    while(arr[loc]>pivot and loc>=0):
        arr[loc+1]=arr[loc]
        loc -= 1
    arr[loc+1]=pivot

arr=list(map(int,input('Enter elements: ').split()))
n=len(arr)
print("\nOriginal array: ",arr)
insertion_rec(arr,n)
print("\nAfter sorted array: ",arr)