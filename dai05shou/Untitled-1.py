def f(l):
    l[0] = 0
    print(f"f(l), l={l}, id={id(l)}")


l = [1, 2, 3]
print(f"Before f, l={l}, id={id(l)}")
f(l)
print(f"After f, l={l}, id={id(l)}")

def f(i: int):
    i = 0
    print(f"f(i), i={i}, id={id(i)}")


i = 1
print(f"Before f, i={i}, id={id(i)}")
f(i)
print(f"After f, i={i}, id={id(i)}")