def P(x):
    if x >= 50:
        return True
    else:
        return False

def binary_search():
    left = 0
    right = 100
    while right - left > 1:
        mid = left + (right - left) // 2
        if P(mid):
            right = mid
        else:
            left = mid
    return right

if __name__ == "__main__":
    print(binary_search())