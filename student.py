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
    avg=(sum(l)/6)
    print("Grade is ")
    if avg>90:
      print("AA")
    elif avg>80:
      print("A+")
    elif avg>70:
      print("B+")
    elif avg>50:
      print("B")
    elif avg>30:
      print("c")
    else:
      print("Disqualify")
#print()
#print(d)
	
        