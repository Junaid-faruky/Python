#Fabonacci series 
num=int(input())
i=0
j=1
count=0
if(num<=0):
    print()
elif (num==1):
    print(i)
else:
    print("Fabonacci series")
    while count < num:
       print(i)
       nth = i + j
       i = j
       j = nth
       count += 1
