class Value:
    def display(self,a,b):          #Method1
        print('Numbers are : ',a,b)
class Calculation:                  
    def display(self,a,b):          #Method2 with same name as method1(Overloading)
        print('Summation : ',(a+b))

#Creating object of above classes...

ob=Value()              #Object for method1
ob1=Calculation()       #Object for method2

#Calling methods...

ob.display(10,20)
ob1.display(10,20)