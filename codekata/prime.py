s=input()
t=int(s)
a=0
for i in range (2,t):
  y=t%i
  if(y==0):
    a=1+a
if(a!=0):
  print("no")
else:
  print("yes")

