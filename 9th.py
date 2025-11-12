x=int(input("Enter x Number: "))
y=int(input("Enter y Number: "))
ask=int(input("Enter Ask operator: "))
formula=(sum,dif,mul, div)
if  formula=="+":
    a=x+y,
    print(sum)
elif formula=="-":
    a=x-y,
    print(dif)
elif formula=="*":
    a=x*y,
    print(mul)
elif formula=="/":
    if y != 0:
        a=x/y
else:
    a="Error"
    print(div)
print(x)
print(y)
print(ask)