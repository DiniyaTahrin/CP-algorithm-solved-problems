def possible(waitTime,arr,n):
    pattern=waitTime+arr[0]
    l=[]
    l.append(pattern)
    ans=True
    for i in range(n):
       if arr[i]-pattern>waitTime and len(l)<3:
             pattern=waitTime+arr[i]
             l.append(pattern)
       elif arr[i]-pattern>waitTime:
             ans=False
             break
    return ans
T=int(input())
for _ in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    low=0
    high=arr[n-1]
    while low<=high:
        mid=(low+high)//2
        if possible(mid,arr,n):
            timee=mid
            high=mid-1
        else:
            low=mid+1
    print(timee)
