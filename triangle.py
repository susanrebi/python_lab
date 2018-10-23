def    tri(a,b,c):
       hyp=(a*a+b*b)**0.5
       if(hyp==c):
           return 1
       else:
            return 0
x=input("base")
y=input("height")
z=input("hypotenuse")
r=tri(x,y,z)
if(r==1):
    print"it is a right angle triangle"
else:
    print"not a right angle triangle"
  
