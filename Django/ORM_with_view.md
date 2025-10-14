# 9/25(목) - Django (ORM with view)

# Django - ORM with view

### 전체 게시글 조회

- 앱 내 views.py 에서 DB 에서 원하는 정보를 받아오는 코드 작성
    
    ```python
    from django.shortcuts import render
    from .models import Article
    
    # Create your views here.
    # 전체 게시글 조회 후 메인 페이지 응답
    def index(request):
        # 1. DB 에 전체 게시글을 조회
        articles = Article.objects.all()
    
        # 2. 전체 게시글 목록을 템플릿과 함께 응답
        context = {
            'articles': articles,
        }
    
        return render(request, 'articles/index.html', context)
    ```
    
- index.html 에서 받아온 정보를 활용
    
    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <h1>메인 페이지</h1>
      {% for article in articles %}
        <p>{{article.pk}}</p>
        <p>{{article.title}}</p>
        <p>{{article.content}}</p>
        <hr>
      {% endfor %}
    </body>
    </html>
    ```
### Read

```python
# articles/views.py
def detail(request, pk):
    # 1. 단일 게시글 조회
    article = Article.objects.get(pk=pk)

    # 2. 단일 게시글 데이터와 템플릿을 응답
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```python
# articles/detail.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Detail</h1>
  <h2>{{article.pk}} 번째 글</h2>
  <hr>
  <p>제목: {{article.title}}</p>
  <p>내용: {{article.content}}</p>
  <p>작성일: {{article.created_at}}</p>
  <p>수정일: {{article.updated_at}}</p>
  <a href="{% url "articles:index" %}">[메인 페이지로]</a>
</body>
</html>
```

```python
# articles/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>메인 페이지</h1>
  <hr>
  {% comment %} 전체 게시글 출력 {% endcomment %}
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      글 제목: {{ article.title }}
    </a>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
</body>
</html>

```

### Create - 이전 throw, catch 처럼 두 개의 view 함수가 필요

```python
# articles/views.py

# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자가 작성한 글을 추출해서 DB에 저장하고 완료되었다는 페이지를 응답
def create(request):
    # 1. 사용자가 작성한 글을 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. DB에 저장
    # 2.1
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 2.2
    article = Article(title=title, content=content)
    article.save()

    # 2.3
    Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
```

```python
# articles/new.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>New</h1>
  <form action="{% url "articles:create" %}" method="">
    <div>
      <label for="title">Title: </label>
      <input name='title' type="text" id='title'>
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name='content' id="content"></textarea>
    </div>
    <input type="submit">
  </form>
  
  <hr>

  <a href="">[back]</a>
</body>
</html>

```

## HTTP request methods

### HTTP : 네트워크 상에서 데이터를 주고 받기 위한 약속

- HTTP request methods : 데이터에 대해 수행을 원하는 작업(행동)을 나타내는 것
- 메서드 종류
    - GET : 리소스 조회, URL에 데이터가 노출됨, 캐싱 가능
        - 캐싱 : 자주 사용하는 데이터를 임시로 저장하고 재활용하여 처리 속도 높이는 기술
    - POST : 데이터 생성/전송, 요청 본문에 데이터, 데이터 노출 없음

### GET method

- 서버로부터 데이터를 요청하고 받아오는 데(조회) 사용
- 검색 쿼리 전송, 웹 페이지 요청, API에서 데이터를 조회하는 것과 같이 서버로부터 데이터를 요청하고 받아오는 데 주로 사용
- 특징
    - URL의 쿼리 문자열을 통해 데이터를 전송
    - 데이터 제한이 있음 (URL 에 담아서 전송해야 하니까)
    - 브라우저 히스토리 - 요청 URL이 브라우저 히스토리에 남음
    - 캐싱 - 브라우저는 GET 요청의 응답을 로컬에 저장하고 다음에 다시 요청이 올 때 서버에 접속하지 않고 저장된 결과를 사용해서 로딩 시간을 단축할 수 있음

### POST method

- 서버에 데이터를 제출하여 리소스를 변경(생성, 수정, 삭제) 하는 데 사용
- 로그인 정보 제출, 파일 업로드, 새 데이터 생성, API에서 데이터 변경을 요청하는 것과 같이 서버로 데이터를 전송하여 서버의 상태를 변경할 때 주로 사용
- 특징
    - HTTP Body를 통해 데이터를 전송
    - GET에 비해 더 많은 양의 데이터를 전송할 수 있음
    - 브라우저 히스토리에 남지 않음
    - POST 요청은 기본적으로 캐시할 수 없음


## HTTP response status code

- 서버가 클라이언트의 요청에 대한 처리 결과를 나타내는 3자리 숫자

### CSRF

- CSRF (Cross-Site-Request-Forgery) : 사이트 간 요청 위조, 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행동을 특정 웹사이트에 요청하게 만드는 해킹 방식
- Django 는 이러한 공격을 막기 위해 CSRF 토큰(일회용 비밀 코드)을 사용
- Django 서버는 DB에 영향을 주는 요청에 대해 Django가 직접 제공한 페이지에서 데이터를 작성하고 있는 것인지에 대한 확인 수단이 필요
- 겉모습이 똑같은 위조 사이트나 정상적이지 않은 요청에 대한 방어 수단
- GET 요청은 확인 안함, POST 요청일 때 확인

### Redirect

- POST 요청을 받은 이후 완료 페이지를 응답하는 것이 아닌 사용자를 적절한 기존 페이지로 보내야 함
    
    → 서버가 클라이언트를 직접 다른 페이지로 보낼 수 없으니 클라이언트가 GET 요청을 한 번 더 보내도록 응답
    
- `redirect()` : 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
    
    ```python
    # render에서 redirect로 변경된 create 함수
    
    def create(request):
        
        title = request.POST.get('title')
        content = request.POST.get('content')
    
        article = Article(title=title, content=content)
        article.save()
        
        # 작성된 글로 redirect
        return redirect('articles:detail', article.pk)
    ```
    

    

### Delete

1. 삭제 URL 추가
    
    `path('int:pk/delete/', views.delete, name='delete'),`
    
2. view 함수 만들기 ( 메인페이지로 redirect)
    
    ```python
    def delete(request, pk):
        # 1. 어떤 게시글 삭제할지 조회
        article = Article.objects.get(pk=pk)
    
        # 2. 조회한 게시글을 삭제
        article.delete()
    
        return redirect('articles:index')
    ```
    
3. 삭제버튼 html에 추가
    
    ```python
    # detail.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <h1>Detail</h1>
      <h2>{{article.pk}} 번째 글</h2>
      <hr>
      <p>제목: {{article.title}}</p>
      <p>내용: {{article.content}}</p>
      <p>작성일: {{article.created_at}}</p>
      <p>수정일: {{article.updated_at}}</p>
      <hr>
      #### 여기 삭제 버튼 추가 ####
      <form action="{% url "articles:delete" article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
      #### 여기까지 ####
      <a href="{% url "articles:index" %}">[메인 페이지로]</a>
    </body>
    </html>
    
    ```
    

### Update - 2개의 view 함수가 필요

1. url 추가
    
    ```python
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    ```
    
2. view 함수 만들기
    
    ```python
    # 수정하는 edit
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            'article':article
        }
        return render(request, 'articles/edit.html', context)
    
    # 수정 저장 update
    def update(request, pk):
        article = Article.objects.get(pk=pk)
    
        title = request.POST.get('title')
        content = request.POST.get('content')
    
        article.title = title
        article.content = content
        article.save()
    
        return redirect('articles:detail', article.pk)
    ```
    
3. html 만들기
    
    ```python
    # edit.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <h1>Edit</h1>
      <form action="{% url "articles:update" article.pk %}" method="POST">
        {% csrf_token %}
        <div>
          <label for="title">Title: </label>
          <input name='title' type="text" id='title' value="{{ article.title }}">
        </div>
        <div>
          <label for="content">Content: </label>
          <textarea name='content' id="content">{{ article.content }}</textarea>
        </div>
        <input type="submit">
      </form>
    </body>
    </html>
    
    ```
    

## 참고

### GET & POST 비교

|  | GET | POST |
| --- | --- | --- |
| 데이터 전송 방식 | URL의 Query string parameter | HTTP body |
| 데이터 크기 제한 | 브라우저 제공 URL 의 최대 길이 | 제한 없음 |
| 사용 목적 | 데이터 검색 및 조회 | 데이터 제출 및 변경 |
- 동일한 URL 한 개로 method 에 따라 서버에 요구하는 행동을 다르게 할 수 있다!
    - GET articles/1/ → 1번 게시글 조회 요청
    - POST articles/1/ → 1번 게시글 조작 요청

### 캐시 (Cache)

- 데이터나 정보를 임시로 저장하여 다시 요청할 때 빠르게 제공하는 저장 공간