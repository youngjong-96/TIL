# Django - Model

<aside>
💡

요약

- 모델이 동작하는 기본 과정
1. 앱 폴더 내 models.py 에서 기본 설계
    
    ```python
    # articles/models.py
    class Article(models.Model):    # models 모듈의 model 이라는 부모 클래스 상속
        title = models.CharField(max_length=10)   # 필드이름 = 데이터 유형, 제약 조건
        content = models.TextField()
    ```
    
2. 마이그레이션 파일 생성 `python manage.py makemigrations`
    
    → 앱 폴더 내 migrations 폴더 내 ‘0001_initial.py’ 파일 생성
    
3. 마이그레이션 파일을 DB에 반영 `python manage.py migrate`

- 관리자 인터페이스
1. 생성 : `python manage.py createsuperuser`
2. 모델 등록
    
    ```python
    # articles/admin.py
    
    from django.contrib import admin
    from .models import Article
    
    # Register your models here.
    # 관리자 사이트에 등록한다
    admin.site.register(Article)
    ```
    
</aside>

## Model

- Model : 데이터베이스와 Python 클래스(객체)로 추상화된 형태로 상호작용
- Model 을 통한 DB 관리
    - urls.py: 사용자 요청의 시작점
    - views.py: 요청을 처리하고 models.py를 통해 데이터를 다룸
    - models.py: 데이터베이스를 정의하고, 데이터베이스와 상호작용
    - templates: view.py로부터 받은 데이터를 사용자에게 보여줄 화면을 구성

### Model Class : DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공

```python
# articles/models.py
class Article(models.Model):    # models 모듈의 model 이라는 부모 클래스 상속
    title = models.CharField(max_length=10)   # 필드이름 = 데이터 유형, 제약 조건
    content = models.TextField()
```



## Model Field

### Field Types

- Field Types : 데이터베이스에 저장될 “데이터의 종류” 를 정의 - models 모듈의 클래스로 정의되어 있음
- 종류
    - 문자열 필드
        - CharField( ) : 제한된 길이의 문자열을 저장 (max_length는 선택 옵션)
        - TextField( ) : 길이 제한이 없는 대용량 텍스트를 저장 (무한대는 아니고 사용하는 시스템에 따라 달라짐)
    - 숫자 필드
        - IntegerField( ), FloatField( )
    - 날짜 / 시간 필드
        - DateField( ), TimeField( ), DateTimeField( )
    - 파일 관련 필드
        - FileField( ), ImageField( )

### Field Options

- Field Options : 필드의 동작과 제약 조건을 정의
- 주요 옵션
    - null : DB에서 NULL 값을 허용할지 여부를 결정 (기본값 : False)
    - blank : form에서 빈 값을 허용할지 여부를 결정 (기본값 : False)
    - default : 필드의 기본값을 설정

## Migrations

- Migrations : model 클래스의 변경사항(필드 생성, 수정 삭제 등) 을 DB 에 최종 반영하는 방법
    1. `python manage.py makemigrations` : 마이그레이션 파일 생성 명령어
    2. `python manage.py migrate` : 마이그레이션 파일(생성된 최종 설계도)을 DB에 반영하기

### 추가 Migrations - 이미 생성된 테이블에 필드 추가

1. models.py 에 새로운 필드 작성
    
    ```python
    # articles/models.py
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
    
2. `python manage.py makemigrations` 명령어 입력 → 변경사항 기반 설계도 생성
    
    → 이 때, 기본값(default) 설정이 필요함
    
    a. 현재 대화를 유지하면서 직접 기본 값을 입력
    
    b. 현재 대화에서 나간 후 models.py에 기본 값 관련 설정 하기
    
    → 2가지 옵션 중 a 옵션 선택 후 django가 기본으로 추천해주는 기본값으로 설정하면 0002 설계도 만들어줌
    
3. `python manage.py migrate` 명령어 입력 → 수정사항 DB 반영
    - git 처럼 설계도가 변경되면 수정사항을 저장함 → 기존 설계도 그대로 가지고 있어야 함

## Admin site

### 관리자 인터페이스

- 관리자 인터페이스 : Django 가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
    - 데이터베이스 모델의 CRUD 작업을 간편하게 수행
    - 빠른 프로토타이핑, 비개발자 데이터 관리, 내부 시스템 구축에 이상적
- `python manage.py createsuperuser` : 관리자계정 생성
- admin.py 에 내가 만든 모델 클래스를 등록해야 admin site 에서 확인 가능
    
    ```python
    # articles/admin.py
    
    from django.contrib import admin
    from .models import Article
    
    # Register your models here.
    # 관리자 사이트에 등록한다
    admin.site.register(Article)
    ```
    

## 참고

### Migrations 관련

- `python manage.py showmigrations` : migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어, [x] 표시가 있으면 migrate 가 완료되었음을 의미
    
    ```python
     # 실행 결과
     [X] 0009_alter_user_last_name_max_length
     [X] 0010_alter_group_name_max_length
     [X] 0011_update_proxy_permissions
     [X] 0012_alter_user_first_name_max_length
    contenttypes
     [X] 0001_initial
     [X] 0002_remove_content_type_name
    sessions
     [X] 0001_initial
    ```
    
- `python manage.py sqlmigrate <앱이름><마이그레이션 이름>` : 해당 migrations 파일이 SQL언어로 어떻게 번역 되어 DB에 전달되는지 확인하는 명령어
    
    ex. `python manage.py sqlmigrate articles 0001`
    
    ```python
    # 실행 결과
    BEGIN;
    --
    -- Create model Article
    --
    CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL); 
    COMMIT;
    ```
    

### SQLite

- Django 의 기본 데이터베이스
    - 파일 기반 : 데이터베이스가 하나의 파일로 저장되어, 설치/설정 없이 간편하게 복사/이동/백업 가능
    - 가볍고 빠름 : 별도 서버 없이 파일로 직접 데이터 처리. 소규모 앱이나 모바일 환경에 적합
    - 높은 호환성 : 다양한 운영체제와 프로그래밍 언어에서 폭넓게 사용 가능
- SQLite 주의사항
    - db.sqlite3 파일은 Git 등 버전관리 시스템에서 관리하지 않도록 gitignore에 추가