# 리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해
# [12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.

def del_duplicate(list):
    return sorted(set(list))

list = [12,24,35,24,88,120,155,88,120,155]
print(del_duplicate(list))
