#1
x = int(input())
while (x % 2 != 0) and (x % 10 != 5):
    x = int(input())


#2
for i in range(10):
    print(i)


#3 (768182441)
K = int(input())
N = int(input())
s = 0
while K <= N:
    if K % 2 != 0:
        s += K
    K += 1
print(s)


#4 (3628800)
N = int(input())
f = 1
for i in range(1, N+1):
    f *= i
print(f)


