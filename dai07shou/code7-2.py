#区間スケジューリング問題に対する貪欲法

N=int(input())
#N=6
interval=[[0]*2 for _ in range(N)]
#[開始時刻,終了時刻]の2次元リスト
for i in range(N):
    interval[i][0],interval[i][1]=map(int,input().split())

#interval=[[9,16],[10,12],[11,16],[13,19],[15,18],[19,23]]


#終了時刻が早い順にソート.
#2つめの要素を基準にソートする場合の書き方
interval.sort(key=lambda x: x[1])

res=0
current_end_time=0

for i in range(N):
    if interval[i][0] < current_end_time:
        continue
    res += 1
    current_end_time=interval[i][1]

print(res)

