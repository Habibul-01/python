def bubble(arr):
    for i in range(n-1):
        swapped=0
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=1
        if(swapped==0):
            break   
arr=list(map(int,input('Enter elements: ').split()))
print("\nOriginal array: ",arr)
n=len(arr)
bubble(arr)
print("\nAfter sorted array: ",arr)