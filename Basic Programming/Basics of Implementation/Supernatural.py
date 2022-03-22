#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/supernatural-cac54bc7/

n = int(input())
cnt = 0

for i in range(2, 322223):
    prod = 1
    b = str(i)
    temp_arr = []
    
    for j in b:
        temp_arr.append(int(j))
#    print("Array:", temp_arr)
    
    if ((temp_arr.count(1) == 0)):
        for k in temp_arr:
            prod *= k
    
#    print("Product:", prod)
#    print("****")

    if prod == n:
        cnt += 1

print(cnt)