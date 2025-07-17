#리스트 내포 기능을 활용하여 평균값 출력
num = [int(input()) for i in range(5)]
print(f"입력된 값 {num}의 평균은 {sum(num)/len(num)}입니다.")


# num = []
# for i in range(5):
#     num.append(int(input()))
# print(sum(num)/len(num)) 