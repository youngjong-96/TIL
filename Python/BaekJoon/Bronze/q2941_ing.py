s = input()

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 크로아티아 알파벳 개수
count_c = 0
# 일반 알파벳 개수 = 반복문 다 돌린 후에 len(s)

# croatia 를 문자열에서 확인하고 있으면 count_c 를 올리고 1로 바꾼다
# 발견되는게 없을 때까지 반복한다
# 1을 문자열에서 모두 지운다


# 3개씩 뽑아서 하는 로직
for _ in range(len(s)):
    # 문자열을 처음부터 쭉 본다
    for i in range(len(s)):
        # 크로아티아 문자열이 있다면 갯수를 세고 1로 바꾼다
        # break 하고 나갔다가 다시 처음부터 문자열을 센다
        if s[i:i+3] in croatia:
            count_c += 1
            # 처음 나오는 한 개만 바꾼다
            s = s.replace(s[i:i+3],"1",1)
            break

print("3개 로직 완료")
print(f'{count_c=}')
print(f'{s=}')
print("==============")

# 2개씩 뽑아서 하는 로직 
for _ in range(len(s)):
    # 문자열을 처음부터 쭉 본다
    for i in range(len(s)):
        # 크로아티아 문자열이 있다면 갯수를 세고 1로 바꾼다
        # break 하고 나갔다가 다시 처음부터 문자열을 센다
        if s[i:i+2] in croatia:
            count_c += 1
            s = s.replace(s[i:i+2],"1",1)
            break

print("2개 로직 완료")
print(f'{count_c=}')
print(f'{s=}')
print("==============")

for _ in range(len(s)):
    s = s.replace('1',"")
    
print(f'{count_c=}')
print(f'{s=}')
print(count_c + len(s))
