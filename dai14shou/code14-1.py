#aが参照渡し、bが値渡し
def chmin(a,b):
    if a > b:
        a=b
        return True
    else:
        return False

