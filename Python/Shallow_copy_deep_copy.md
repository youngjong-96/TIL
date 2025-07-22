# 얕은 복사와 깊은 복사

참고: https://kevinitcoding.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%ACShallow-copy%EC%99%80-%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%ACdeep-copy%EC%97%90-%EB%8C%80%ED%95%9C-%EC%99%84%EB%B2%BD-%EC%A0%95%EB%A6%AC

### 얕은 복사와 깊은 복사는 mutable 객체(list, dict, set)를 복사할 때만 신경쓰면 됨

```
💡

#한 줄 요약

얕은 복사: 그냥 = 를 사용해서 복사, 주소값을 그대로 가져 옴. **복사한 객체의 값을 변경하면 원본도 변경됨 → 에러가 발생하지는 않아서 예상치 못한 결과가 나왔을 때 디버깅 어려울 수 있음!**

깊은 복사: copy 모듈의 deepcopy( ) 함수로 복사, 새로운 객체를 만들어서 주소값이 다름.

```

## 얕은 복사

```python
a = [1,2,3]
b = a

# 값, 주소값 모두 동일
print(a,b)
# [1,2,3][1,2,3]
print(id(a),id(b))
# 255644123543 255644123543   

# 값 둘 다 변경
a[0] = 9999
print(a,b)
# [9999,2,3][9999,2,3]
```

## 깊은 복사

```python
import copy

a = [1,2,3]
b = copy.deepcopy(a)

#값은 동일하지만 주소값은 다름
print(a,b)
#[1,2,3][1,2,3]
print(id(a),id(b))
# 255644123543 255644113571

# 변경한 객체의 값만 변경
a[0] = 9999
print(a,b)
#[9999,2,3][1,2,3]
```