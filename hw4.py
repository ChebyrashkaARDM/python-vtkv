#1
#[2, 2, 2]


#2
#[1, 2, 2]


#3 (4.2)
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

mean_arf = sum(a) / len(a)
print(mean_arf)


#4 (32)
n = int(input())
m = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
print(a[m])


#5 (6)
n = int(input())
a = []
for i in range(n):
    a = a + [int(input())]
s = 0
for i in range(0, n, 2):
    s += a[i]
print(s)

