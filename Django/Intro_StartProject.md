# Django - Intro & Design Pattern

<aside>
💡

[요약]

1. 가상 환경 생성 `python -m venv venv` 
2. 가상 환경 활성화 `source venv/Scripts/activate` 
3. Django 설치 `pip install django` 
4. 패키지 목록 파일 생성 `pip freeze > requirements.txt` 
    - `pip install -r requirements.txt` : requirements.txt 로부터 패키지 설치
5. Django 프로젝트 생성 `django-admin startproject 프로젝트명 .` 
6. 서버 실행 `python [manage.py](http://manage.py) runserver` 
7. 앱 생성 `python [manage.py](http://manage.py) startapp 앱이름` 
8. 프로젝트 폴더 아래 “settings.py”

```python
# Application definition

INSTALLED_APPS = [
    'my_app',    # 이거 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

1. 프로젝트 폴더 아래 “urls.py”

```python
from 앱이름 import view

path('앱이름/', view.index)
```

1. 앱 폴더 아래 “view.py” 

```python
def index(request):
    return render(request, 'articles/index.html')
```

1. 앱 폴더 아래 “templates” 폴더 만들고 그 아래 ‘articles’ 폴더 만들고 그 아래 html 작성
</aside>

## Web Application

### 클라이언트와 서버

- 웹 페이지를 보게 되는 과정
    1. 웹 브라우저(클라이언트)에서 ‘google.com’ 입력 후 Enter
    2. 웹 브라우저는 인터넷에 연결된 전세계 어딘 가에 있는 구글 컴퓨터(서버)에게 `메인 홈페이지.html` 파일을 달라고 요청
    3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 `메인 홈페이지.html` 파일을 찾아 응답
    4. 웹 브라우저는 전달받은 `메인 홈페이지html` 파일을 사람이 볼 수 있도록 해석해주고 사용자는 구글의 메인 페이지를 보게 됨

### Frontend & Backend

- Frontend(프론트엔드)
    - 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
    - HTML, CSS, JavaScript, 프론트엔드 프레임워크(Vue) 등
- Backend(백엔드)
    - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
    - 서버 언어(Python, Java 등) 및 백엔드 프레임워크(Django), DB, API, 보안 등

## Framework

### Web Framework : 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구

- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

### Django Framework : Python 기반 대표적인 웹 프레임워크

- “클라이언트 - 서버” 구조의 서버를 구현하는 것이 Django를 배우는 목적!

## 가상 환경

<aside>
💡

[요약]

1. 가상 환경 생성 `python -m venv venv`
2. 가상 환경 활성화 `source venv/Scripts/acdtivate`
3. 필요한 의존성 패키지 설치 `pip install`
4. 현재 환경의 패키지 목록을 `pip freeze > requirements.txt` 로 저장
5. 다른 환경에서도 동일한 설치를 하려면 `pip install -r requirements.txt` 
6. 작업이 끝나면 `deactivate` 로 가상환경 비활성화
</aside>

- 하나의 컴퓨터 안에서 또 다른 ‘독립된’ 파이썬 환경 생성


### 가상 환경 생성 및 활성화

1. 가상 환경 생성
    - `python -m venv venv` : 현재 디렉토리 안에 venv 라는 폴더가 생성됨, venv 라는 이름의 가상 환경을 생성한 것
2. 가상 환경 활성화
    - `source venv/Scripts/activate` : venv/Scripts/ 경로에 있는 activate 파일 실행
    - 활성화 후, 프롬프트 앞에 (venv) 와 같이 표시된다면 성공한 것
3. 가상 환경 종료
    - `deactivate` : 활성화한 상태에서 deactivate 명령을 입력하면, Python Global 환경으로 돌아옴
    - 그냥 꺼도 가상환경 꺼지는데 정상적인 종료는 명령어를 입력해서 끄는 거

### 의존성 패키지

- 의존성 : 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리
- 의존성 패키지 : 프로젝트가 의존하는 “개별 라이브러리”들을 가리키는 말
- `pip list` : 현재 환경에 설치된 라이브러리 목록을 확인
- `pip freeze > requirements.txt`
    - `pip freeze` : 가상 환경에 설치된 모든 패키지를 버전과 함께 특정한 형식으로 출력
    - 이를 requirements.txt 라는 파일로 저장해서 나중에 동일한 환경 재현에 활용
    
    <aside>
    💡
    
    - “>” 는 pip  명령어가 아닌 CLI 의 Redirection operator로 이전 명령어의 출력을 파일로 redirect, 즉 생성하고 작성 합니다
    - 같은 명령어를 다시 사용할 경우 이전 파일의 내용을 덮어씁니다
    </aside>
    

### 의존성 패키지 기반 설치

- `pip install -r requirements.txt` : requirements.txt 로부터 패키지 설치

### 가상 환경 주의사항

- 가상 환경에 ‘들어가고 나오는’ 것이 아니라 사용할 Python 환경을 ‘on/off’ 로 전환하는 개념
- 프로젝트마다 별도의 가상 환경을 사용
- 일반적으로 가상 환경 폴더 venv는 관련된 프로젝트와 동일한 경로에 위치시킴
- 폴더 venv는 .gitignore 파일에 작성되어 원격 저장소에 공유하지 않음

## Django 프로젝트

### Django 프로젝트 생성 및 서버 실행

1. Django 설치
    - `pip install django` : 현재 환경에 Django 패키지를 설치
2. 프로젝트 생성
    - `django-admin startproject firstpjt .` : 현재 디렉토리( . )에 “firstpjt” 라는 이름의 프로젝트 생성
3. 서버 실행
    - `python manage.py runserver` : manage.py 폴더에 있는 runserver 명령 실행
        - ⚠️ manage.py 와 동일한 위치에서 명령어를 실행해야 함
        - ⚠️ ctrl + c 를 눌러서 서버 종료

## Django Design Pattern

### Design Pattern

- 디자인패턴 : 소프트웨어 설계에서 반복적으로 발생하는 문제에 대한, 검증되고 재사용 가능한 일반적인 해결책
- MVC 디자인 패턴 - 하나의 애플리케이션을 구조화하는 대표적인 구조적 디자인 패턴
    - Model : 데이터 및 비즈니스 로직을 처리
    - View : 사용자에게 보이는 화면을 담당
    - Controller : 사용자의 입력을 받아 Model 과 View 를 제어
- MTV 디자인 패턴
    - Model / Template ( = View) / View ( = Controller)

### 프로젝트와 앱

- 프로젝트 : 애플리케이션의 집합
    - DB 설정, URL 연결, 전체 앱 설정 등
- 애플리케이션 : 독립적으로 작동하는 기능 단위 모듈
    - 각자 특정한 기능을 담당
    - 다른 앱들과 함께 하나의 프로젝트를 구성
1. 앱 생성
    - `python manage.py startapp articles` : articles 라는 폴더와 내부에 여러 파일이 생성
2. 앱 등록
    - 프로젝트에 새로 만든 앱을 등록해준다
    - 프로젝트 폴더 안에 ‘settings.py’ 파일 안에 ‘INSTALLED_APPS’ 라는 리스트 안에 문자열로 새로 만든 앱 폴더명을 추가해준다
    - 추가할 때는 리스트 앞으로 추가해주는 것이 좋음 (Django의 동작 순서 때문)

### 프로젝트 및 앱 구조

- 프로젝트 구조
    - ⭐settings.py : 프로젝트의 모든 설정을 관리
    - ⭐urls.py : 요청 들어오는 URL에 따라 이에 해당하는 적절한 views 를 연결
    - init.py : 해당 폴더를 패키지로 인식하도록 설정하는 파일
    - asgi.py : 비동기식 웹 서버와의 연결 관련 설정
    - wsgi.py : 웹 서버와의 연결 관련 설정
    - manage.py : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
- 앱 구조
    - admin.py : 관리자용 페이지 설정
    - ⭐models.py : DB와 관련된 model을 정의
    - ⭐views.py : HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환, url, model, template 과 연동
    - apps.py : 앱의 정보가 작성된 곳
    - tests.py : 프로젝트 테스트 코드를 작성하는 곳

## 참고

### 가상 환경 생성 루틴

- Django 프로젝트 생성 전 루틴
    1. 가상 환경 생성 `python -m venv venv` 
    2. 가상 환경 활성화 `source venv/Scripts/activate` 
    3. Django 설치 `pip install django` 
    4. 패키지 목록 파일 생성 `pip freeze > requirements.txt` (패키지 설치시마다 진행)
- Django 프로젝트를 git 저장소로 만드는 경우
    1. 가상 환경 생성
    2. 가상 환경 활성화
    3. Django 설치
    4. 패키지 목록 파일 생성
    5. gitignore 파일 생성 ( 첫 add 전 진행 )
    6. git 저장소 생성 (git init)
    7. Django 프로젝트 생성

### Python 패키지 설치법

| 명령어 예시 | 의미 |
| --- | --- |
| pip install SomePackage | 최신 버전 설치 |
| pip install SomePackage == 1.0.5 | 특정 버전 설치 |
| pip install SomePackage >= 1.0.4 | 최소 버전(1.0.4) 이상을 설치 |
| pip install SomePackage ~= 1.0.4 | 호환 버전 이상(1.0.4) ~ 다음 마이너 버전(1,1,0) 미만 설치 |

### render 함수

`render(request, template_name, context)` 

: 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse 응답 객체를 반환하는 함수

### MTV 디자인 패턴 정리

- Model (models.py)
    - 데이터와 관련된 로직을 관리
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- Template (<filename>.html)
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
- View (views.py)
    - Model & Template 과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할

### 프레임워크의 규칙 및 설계 철학

- Django의 규칙
    - urls.py에서 각 url 문자열 경로는 반드시 ‘/’ 로 끝남
    - views.py에서 모든 view 함수는 첫번째 인자로 요청 객체를 받음 (request)
    - Django는 특정 경로에 있는 template 파일만 읽어올 수 있음 (app 폴더/templates)
