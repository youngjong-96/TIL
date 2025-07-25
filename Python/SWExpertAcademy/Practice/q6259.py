# 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

input = 'hello world! 123'

letters = 0
digits = 0

for i in input:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print(f"LETTERS {letters}\nDIGITS {digits}")