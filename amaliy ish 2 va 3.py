#2.1 


a=int(input("a - qiymatini kiriting: "))
b=int(input("b - qiymatini kiriting: "))
p=2*(a+b)
s=a*b
print(f'togri tortburchak perimetri={p}')
print(f'togri tortburchak yuzi={s}')


#2.2 

# A=int(input("kichik sonni kiriting: A="))	
# B=int(input("katta sonni kiriting: B="))
# n=B-A+1
# for i in range(0,n):
#     print(B-i)

# son = int(input())
# son1 = int(input())
# son2 = int(input())
# musbat = 0
# manfiy = 0
# nol = 0
# if son=0:
#     nol += 1
# elif son > 0:
#     musbat +=1
# else:
#     manfiy+=1

# if son2=0:
#     nol += 1
# elif son2 > 0:
#     musbat +=1
# else:
#     manfiy+=1

# if son1=0:
#     nol += 1
# elif son1 > 0:
#     musbat +=1
# else:
#     manfiy+=1
    
    
    #3.1
import math
x = float(input())
y = float(input())
z = float(input())
gamma =5 * math.atan(x)-(1/4)*math.acos(x)*(x+3*math.fabs(x-y)+x**2)/(math.fabs(x-y)*z+x**2)
print(gamma)


# 3.2
import math
x=float(input('0<x<1  x='))
n=int(input('n='))
s=0
if(0<x and x<1):
    for i in range(1,n):
        s=s+(math.pow(-1,i)*math.pow(x,(2*i+1)))/(2*i+1)
print(s)




    