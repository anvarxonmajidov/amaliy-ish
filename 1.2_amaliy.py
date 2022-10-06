
#1.2 amaliy 23. Uchburchаkning uchtа uchi koordinаtаlаri berilgаn: (x1,y1), (x2,y2), (x3,y3).
# Uning perimetrini vа mаydonini toring. Uchburchаkning mаydonini topishdа Geron formulаsidаn foydаlаning 					 .
# Bu erdа а, b, s - uchburchаk tomonlаri,  p=(а+b+s)/2 – yarim perimetr.

print("x1=",end=" ")
x1=int(input())
print("y1=",end=" ")
y1=int(input())
print("x2=",end=" ")
x2=int(input())
print("y2=",end=" ")
y2=int(input())
print("x3=",end=" ")
x3=int(input())
print("y3=",end=" ")
y3=int(input())
a=((x2-x1)**2+(y2-y1)**2)**(1/2)
b=((x3-x2)**2+(y3-y2)**2)**(1/2)
c=((x3-x1)**2+(y3-y1)**2)**(1/2)
p=(a+b+c)/2
s=(p*(p-a)* (p-b)* (p-c))**(1/2)
print("Uchburchak perimetr=",2*p)
print("Uchburchak yuzasi=",s)
