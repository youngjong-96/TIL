# Django - Authentication System 01

<aside>

[요약]

- User model 대체하기
    1. user 모델 등록
        
        ```python
        # accounts/models.py
        
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        
        class User(AbstractUser):
            pass
        ```
        
    2. 프로젝트 기본 user 모델 변경
        
        ```python
        # 프로젝트폴더/settings.py
        
        AUTH_USER_MODEL = 'accounts.User'
        ```
        
    3. admin 등록
        
        ```python
        # accounts/admin.py
        
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.register(User, UserAdmin)
        ```
        
- login 함수 핵심
    
    ```python
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import login as auth_login
    
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            # GET 요청일 때 로그인 페이지를 응답
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    ```
    
</aside>

## Cookie & Session

### 1. HTTP

- HTTP 의 특징
    - 비 연결 지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음, 클라이언트는 서버와 연결되어 있지 않음
    - 무상태 : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
        
        → 장바구니 담은 상품, 로그인 상태 등 유지할 수 없음
        

### 2. 쿠키

- 쿠키 : 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 이를 통해 서버가 사용자를 기억하고 식별
- 쿠키의 특징
    - 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
    - key-value 형식의 데이터
- 쿠키 사용 예시
    - 로그인 유지
    - 장바구니
    - 언어, 테마 등 사용자 설정 기억
- 쿠키 사용 목적
    - 세션 관리
    - 개인화
    - 추적, 수집

### 3. 세션

- 세션 : 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지, 저장하는 데이터 저장 방식
- 로그인 정보와 같은 중요 데이터를 클라이언트가 아닌 서버 쪽에 저장하고 유지하는 기술
- 서버는 각 사용자를 구분하기 위한 세션 ID를 발급하고 이 ID를 쿠키에 담아 사용자를 식별
- 세션의 특징
    - 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지
    - 상태 정보를 저장하는 데이터 저장 방식
    - 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄
    - 영구적으로 유지되지 않음

## django Authentication System

- Django 에서 사용자 인증과 관련된 기능을 모아 놓은 시스템
- 인증에 중요한 기본적인 기능을 제공
    - User Model : 사용자 인증 후 연결될 User Model 관리
    - Session 관리 : 로그인 상태를 유지하고 서버에 저장하는 방식을 관리
    - 기본 인증 (Id/Password) : 로그인/로그아웃 등 다양한 기능을 제공

### 1. Custom User model

- 기본 User Model의 한계
    - 내장된 auth 앱에 작성된 User 클래스를 사용해야 하는데, 기본 User 모델은 제공되는 필드가 매우 제한적임
        
        → 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정하기 어려움
        
        → User Model 을 그대로 사용하지 않고 요구사항에 맞춰 확장해서 사용
        

### 2. User model 대체하기

- 사전 준비 : 계정을 관리할 두 번째 app ‘accounts’ 생성
    - 등록 → URL 설정
1. accounts 앱에서 User 모델 등록하기
    
    ```python
    # accounts/models.py
    
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    class User(AbstractUser):
        pass
    ```
    
2. 프로젝트에서 사용하는 기본 User 모델을 변경 (AUTH_USER_MODEL 값을 변경)
    
    ```python
    # 프로젝트폴더/settings.py
    
    AUTH_USER_MODEL = 'accounts.User'
    ```
    
3. admin site 에 대체한 User 모델 등록
    
    ```python
    # accounts/admin.py
    
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User
    
    admin.site.register(User, UserAdmin)
    ```
    

`프로젝트 중간에  AUTH_USER_MODEL 을 변경하는 것은 매우매우 위험!` 

`-> 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행해야 함` 

`이후 커스터마이징을 위해, 첫 migrate를 실행하기 전에 User 모델 대체 작업을 완료해야 함`

### Login

- Login : 인증을 완료하고 Session을 만들고 클라이언트와 연결하는 것
1. 로그인 경로 URL 생성
    
    ```python
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        path('login/', views.login, name='login'),
    ]
    ```
    
2. login 함수 작성 (로그인 페이지 요청을 처리하기 위한 else 로직 부분 먼저 작성)
    
    ```python
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        if request.method == 'POST':
            pass
        else:
            # GET 요청일 때 로그인 페이지를 응답
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    ```
    
3. login.html 작성
    
    ```html
    <h1>Login</h1>
      <form action="{% url "accounts:login" %}" method='POST'>
        {% csrf_token %}
        {{ form }}
        <input type="submit">
      </form>
    ```
    
4. login 함수 완성
    
    ```python
    from django.contrib.auth import login as auth_login
    
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            # GET 요청일 때 로그인 페이지를 응답
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    ```
    
- `login(request, user)`: AuthenticationForm 을 통해 인증된 사용자를 로그인 하는 함수
    - request : 현재 사용자의 세션 정보에 접근하기 위해 사용
    - user : 어떤 사용자가 로그인 되었는지를 기록하기 위해 사용
- `get_user()` : AuthenticationForm의 인스턴스 메서드
    - 유효성 검사를 통과했을 경우, 로그인 한 사용자 객체를 반환

### Template with Authentication data (템플릿에서 인증 관련 데이터를 출력하는 방법)

`{{ user.속성}}` 그냥 이렇게 쓰면 됨!

이게 어떻게 가능하냐?!

django에 context 데이터가 이미 존재하기 때문

(settings.py 에 TEMPLATES 부분에서 확인할 수 있음)

## 참고

### 1. 쿠키의 수명

- Session cookie
    - 현재 세션이 종료되면 삭제
    - 브라우저 종료와 함께 세션 삭제
- Persistent cookie
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제

### 2. 쿠키와 보안

- 제한된 정보 : 쿠키에는 보통 중요하지 않은 정보만 저장
- 암호화 : 중요한 정보는 암호화해서 저장
- 만료 시간 : 만료 시간 설정
- 도메인 제한 : 특정 웹사이트에서만 사용하도록 설정

### 3. Django 에서의 세션 관리

- Django 는 ‘database-backed sessions’ 저장 방식을 기본 값으로 사용
- session 정보는 DB의 `django_session` 테이블에 저장

### 4. User 모델 대체하기 Tip

- 모델 대체 순서가 헷갈리면 공식문서를 확인하자
    - https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#substituting-a-custom-user-model


# Django - Authentication System 02

### Logout

- 로그아웃은 Session 을 Delete하는 과정
- 서버의 세션 데이터를 비우고, 클라이언트의 세션 쿠키를 삭제
- 로그아웃 로직 작성
    1. URL 작성
        
        ```python
        # accounts/urls.py
        
        path('logout/', views.logout, name='logout'),
        ```
        
    2. view 함수 작성
        
        ```python
        # accounts/views.py
        
        from django.contrib.auth import logout as auth_logout
        
        def logout(request):
            auth_logout(request)
            return redirect('articles:index')
        ```
        
    3. html 수정
        
        ```html
        # articles/index.html
        
        <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
        </form>
        ```
        

### AbstracUser class

- Abstract base classes (추상 기본 클래스)
    - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
    - 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
- AbstractUser class
    - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스
    - 기본 User 모델이 가진 모든 필드가 이미 구현되어 있음
- 거의 AbstractUser class 를 상속받아서 사용할 경우가 많음


### 회원 가입

- 회원가입 로직 작성
    1. URL 작성
        
        ```python
        # accounts/urls.py
        
        path('signup/',views.signup, name='signup'),
        ```
        
    2. View 함수 작성
        
        ```python
        # accounts/views.py
        
        from .forms import CustomUserCreationForm
        
        def signup(request):
            if request.method == 'POST':
                # 사용자 입력 데이터 받기
                # ModelForm을 상속받아서 인자에 첫번째 인자가 data 여서 생략 가능
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('articles:index')
            else:
                # 회원가입 폼 (만들어진거 사용)
                form = CustomUserCreationForm()
            context = {
                'form': form
            }
            return render(request, 'accounts/signup.html', context)
        ```
        
    3. HTML 작성
        
        ```html
        # accounts/signup.html
        
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
        </head>
        <body>
          <h1>Signup</h1>
          <form action="{% url "accounts:signup" %}" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit">
          </form>
        </body>
        </html>
        ```
        
    4. 커스텀 유저 모델을 사용하기 위해서 form 을 작성
        
        ```python
        # accounts/forms.py
        
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib.auth import get_user_model
        
        class CustomUserCreationForm(UserCreationForm):
            class Meta(UserCreationForm.Meta):
                model = get_user_model()
        ```
        
        `get_user_model()` : 현재 프로젝트에서 “활성화된 사용자 모델”을 반환하는 함수
        

### 회원 탈퇴

- 회원탈퇴 로직 작성
    1. URL 생성
        
        ```python
        # accounts/urls.py
        
        path('delete/', views.delete, name='delete'),
        ```
        
    2. view 함수 작성
        
        ```python
        # accounts/views.py
        
        def delete(request):
            request.user.delete()
            return redirect('articles:index')
        ```
        
    3. html 수정
        
        ```html
        # articles/index.html
        
        <form action="{% url "accounts:delete" %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴">
        </form>
        ```
        

## 인증된 사용자에 대한 접근 제한

### is_authenticated 속성

- 사용자가 인증 되었는지 여부를 알 수 있는 User model 의 읽기 전용 속성
- 인증 사용자에 대해서는 항상 True, 비인증 사용자에 대해서는 항상 False
- 사용 예시
    - 사용자의 로그인 상태에 따라 다른 메뉴를 보여줄 때,
    - view 함수 내에서 특정 기능을 로그인한 사용자에게만 허용하고 싶을 때
- 인증된 사용자에 대해서 다른 화면 보여주기
    
    ```html
    # articles/index.html
    
    <body>
      <h1>메인 페이지</h1>
      {% if request.user.is_authenticated %}
      <h3>Hello, {{ user.username }}</h3>
      
      {% comment %} 로그아웃버튼 {% endcomment %}
      <form action="{% url "accounts:logout" %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
    
      {% comment %} 게시글 작성 버튼 {% endcomment %}
      <a href="{% url "articles:create" %}">CREATE</a>
      <hr>
    
      {% comment %} 전체 게시글 출력 {% endcomment %}
      {% for article in articles %}
        <div>
          <p>글 번호: {{ article.pk }}</p>
          <p>
            글 제목: <a href="{% url "articles:detail" article.pk %}">{{ article.title }}</a>
          </p>
          <p>글 내용: {{ article.content }}</p>
        </div>
        <hr>
      {% endfor %}
      
      {% comment %} 회원탈퇴 버튼 {% endcomment %}
      <form action="{% url "accounts:delete" %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
      {% else %}
      {% comment %} 로그인 {% endcomment %}
      <a href="{% url "accounts:login" %}">Login</a>
    
      {% comment %} 회원가입 {% endcomment %}
      <a href="{% url "accounts:signup" %}">회원가입</a>
      {% endif %}
    </body>
    ```
    
- 인증된 사용자가 주소를 이용해서 잘못된 접근 하려는 것 막기
    
    → 이미 로그인한 회원이 주소로 다시 로그인하거나 회원가입하려고 하면 메인화면으로 리다이렉트
    
    ```python
    # accounts/views.py
    
    def login(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
        ...
    
    def signup(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
        ...
    ```
    

### login_required 데코레이터

- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
- 비인증 사용자의 경우, /accounts/login/ 주소로 redirect 시킴
- 비인증 사용자가 게시글을 작성, 삭제, 수정할 수 없도록 데코레이터 적용
    
    ```python
    # articles/views.py
    
    from django.contrib.auth.decorators import login_required
    
    @login_required
    def create(request):
    
    @login_required
    def delete(request, pk):
    
    @login_required
    def update(request, pk):
    ```
    
    - 로그인 안하고 로그아웃, 회원탈퇴 불가
    
    ```python
    # accounts/views.py
    
    from django.contrib.auth.decorators import login_required
    
    @login_required
    def logout(request):
    
    @login_required
    def delete(request):
    ```
    

## 참고

### is_authenticated 코드

- 메서드가 아닌 속성 값임을 주의!

### 회원가입 후 자동 로그인

```python
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()            # 여기 부분 수정
            auth_login(request, user)     # 여기 부분 추가
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

### 회원 탈퇴 개선

- 회원 탈퇴 이후에도 로그인했던 세선 데이터는 남아있는데 이것도 삭제하려면
    
    ```python
    def delete(request):
        request.user.delete()
        auth_logout(request)  # 이 코드 추가
        return redirect('articles:index')
    ```
    
    `단, 탈퇴 후 로그아웃이 진행되어야 함. 로그아웃이 먼저되면 탈퇴할 회원 정보가 없음`
    

# Django - Authentication System 03

### 회원정보 수정

1. URL 작성
    
    ```python
    # accounts/urls.py
    
    path('update/', views.update, name='update'),
    ```
    
2. UserChangeForm 커스터마이징
    
    ```python
    # accounts/forms.py
    
    from django.contrib.auth.forms import UserChangeForm
    
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            fields = ('email', 'first_name', 'last_name')
            model = get_user_model()
    ```
    
3. views 함수 작성
    
    ```python
    # accounts/views.py
    
    from .forms import CustomUserCreationForm, CustomUserChangeForm
    
    def update(request):
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/update.html', context)
    ```
    
4. html 수정
    
    ```html
    # accounts/update.html
    
    <form action="{% url "accounts:update" %}" method="POST">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
    ```
    

## 비밀번호 변경

- 인증된 사용자의 Session 데이터를 Update 하는 과정
- 기존 비밀번호를 통해 사용자를 인증하고, 새로운 비밀번호를 암호화하여 갱신
- 비밀번호 변경 로직 작성
    1. URL 작성 (Django에서 제공하는 URL 주소)
        
        ```python
        # accounts/urls.py
        
        path('password/', views.password, name='password'),
        ```
        
    2. view 함수 작성
        
        ```python
        # accounts/views.py
        
        from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
        
        def password(request):
            if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    return redirect('articles:index')
            else:
                form = PasswordChangeForm(request.user)
            context = {
                'form': form
            }
            return render(request, 'accounts/password.html', context)
        ```
        
    3. html 작성
        
        ```html
        # accounts/password.html
        
        <form action="{% url "accounts:password" %}" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit">
        </form>
        ```
        

### 세션 무효화 방지

`update_session_auth_hash(requeset, user)` : 암호 변경 시 세션 무효화를 막아주는 함수

```python
# accounts/views.py

from django.contrib.auth import update_session_auth_hash

def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/password.html', context)
```

### 비밀번호 암호화

- 해시함수를 이용해서 비밀번호를 고정된 길이의 임의의 문자열로 변환
- django 는 기본적으로 SHA-256 해시 함수를 사용
    - SHA-256 (Secure Hash Algorithm - 256): 256비트 길이의 결과물을 반환

https://d2.naver.com/helloworld/318732

## 참고

### 비밀번호 초기화

- 비밀번호를 잊어버린 사용자가 이메일을 활용하여 비밀번호를 다시 설정하는 과정
    - 비밀번호를 찾으려고 하는 이메일 입력
    - 이메일로 비밀번호 재설정 링크를 전송
    - 비밀번호 재설정 페이지에서 새로운 비밀번호 설정
    - 초기화 후 다시 로그인
- 초기화 로직 구현
    1. URL 생성
        
        ```python
        # crud/urls.py
        
        path('accounts/', include('django.contrib.auth.urls')),
        ```
        
    2. 만들어진 링크를 활용해서 화면 확인
        - [`http://127.0.0.1:8000/accounts/password_reset/`](http://127.0.0.1:8000/accounts/password_reset/) 접속하면 이메일 발송 페이지 확인 가능

### PasswordChangeForm 인자 순서

- PasswordChangeForm이 다른 Form과 달리 user 객체를 첫번째 인자로 받는 이유
    - 부모 클래스인 SetPasswordForm의 생성자 함수 구성을 따르기 때문