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

```
💡

슬라이싱으로 하는 복사도 얕은 복사임!!!!
```


```python
origin = [1,2,3,4,5]

copy = origin[:]   # 슬라이싱으로 복사

origin[0] = 9999   # 원본값 수정

print(f'{origin=}')    # 원본 출력
print(f'{copy=}')      # 복사본 출력
print(f"{origin is copy=}")   # 주소값이 같은가요?
print(f'{origin == copy=}')   # 값이 같은가요?

>> 
origin=[9999, 2, 3, 4, 5]
copy=[1, 2, 3, 4, 5]
origin is copy=False
origin == copy=False
```

값, 주소값 모두 달라서 깊은 복사가 된 것처럼 보임!

하지만 이건 슬라이싱의 특성으로 인해 발생한 것으로 사실은 얕은 복사인 것,,,

사실은,,,

슬라이싱해서 origin 과 같은 새로운 리스트를 어딘가의 생성 → 그 리스트의 첫번째 주소를 copy가 저장 → 원본 수정해도 새로운 리스트의 주소를 가리키고 있기 때문에 영향 x

하지만 결과적으로 ‘값’ 자체를 복사해 온게 아니라 새로운 ‘주소’를 복사한 것임

이걸 확인해보려면 아래와 같이 해보면 됨

```python
origin = [[1, 2, 3],2,3,4,5]    #이중 배열

copy = origin[:]                #슬라이싱으로 복사

origin[0][0] = 9999             #원본에서 이중배열 안에 값을 수정

print(f'{origin=}')             #원본 출력
print(f'{copy=}')               #복사본 출력
print(f"{origin is copy=}")     # 주소값이 같은가요?
print(f'{origin == copy=}')     # 값이 같은가요?

>>
origin=[[9999, 2, 3], 2, 3, 4, 5]
copy=[[9999, 2, 3], 2, 3, 4, 5]
origin is copy=False
origin == copy=True
```

원본을 변경했는데 복사본의 값이 바뀌었음

주소값이 다르고 변경된 원본과 복사본의 값이 같음

(헷갈린다면 pythontutor에서 실제 메모리가 어떻게 되는지 눈으로 보면 좀 더 이해가 잘 됨)


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