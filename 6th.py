a= float(input("enter a number:")) #a is the coeffeciant of x**2
b= float(input("enter a number:")) #b is the coefficiant of x
c= float(input("enter a number:")) #c is the constant

Formula=(-b+(b**2-4*a*c)**(1/2))/(2*a)
Formula1=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print("ax**2+b*x+c is=", (Formula))
print("ax**2+b*x+c is=", (Formula1))

