# 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
# 구분하는 프로그램을 작성하십시오.

url = input().split('/')


print(f"protocol: {url[0][0:-1]}")
print(f"host: {url[2]}")
print(f"others: {url[3]}")