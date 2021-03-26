#하이루
N = int(input())
a = []
for i in range(N):
    b = int(input())
    a.append(b)
a.sort()
for i in range(N):
    print(a[i])