#다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.

pi = 3.141592

rlist = list(map(int, input().split(',')))
result = []

for i in rlist:
    result.append(i*pi*2)

formatted_list = [f"{i:.2f}" for i in result]

print(", ".join(formatted_list))