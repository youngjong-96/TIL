# 여러 문장을 입력받아 대문자로 출력

while True:
    try:
        string = input()
        if string:
            print(f">> {string.upper()}")
        else:
            break
    except EOFError:
        break
    