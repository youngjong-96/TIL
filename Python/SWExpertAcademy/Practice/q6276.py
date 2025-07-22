# 구구단 각 단을 3의 배수이거나 7의 배수인 수를 제외하고 출력
result = []

for i in range(2,10):
    dan = []
    for j in range(1,10):
        if not (i * j % 3 ==0 or i * j % 7 == 0):
            dan.append(i * j)
    result.append(dan)

print(result)