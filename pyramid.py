n = int (input("enter the number of rows"))
m = (n*2)-2
for i in range(n):
   for j in range(m):
       print(end=" ")


   m=m-1
   for j in range(i+1):
       print("*",end=" ")
   print()