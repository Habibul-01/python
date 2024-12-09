import math
a=int(input('Enter value 0f a: '))
b=int(input('Enter value of b: '))
c=int(input('Enter value of c: '))
msg=f"Equation is:({a}x2)+({b}x)+({c})"
print(msg)
d=(b*b)-(4*a*c)
sq=math.sqrt(abs(d))
if d>0:
	print('Roots are real and different')
	print(-b+sq/(2*a))
	print(-b-sq/(2*a))

elif d<0:
	print('Roots are not real number')
	print(-b/(2*a),'+i',sq/(2*a))
	print(-b/(2*a),'-i',sq/(2*a))
else:
	print('Roots are real and equal')
	print(-b/(2*a))
	print(-b/(2*a))