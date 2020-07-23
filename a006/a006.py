import sys
import math

for line in sys.stdin:
    a, b, c = map(int, line.split(" "))
    if b**2-4*a*c<0:
        print("No real root")
    else:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        if x==y:
            print("Two same roots x="+str(int(x)))
        if x!=y:
            print("Two different roots x1="+str(int(x))+" , x2="+str(int(y)))

    
     
    