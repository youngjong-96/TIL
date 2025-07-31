# 과목의 개수 N
N = int(input())

scores = list(map(int, input().split()))

Max_score = max(scores)

fake_scores = []

for score in scores:
    fake_scores.append(score/Max_score*100)

print(sum(fake_scores)/len(fake_scores))