#二分探索の応用例:年齢当てゲーム

#[left,right)
left = 20
right = 36

ans=31
while right - left > 1:
    mid=(right + left)//2

    if ans < mid:
        right = mid
    else:
        left = mid

print(left)

