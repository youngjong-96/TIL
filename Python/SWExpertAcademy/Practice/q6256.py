# 두 딕셔너리를 합치고 가격이 3000원 이상인 메뉴를 출력
a = {'아메리카노': 1900, 
     '카페모카': 3300, 
     '에스프레소': 1900, 
     '카페라떼': 2500, 
     '카푸치노': 2500, 
     '바닐라라떼': 2900,
     }
b = {'헤이즐럿라떼': 2900, 
     '카페모카': 3300, 
     '밀크커피': 3300, 
     '아메리카노': 1900, 
     '샷크린티라떼': 3300,
     }

merge_dict = {}

for key in b:
    merge_dict[key] = b[key]

for key in a:
    merge_dict[key] = a[key]

result = {}

for key in merge_dict:
    if merge_dict[key] >= 3000:
        result[key] = merge_dict[key]
        
print(set(result.items()))