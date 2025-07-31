student_num = []

for i in range(1, 31):
    student_num.append(i)

for i in range(28):
    num = int(input())
    student_num.remove(num)

print(min(student_num))
student_num.remove(min(student_num))
print(student_num[:])