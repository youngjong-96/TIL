# 다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고, 그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.

n = int(input())

keys = [i for i in range(1,n+1)]
values = [i**2 for i in keys]

result={}

for i in range(len(keys)):
    result[keys[i]] = values[i]
    
print(result)
