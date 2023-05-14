b=(int(input("Enter the Total no of bananas : ")))
d=(int(input("Enter the Total distance : ")))
c=(int(input("Enter the Camel Capacity : ")))
l=0
s=b
for i in range (d):
    while s>0:
        s=s-c
        if s==1:
            l=l-1
        l=l+2
    l=l-1
    s=b-l
    if s==0:
        break
print("No of banana's left is : ",s)