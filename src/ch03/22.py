n=int(input("> "))
for i in range(3*n+1,-3,-1):
    for j in range(2*n-1):
        if j%2==0: 
            h=n 
        else: 
            h=n-1
        if i==-1 or i==-2 :
            print("II"+" "*(4*h-3)+"II",end=" ")
        elif i==0:
            print("|"+"="*(4*h-1)+"|",end=" ")
        elif i<h:
            print("|"+" "*h,"|"+" "*(2*h-3)+"|"if h>1 else " "," "*h+"|",sep="",end=" ")
        elif i==h:
            print("|"+" "*h," "+"_"*(2*h-3)+" "if h>1 else " "," "*h+"|",sep="",end=" ")
        elif i<=3*h:
            print(" "*(i-h-1)+"/"+"-"*(6*h-2*i+1)+"\\"+" "*(i-h-1),end=" ")
        elif i==3*h+1:
            print(" "*(2*h)+"*"+" "*(2*h),end=" ")
        else:
            print(" "*(4*h+1),end=" ")
    print()
