### 리스트와 튜플을 이용해 각 학생 점수 및 학생들의 과목별 총점, 평균 출력

```
scores = []

count = int(input("총 학생 수를 입력하세요: "))

#학생 별 과목의 총점 및 평균 출력
for i in range(1, count + 1):
    score = {}
    score["name"] = input("학생의 이름을 입력하세요: ")
    score["kor"] = int(input(f"{score["name"]} 학생의 국어 점수를 입력하세요: "))
    score["mat"] = int(input(f"{score["name"]} 학생의 수학 점수를 입력하세요: "))
    score["eng"] = int(input(f"{score["name"]} 학생의 영어 점수를 입력하세요: "))
    scores.append(score)

for score in scores: #score 가 딕셔너리여서 score에는 기본적으로 key값이 들어감
    total = 0
    for key in score:
        if key != "name":
            total += score[key]
    print(f"{score["name"]} => 총점: {total}, 평균: {total/3}")

#과목별 총점 및 평균 출력
kor_total, mat_total, eng_total = 0,0,0
for score in scores:
    for key in score:
        if key == "kor":
            kor_total += score[key]
        elif key =="mat":
            mat_total += score[key]
        elif key == "eng":
            eng_total += score[key]

print(f"국어 => 총점: {kor_total}, 평균: {kor_total/len(scores)}")
print(f"수학 => 총점: {mat_total}, 평균: {mat_total/len(scores)}")
print(f"영어 => 총점: {eng_total}, 평균: {eng_total/len(scores)}")
```
