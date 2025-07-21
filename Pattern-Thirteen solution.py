n = int(input())
val = 10
for i in range(1, n + 1):
   for j in range(i):
       print(val, end = " ")
       val += 10
   print()
