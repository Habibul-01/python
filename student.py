l=[]
d={}
n=int(input("Enter number of students: "))
for i in range(1,n+1):
    msg=f"Enter student {i} marks: "
    print(msg)
    msg=f"Enter key: "
    key=input(msg)
    l=[]
    for i in range(1,7):
        msg=f"Enter sem {i} number: "
        num=int(input(msg))
        l.append(num)
    d[key]=l
print()
print(d)      
        