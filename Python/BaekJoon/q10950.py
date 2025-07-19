#A+B

T = int(input())
result_list=[]

for i in range(T):
    a, b = map(int, input().split())
    result_list.append(a+b)
    
for i in range(T):
    print(result_list[i])