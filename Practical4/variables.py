a = 5080000
b = 5330000
c = 5550000
d = b - a
e = c - b
if d > e:
    print("the population growth is decelerating in Scotland")
elif d == e:
    print("the population growth doesn't change in Scotland")
else:
    print("the population growth is accelerating in Scotland")
# d > e, the population growth is decelerating in Scotland.
print("\n")
print("X" , "\t" , "Y" , "\t" , "W" , "\t")
for X in (True , False):
    for Y in (True , False):
        W = X or Y
        print(X , "\t" , Y , "\t" , W , "\t")
# X     Y     W
# True  True  True
# True  False True
# False True  True
# False False False