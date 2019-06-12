f=list(map(int,input().split()))
for j in range(f[0]+1,f[1]):
  if j%2 != 0:
    print(j,end=' ')
