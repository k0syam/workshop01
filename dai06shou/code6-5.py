#射撃王問題
INF=1<<60
N=int(input())

h=[0]*N
s=[0]*N

#二分探索
left=0
right=INF

while right - left > 1:
    mid=(left + right)//2

    #判定
    ok=True
    #それぞれの風船を割るまでの時間制限
    t=[0]*N

    for i in range(N):
        if mid < h[i]:
            ok=False
        else:
            t[i]= (mid-h[i]) // s[i]
    #風船を割る優先順にソート
    t.sort()
    
    for i in range(N):
        if t[i] < i:
            ok=False#時間切れ
        
    if ok:
        right=mid
    else:
        left=mid

print(right)

