#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/beauty-factor-bab8f334/


def sumOfDigit(n):
    a = n
    flag = 0
    
    while flag != 1:
        sum_1 = 0
        for digit in str(a):
            sum_1 += int(digit)
        if len(str(sum_1)) != 1:
            flag = 0
            a = sum_1
        else:
            flag = 1

    return sum_1

b, k = map(int, input().split())

if k == 9:
    if b != 9:
        print(-1)
    else:
        print(123456789)
    exit()

c = ""
for i in range(1, k+1):
    c += str(i)
num = int(c)     
    
result = 1

while ((result != 0) or (len(lst) > k)):
    e = 0
    f = str(num)
    lst = []
    for i in f:
        lst.append(i)
    
    temp_arr_com = []
    temp_arr_uncom = []
    
    for i in range(len(lst)):
        if lst[i] not in temp_arr_uncom:
            temp_arr_uncom.append(lst[i])
        else:
            temp_arr_com.append(lst[i])
    
    if ((len(temp_arr_com) == 0) and (temp_arr_uncom.count("0") == 0)):
        if (sumOfDigit(num) == b):
            e = num
            result = 0
    num += 1
if len(lst) > k:
    print(-1)
else:
    print(e)