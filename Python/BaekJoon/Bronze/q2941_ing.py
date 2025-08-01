original_s = "ljes=njak"

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count_c = 0

count_o = 0

# croatia 를 문자열에서 확인하고 있으면 count_c 를 올리고 문자열에서 지운다.
# 발견되는게 없을 때까지 반복한다

for cro in croatia:
    print(cro)
    if cro in original_s:
        count_c += 1
        original_s.replace(cro,"")

print(original_s)


print('c=' in 'ljes=njak')