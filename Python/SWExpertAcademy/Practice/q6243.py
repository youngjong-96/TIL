# 사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고,
# 중복된 단어없이
# 단어를 콤마(,)로 구분해
# 사전순으로 출력하는 프로그램을 작성하십시오.


string = input().split()

string_set = set(string)
sorted_string = list(sorted(string_set))

print(",".join(sorted_string))