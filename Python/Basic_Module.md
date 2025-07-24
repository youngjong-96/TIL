## 모듈

: 한 파일로 묶인 **변수**와 **함수**의 모음, 특정한 기능을 하는 코드가 작성된 파이썬 파일

- 모듈 사용
    1. Import 문 사용
    
    ```python
    import math
    
    print(math.pi) # 모듈명.변수명
    print(math.sqrt(4)) #모듈명.함수명
    ```
    
    - 같은 이름의 함수가 여러 모듈에 있을 때 충돌 방지
    - 코드가 길어질 수는 있음
    1. from 절 사용
    
    `from math import pi, aqrt`
    
    - 코드가 짧고 간결해짐
    - 모듈 위치를 알기 어려워 명시적이지 않을 수 있고 이름이 겹치면 충돌 발생함
    
    ```python
    # from 절 사용 주의 사항 1
    ## 같은 이름인 경우 덮어쓰기 주의
    from math import sqrt  # math.sqrt가 먼저 import됨
    from my_math import sqrt  # my_math.sqrt가 math.sqrt를 덮어씀
    
    result = sqrt(9)  # math.sqrt가 아닌 my_math.sqrt가 사용됨
    
    # from 절 사용 주의 사항 2
    ## 모든 요소를 한 번에 import 하는 * 은 권장하지 않음
    from math import *
    from my_math import sqrt, tangent  # 어느 함수가 math 모듈과 중복되는지 모름
    
    # 아래는 사용자가 임의로 정의한 변수들
    a = 100
    c = 200
    e = 300  # math 모듈의 자연상수 e를 사용할 수 없게 됨
    ```
    
    -  as 키워드
        - as 키워드로 별칭 부여 가능 → 이름 충돌 문제 해결! or 줄여서 쉽게 사용
    
    ```python
    from math import sqrt
    from my_math import sqrt as my_sqrt
    
    print(sqrt(4))  # 2.0
    print(my_sqrt(4))  # 2.0
    ```
    

## 파이썬 표준 라이브러리

: 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음 (Python Standard Library)

[https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

- 패키지 : 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것 (연관 모듈 폴더링)
- 패키지의 사용 목적 : 모듈들의 이름공간을 구분하여 충돌 방지, 모듈을 효율적으로 관리
- 패키지, 모듈, 함수, 변수 다 임포트 가능함 → from 절로 경로 찾아갈 때 .(점 연산자)를 통해 찾아감

```python
## 사용자 정의 패키지
from my_package.math.my_math import add  # add 함수 임포트
from my_package.statistics import tools  # tools 모듈 임포트

print(add(1, 2))       # 3  (더하기)
print(tools.mod(1, 2)) # 1  (나머지)
```

<aside>
💡

내장된 패키지/모듈은 import 해서 바로 사용하고 외부 모듈은 pip install 설치 해야함

</aside>

- pip란? : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

`pip install <패키지명>` 으로 설치

<aside>
💡

패키지에도 버전이 있어서 호환성 확인해야 함!

설치한 패키지는 `pip freeze > requirements.txt` 명령어로 버전 기록해두면 좋음

</aside>
