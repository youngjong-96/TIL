# 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

words = input().split()


for i in range(len(words)-1,-1,-1):
    print(f"{words[i]} ",end="")
