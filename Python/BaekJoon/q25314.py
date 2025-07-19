#혜야의 면접 - long을 몇 번이나 썼을까,,,,

while True:
    N = int(input())
    if 4 <= N <= 1000 and N % 4 == 0 :
        print("long "*(N//4)+"int")
        break
    else:
        print("4~1000 사이의 4의 배수를 입력하세요: ")