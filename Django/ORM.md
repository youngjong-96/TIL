# Django - ORM

## ORM

- ORM (Object-Relational-Mapping) : 객제 지향 프로그래밍 언어의 객체와 데이터베이스의 데이터를 매핑하는 기술

## QuerySet API

- QuerySet API : 데이터베이스의 복잡한 SQL 쿼리문을, 직관적인 Python 코드로 다룰 수 있게 해주는 번역기
- 동작 방식
    - Django → DB : Django( QuerySet API)에서 ORM 을 통해 SQL 쿼리로 변환되어 DB로 전달
    - DB → Django : ORM이 SQL 문을 QuerySet or Instance 형태로 변환하여 Django로 반환
- 기본 구조
    - `모델 클래스.매니저.QuerySetAPI 메서드` ex. `Article.objects.all( )`
- QuerySet
    - 데이터베이스에서 전달받은 객체 목록(데이터 모음)
    - 순회 가능

## QuerySet API 실습

- 실습 준비
    1. ipython 설치
        1. `pip install ipython` : django shell 사용 시 도움을 주는 패키지 ipython 설치
        2. `pip freeze > requirements.txt` : 설치한 라이브러리 업데이트
    2. django Shell 접속
        1. `python manage.py shell` 

### Create

1. 빈 객체 생성 후 값 할당 및 저장
    1.  article 인스턴스 생성`article = Article()`
    2. 인스턴스 변수에 값을 할당 `article.title = 'first'` , `article.content = 'django!'` 
    3. DB 에 저장 `article.save()` 
    - 저장하고 나면 인스턴스를 활용하여 인스턴스 변수를 활용해서 데이터에 접근 가능
        
        ```python
        In [11]: article.title
        Out[11]: 'first'
        
        In [12]: article.content
        Out[12]: 'django!'
        ```
        
2. 초기 값과 함께 객체 생성 및 저장
    1. 인스턴스를 생성하면서 변수값을 바로 할당
        
        `article = Article(title='second', content='django!')`
        
    2. DB 에 저장 `article.save()` 
3. create( ) 메서드로 한 번에 생성 및 저장
    1. create( ) 메서드로 한 번에 생성 및 저장(save( ) 메서드를 내장하고 있음)
        
        `Article.objects.create(title='third', content='django!')`
        

### Read

- QuerySet 반환 메서드
    - all( ) : 전체 데이터 조회
        
        ```python
        In [16]: Article.objects.all()
        Out[16]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
        ```
        
    - filter( ) : 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
        
        ```python
        In [17]: Article.objects.filter(content='django!')
        Out[17]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
        
        In [18]: Article.objects.filter(title='ssafy')
        Out[18]: <QuerySet []>
        
        In [19]: Article.objects.filter(title='first')
        Out[19]: <QuerySet [<Article: Article object (1)>]>
        ```
        
- QuerySet을 반환하지 않는 메서드
    - get( ) : 주어진 매개변수와 일치하는 객체를 반환
        
        ```python
        In [20]: Article.objects.get(pk=1)
        Out[20]: <Article: Article object (1)>
        
        In [21]: Article.objects.get(pk=100)
        DoesNotExist: Article matching query does not exist.
        
        In [22]: Article.objects.get(content='django!')
        MultipleObjectsReturned: get() returned more than one Article -- it returned 3!
        ```
        
    - get의 특징
        - 찾을 수 없어도 error, 여러 개여도 error → primary key 나 고유성을 보장하는 조회에 사용

### Update

- 인스턴스 변수를 변경 후 save 메서드 호출
    
    ```python
    
    # 수정할 인스턴스 조회
    In [23]: article = Article.objects.get(pk=1)
    
    # 인스턴스 변수를 변경
    In [24]: article.title = 'byebye'
    
    # DB에 저장
    In [25]: article.save()
    
    In [26]: article.title
    Out[26]: 'byebye'   # 확인해보면 바뀌어 있음
    ```
    

### Delete

- 삭제하려는 데이터 조회 후 delete 메서드 호출
    
    ```python
    # 삭제할 인스턴스 조회
    In [27]: article = Article.objects.get(pk=1)
    
    # delete 메서드 호출 (삭제 된 객체가 반환)
    In [28]: article.delete()
    Out[28]: (1, {'articles.Article': 1})
    
    In [29]: Article.objects.get(pk=1)
    DoesNotExist: Article matching query does not exist.   # 확인해보면 삭제됐음
    ```
    

## 참고

### Field lookups : 단순 비교(=)를 넘어 더 상세한 조건으로 데이터를 조회할 수 있도록

- title 필드가 ‘second’으로 시작하는 Article 데이터(레코드)를 모두 찾고 싶다면?
    
    `Article.objects.filter(모델필드명__조회조건=비교할 값)`
    
    `Article.objects.filter(title__startswith='second')`
    


### ORM, QuerySet API 를 사용하는 이유

- 데이터베이스 추상화
- 생산성 향상
- 객체 지향적 접근

### api 호출 기본 구조
    
    ```python
    import request
    
    API_URL = API 요청 주소
    params = {
        # 필요 파라미터들 정의
    }
    
    # get 메서드에 url, 파라미터 넣고 요청 후 json 메서드로 딕셔너리로 변환
    request.get(API_URL, params=params).json()
    ```
    
    <aside>
    💡
    
    알라딘 API
    
    ```python
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx' # 상품검색 URL
        API_KEY = 'ttbdudwhd961058001'
        params = {
            'ttbkey': API_KEY,
            'Query': 'AI',
            'QueryType': 'Title',
            'SearchTarget': 'Book',
            'Output': 'JS',
            'MaxResults': 10,
            'Start': 1,
            'Version': '20131101',
        }
    ```
    
    </aside>
    