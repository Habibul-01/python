def binary(l,value):
    start=0
    end=len(l)-1
    mid=0
    while(end>=start):
        mid=(end+start)//2
        if l[mid]>value:
            end=mid-1
        elif l[mid]<value:
            start=mid+1
        else:
            return mid    
    return -1
l=[]
l=list(map(int,input('Enter a sorted array: ').split()))
value=int(input('Enter the search element: '))
result=binary(l,value)
if result==-1:
    print("Element is not found..!")
else:
    print("Element is founded at index ",result)