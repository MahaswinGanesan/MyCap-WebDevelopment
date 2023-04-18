x=int(input("Enter the limit:"))
i=2
a=0
b=1
print( a,"\n",b)
while(i<x):
    print("\n",a+b)
    t=a+b
    a=b
    b=t
    i=i+1
    
