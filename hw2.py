# 1
#print("True\n")



# 2
#login = input()
password1 = input()
password2 = input()
print(password2 == password1)
#print("False\n")



# 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
tmp = a
if b < tmp:
    tmp = b
if c < tmp:
    tmp = c
if d < tmp:
    tmp = d
print(tmp)
#print("5\n")



# 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
tmp = a
if b > tmp:
    tmp = b
if c > tmp:
    tmp = c
if d > tmp:
    tmp = d
print(tmp)
#print("30\n")



# 5
a = int(input())
b = int(input())
c = int(input())
if (a+b > c) and (a+c > b) and (b+c > a):
    print("True")
else:
    print("False")
#print("True\n")



# 6
a = int(input())
b = int(input())
c = int(input())

if max(a,b,c) == a + b + c - max(a,b,c):
    print("вырожденный")
elif a == b == c:
    print("равносторонний")
else:
    print("разносторонний")
#print("вырожденный")



# 7
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c > b or d < a:
    print(0)

if (a <= c <= b) and (a <= d <= b):
    print(d - c + 1)

if (c <= a <= d) and (c <= b <= d):
    print(b - a + 1)

if (a <= c <= b) and (d > b):
    print(b - c + 1)

if (a > c) and (a <= d <= b):
    print(d - a + 1)

#print("7\n")



