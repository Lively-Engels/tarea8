a=float(input("introduce el valor de a: "))
b=float(input("introduce el valor de b: "))
c=float(input("introduce el valor de c: "))

if a==0:
 print("el valor de a no puede ser 0 introduce otro valor")
 
if a!=0:
 x1=(-b+(((b*b)-(4*a*c))**0.5))/(2*a)
 x2=(-b-(((b*b)-(4*a*c))**0.5))/(2*a)
     
 print ("el valor de x1 es:")
 print(x1)

 print("el valor de x2 es:")
 print(x2)


