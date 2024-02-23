def search(ps,n,sug):
    low=0
    high=n
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if ps[mid]>=sug:
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    ps=[0]
    for i in range(n):
       ps.append(ps[i]+arr[i])
    for kk in range(q):
        sugar=int(input())
        print(search(ps,n,sugar))