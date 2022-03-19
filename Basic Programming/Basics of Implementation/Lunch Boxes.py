#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/lunch-boxes-019bf2a5/

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    no_schools = 0
    sum = 0

    for i in range(m):
        if (a[i] + sum) <= n:
            sum += a[i]
            no_schools += 1
    print(no_schools) 