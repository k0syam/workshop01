#区間[left,right)をソート
def QuickSort(a,left,right):
    if right - left <= 1:#要素1つのとき
        return
    
    pivot_index=(left + right)//2#ピボットのindex
    pivot=a[pivot_index]#ピボットの値
    #swap
    a[pivot_index], a[right-1] = a[right-1], a[pivot_index]
    #i:左詰めされたpivot未満の要素の右端
    i=left

    for j in range(left,right-1):
        if a[j] < pivot:#pivot未満のものがあったら左詰めswap
            a[i],a[j]=a[j],a[i]
            i += 1
    
    #最後まで見たらpivotを挿入
    a[i],a[right-1] = a[right-1],a[i]

    QuickSort(a,left,i)
    QuickSort(a,i+1,right)




if __name__ == '__main__':

    a=[4,1,3,5,2,8,7,12,3,6]
    
    n=len(a)

    QuickSort(a,0,n)
    print(a)