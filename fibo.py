#def fibo(num):
#    if num<2:
#        return num
#    else:
        
#        return fibo(num-1)+fibo(num-2)

#print(fibo(5)) 

from math import sqrt, pow

def fibo(num):
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, num) / sqrt(5))

print(fibo(5))


