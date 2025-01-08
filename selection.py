def selection(arr):
    for i in range(n):
        min=arr[i]
        index=i
        for j in range(i,n):
            if(min>arr[j]):
                min=arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]
        
arr=list(map(int,input('Enter elements: ').split()))
n=len(arr)
print("\nOriginal array: ",arr)
selection(arr)
print("\nAfter sorted array: ",arr)