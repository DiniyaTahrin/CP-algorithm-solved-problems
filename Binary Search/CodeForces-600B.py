n,m= map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ansq=[]
a.sort()
for j in range(m):
  target=b[j]
  low=0
  high=n-1
  ans=n
  while low<=high:
    mid=(low+high)//2
    if a[mid]>target:
      ans=mid
      high=mid-1
    else:
      low=mid+1 
  ansq.append(ans)    
print(*ansq)  