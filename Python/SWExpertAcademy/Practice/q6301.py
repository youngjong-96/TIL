# 항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

result = []

result = [[[0 for k in range(4)] for j in range(3)] for i in range(2)]

# for i in range(2):
#     row = []
#     result.append(row)
#     for j in range(3):
#         col = []
#         row.append(col)
#         for k in range(4):
#             col.append(0)
            
print(result)