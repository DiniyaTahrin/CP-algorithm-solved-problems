def possible(arr,size,n,f):
  peep=0
  for i in range(n):
    peep+=int(arr[i]/size)
  if peep>=f:
    return True
  else:
    return False    
import math
T=int(input())
for _ in range(T):
  n,f=map(int,input().split())
  arr=list(map(int,input().split()))
  arr.sort()
  for i in range(n):
    arr[i]=(arr[i]**2)*math.pi
  low=0
  high=arr[n-1]
  while high-low>=10**-3:
    mid=(low+high)/2
    if possible(arr,mid,n,f+1):
      low=mid
    else:
      high=mid  
  print(low) 
