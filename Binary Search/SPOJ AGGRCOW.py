def placingcow(arr,dist,c):
    lastplaced=0
    cowsplaced=1
    for j in range(1,n):
        if arr[j]-arr[lastplaced]>=dist:
            lastplaced=j
            cowsplaced+=1
            if cowsplaced==c:
                break
    if cowsplaced==c:
        return True
    else:
        return False


T=int(input())
for _ in range(T):
    n,c=map(int,input().split())
    stalls=[]
    for j in range(n):
        k=int(input())
        stalls.append(k)
    stalls.sort()
    low=stalls[0]
    high=stalls[n-1]-stalls[0]
    while low<=high:
        mid=(low+high)//2
        if placingcow(stalls,mid,c):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    print(ans)