# Django - Template & URLs

## Template System

### Django Template System

: 파이썬 데이터(context)를 HTML 문서(Template)와 결합하여, 로직과 표현을 분리한 채 동적인 웹페이지를 생성하는 도구

→ 페이지 틀에 데이터를 동적으로 결합하여 페이지를 효율적으로 만들기 위함

### Django Template Language

: Template 에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

1. 변수 (variable)
    - render 함수의 세번째 인자로 딕셔너리 타입으로 전달
    - 딕셔너리 key가 template에서 사용 가능한 변수명이 됨
    - dot(’.’)을 사용해서 변수 속성에 접근할 수 있음
    
2. 필터 (filters)
    - 표시할 변수를 수정할 때 사용
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
3. 태그 (tags)
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags 제공
4. 주석 (comments)
    - inline `{#      #}`
    - multiline `{% comment %}                     {% endcomment %}`

## 템플릿 상속

- 템플릿 상속 : 여러 템플릿이 공통요소를 공유할 수 있게 해주는 기능
    - 페이지의 공통 요소를 포함
    - 하위 템플릿이 재정의 할 수 있는 공간을 정의
- 상속 구조 만들기
    1. skeleton 역할을 하게 되는 상위 템플릿(base.html) 작성
    
    ```python
    # 상위 템플릿으로 html 하나 만들고 아래 코드로 자식들이 내용을 채울 공간을 생성
    # content 는 공간 이름으로 매번 달라질 수 있음
    {% block content %}
    {% endblock content %}
    ```
    
    1. 기존 하위 템플릿들이 상위 템플릿을 상속받도록 변경
    
    ```python
    # 자식 html에서 상속받을 템플릿을 선언
    # 반드시 가장 상단에 작성해야 함
    {% extends "articles/base.html" %}
    
    {% block content %}
    # 이 안쪽에다가 자식 html 만의 내용을 작성
    # 공간 이름도 적어줘야 함 (여기서는 content)
    {% endblock content %}
    ```
    

## 요청과 응답

### HTML form : HTTP 요청을 서버에 보내는 가장 편리한 방법!

- 데이터를 담아서 요청한다 (데이터는 input 태그로 받고 action 주소로 전달한다)
- [실습] fake naver 를 만들어서 네이버에 검색 요청 보내보기
    1. 검색창 틀 만들기
    
    
    1. search.html 안에 아래 코드 입력하기
        - action 에 검색요청하는 주소 입력
        - name 에 naver 에서 사용하는 검색 input 받는 key 입력
    
    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <form action="https://search.naver.com/search.naver" method="GET">
        <label for="message">검색어</label>
        <input type="text" name="query" id="message">
        <input type="submit" value="submit">
      </form>
    </body>
    </html>
    ```
    

### HTML form 핵심 속성

- ‘action’ & ‘method’ : 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
    - action : 입력 데이터가 전송될 URL을 지정(목적지)
    - method : 데이터를 어떤 방식으로 보낼 것인지 (GET, POST)
- input : 사용자의 데이터를 입력 받을 수 있는 HTML 요소, type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
    - `name` 이 핵심 속성임 : 사용자가 입력한 데이터에 붙이는 이름(key), 서버는 name 속성에 설정된 값을 통해서 사용자가 입력한 데이터에 접근
- Query String Parameters : 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
    - 문자열은 & 로 연결된 key=value 쌍으로 구성되고, 기본 URL 과는 물음표로 구분

### HTML form 활용

- [실습] throw 에서 보낸 메세지를 catch 에서 받아서 처리하기
1. urls.py - URL 경로 처리

```python
path('throw/', views.throw, name='throw'),
path('catch/', views.catch, name='catch'),
```

1. http://views.py - throw( ) 함수와 catch( ) 함수 작성

```python
def throw(request):
    return render(request, 'articles/throw.html')

# 사용자 입력 데이터를 추출해서 응답 페이지에 보여주기
def catch(request):
    # 사용자 입력데이터는 request 객체이 있음
    context = {
        'message' : request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)
```

1. throw.html - form 을 활용해 메세지를 보낼 틀을 만들기

```python
<form action="articles/catch" method="GET">
    <input type="text" name="message">
    <input type="submit" value="submit">
  </form>
```

1. catch.html - catch( ) 함수에서 받은 검색어를 화면에 출력할 수 있도록 작업

```python
<body>
  <h1>Catch</h1>
  <h2>{{ message }}를 잘 받았습니다.</h2>
</body>
```

## Django URLs

### Variable Routing :  URL 일부에 변수를 포함시키는 것

→ URL 에서 똑같은 부분들을 변수로 쓰겠다

- 사용법 : <속성: 이름>`path('articles/<int:num>/',...)`
- 이 때 이름 부분을 함수의 매개변수로 전달함



- URL 에 쓸 때에는 / 로 구분해서 사용함



### App URL 정의 : 각 app에 URL을 정의하는 것

→ app이 많아지면 프로젝트의 urls.py 하나에서 너무 많은 url을 관리하게 되니 각자의 app 에서 url을 관리하자

- include( ) 함수를 사용한다!
- URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 include 된 URL로 전달해서 각 app에서 처리
- 어떻게 하느냐?!
    - 각 앱에서 urls.py 파일을 만들고 프로젝트 urls.py 에서 include( ) 함수로 추가한다
    - 각 앱의 urls.py 파일에서 일치하는 주소를 제외한 나머지 주소들을 처리하도록 한다
    
    ```python
    # 각 app의 urls.py
    
    from django.contrib import admin
    from django.urls import path
    # 명시적 상태 경로
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('', views.index, name='index'),
        path('dinner/', views.dinner, name='dinner'),
        path('search/', views.search, name='search'),
        path('throw/', views.throw, name='throw'),
        path('catch/', views.catch, name='catch'),
        path('<int:num>/', views.detail, name='detail'),
    ]
    
    # 프로젝트의 urls.py
    from django.contrib import admin
    from django.urls import path, include
    from articles import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        # 클라이언트 요청 주소가 /articles/까지 일치 한다면,
        # 나머지 주소는 articles 앱의 urls.py로 넘긴다.
        path('articles/', include('articles.urls'))
    ]
    ```
    

## URL 이름 지정

- URL 이 많아지고 경로도 복잡해지면 관리도 어렵고 혹시 주소가 변경되면 사용하는 곳마다 다 들어가서 바꿔주기가 빡세다!
    
    → 그러니까 이름을 정해서 이름으로 관리하자!
    
- 어떻게 하느냐?!
    1. path 함수에 name 인자를 키워드 인자로 정의해서 사용한다
    
    ```python
    urlpatterns = [
        path('', views.index, name='index'),
        path('dinner/', views.dinner, name='dinner'),
        path('search/', views.search, name='search'),
        path('throw/', views.throw, name='throw'),
        path('catch/', views.catch, name='catch'),
        path('<int:num>/', views.detail, name='detail'),
    ]
    ```
    
    1. URL 을 사용하는 곳에는 URL tag 를 사용해서 호출(?)한다
    
    ```python
    <a href="{% url "articles:dinner" %}">저녁 메뉴 확인하러 가기!!</a>
    ```
    
- URL tag : 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
    
    `{% url 'url_name' arg1 arg2 %}`
    
    - URL 패턴에 변수가 포함되어 있으면, ‘url_name’ 이후 추가
        
        ```python
        # url.py
        path('<int:num>/', views.detail),
        ```
        
        ```python
        # articles/index.html
        
        <a href="{% url 'detail' 1 %}">Article 1</a>
        ```
        
    - DTL의 for 태그에서 사용한 변수 이름도 사용할 수 있음
        
        ```python
        # articles/views.py
        
        def index(request):
        		context = {
        				'nums' : [1, 2, 3],
        		}
        		return render(request, 'articles/index.html', context)
        ```
        
        ```python
        # articles/index.html
        
        {% for num in nums %}
        		<a href="{% url 'detail' num %}">Article {{ num }}</a>
        {% endfor %}
        ```
        

## URL 이름 공간

- URL 마다 이름을 정해 줬는데 서로 다른 app 에서 같은 이름을 쓰면 어떻게 하지?!
    
    → 이름에 성을 붙이자!
    
- 어떻게 하느냐?!
    1. urls.py 에 app_name 변수 설정 `app_name = '어플이름'`
        
        `app_name = 'articles'`
        
    2. app_name 이 추가 또는 수정되면 url 태그에 반영한다`{% url 'app_name:path_name' %}` 
        
        `{% url 'articles:search' %}`
        

## 참고

### 추가 템플릿 경로

- 앱 폴더 내부 templates 폴더 외에 템플릿을 위치하고 싶을 때, 템플릿 경로를 지정할 수 있음
- 프로젝트 폴더 내 settings.py 안에서 설정

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
		        BASE_DIR / 'templates',   # 여기가 원래 비어있는데 이렇게 추가
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### DTL 주의사항

- 장고 템플릿은 파이썬 문법과 비슷한 게 있어서(for, if 등) 오해할 수 있지만 파이썬 문법과 다르다!
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것
    
    → html 에서 하지 않기
    

### Trailing Slashes

- Django 는 URL 끝에 ‘/’ 가 없으면 자동으로 붙임
    
    → 모든 프레임워크가 그런건 아니고 Django는 그럼
    
- URL 뒤에 / 가 있는 것과 없는 것은 서로 다른 URL 임