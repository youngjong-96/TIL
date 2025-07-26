# 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.

string = 'H1e2l3l4o5w6o7r8l9d'

idx = range(0,len(string),2)

for idx in idx:
    print(string[idx], end="")