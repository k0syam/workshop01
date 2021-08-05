
def InsertionSort(a):
    n=len(a)
    for i in range(1,n):
        v=a[i]

        j=i
        while j > 0:
            if a[j-1] > v:
                a[j] = a[j-1]
            else:
                break
            j -= 1
        
        a[j] = v



if __name__ == '__main__':
    a=[4,1,3,5,2]

    InsertionSort(a)
    print(a)