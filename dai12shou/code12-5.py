#0以上MAX未満
MAX=100000


def BucketSort(a):
    n=len(a)
    #num[v]:vの個数
    num=[0]*MAX
    for i in range(n):
        num[a[i]] += 1
    
    #n_less[v]:v以下の値の個数
    #a[i]が全体の中で何番目に小さいか求める
    #numの累積和を取ることで求まる
    n_less=[0]*MAX
    n_less[0]=num[0]#これいらないの？
    for v in range(1,MAX):
        n_less[v]=n_less[v-1] + num[v]
    
    #ソートしたもの
    a2=[0]*n
    for i in range(n-1,-1,-1):
        print(n_less[a[i]])
        a2[n_less[a[i]]]=a[i]#なんかエラー出る
        n_less[a[i]] -= 1
        
    a=a2

if __name__ == '__main__':

    a=[4,1,3,5,2,8,7,12,3,6]
    
    n=len(a)

    BucketSort(a)
    print(a)