n,q=map(int,input().split())
lis=list(map(int,input().split()))
da=[0]*n
for i in range(q):
  l,r=map(int,input().split())
  l-=1
  r-=1
  da[l]+=1
  if r+1<n:
    da[r+1]-=1
coun=[]    
summ=0
for jj in range(n):
  summ+=da[jj]
  coun.append(summ)
coun.sort()
lis.sort()
maxSum=0
for i in range(n):
    maxSum+=(coun[i]*lis[i])
print(maxSum)   