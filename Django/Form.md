# Django - Form

<aside>
💡

[요약]

- Form
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```
    
- ModelForm
    
    ```python
    # articles/forms.py
    
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__'
    ```
    
- new + create
    
    ```python
    # articles/views.py
    
    def create(request):
        if request.method == "POST":
            # create 부분 실행
            form = ArticleForm(request.POST)
    
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            # new 부분 실행
            form = ArticleForm()
        
        # new, create 공통 부분
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    
- edit + update
    
    ```python
    # articles/view.py
    
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == "POST":
            # 기존 update 부분
            form = ArticleForm(request.POST, instance=article)
    
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            # 기존 edit 부분
            form = ArticleForm(instance=article)
        
        # 공통 부분
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    
</aside>

## Django Form

- html 의 form 은 사용자가 입력한 데이터의 유효성 검사를 할 수 없다
    
    → Django 의 form 을 사용
    

### 1. Form Class

- Django Form : 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```
    
    ```python
    # articles/views.py
    
    from .forms import ArticleForm
    
    def new(request):
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    
    ```html
    <!-- articles/new.html -->
    
    <h1>New</h1>
      <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{ form }}
        
        <input type="submit">
      </form>
    ```
    

### 2. Widgets

- widgets : HTML ‘input’ element 의 표현을 담당, input 요소의 속성 및 출력되는 부분을 변경하는 것
    
    ```python
    content = forms.CharField(widget=forms.Textarea)
    ```
    

### 3. Django ModelForm

- ModelForm
    - model 과 연결된 form 을 자동으로 생성해주는 기능을 제공
    - 데이터 수집과 저장 과정을 동시에 처리할 수 있도록 도와줌
    
    ```python
    # articles/forms.py
    
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = '__all__'
    ```
    
- Form vs ModelForm
    - Form : 사용자 입력 데이터를 DB에 저장하지 않을 때 ( ex. 검색, 로그인)
    - ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 ( ex. 게시글 작성, 회원가입)

### 4. Meta class

- Meta class : ModelForm 의 정보를 작성하는 곳
- ‘fields’ 및 ‘exclude’ 속성
    - fields - 포함, exclude - 제거
    
    ```python
    # fields
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = ('title',)
    
    # exclude
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            exclude = ('title',)
    ```
    
- Meta class 주의사항
    - Django 에서 ModelForm 에 대한 추가 정보나 작성하는 클래스 구조를 Meta 클래스로 작성했을 뿐, 파이썬의 inner class 와 같은 문법적인 관점으로 접근 x

### 5. ModelForm 적용

- ModelForm 을 적용한 create 로직
    
    ```python
    # articles/views.py
    
    def create(request):
        # 사용자 입력 데이터를 통째로 form 클래스의 인자로 넣어서 인스턴스 생성
        form = ArticleForm(request.POST)
    
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사를 통과하면 바로 저장하고 반환한 객체를 다시 article로 저장
            article = form.save()
            return redirect('articles:detail', article.pk)
        
        # 유효성 검사를 통과하지 못하면 에러 메세지를 포함해서 해당 페이지를 다시 응답
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    
    - `is_valid()` : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean 으로 반환
- ModelForm 을 적용한 edit 로직
    
    ```python
    # articles/views.py
    
    def edit(request, pk):
        # 수정할 article pk로 조회
        article = Article.objects.get(pk=pk)
        # 사용자가 기존 입력한 데이터 전달
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    
- ModelForm을 적용한 update 로직
    
    ```python
    # articles/views.py
    
    def update(request, pk):
        # 수정할 게시글 조회
        article = Article.objects.get(pk=pk)
        
        # 사용자가 입력한(수정한) 데이터를 통째로 받음
        form = ArticleForm(request.POST, instance=article)
    
        # 유효성 검사 통과하면 유효성 검사 후 리다이렉트
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
        
        # 유효성 검사 통과 못하면 해당 페이지를 다시 줌
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    

### 6. save 메서드

- `save()` : 데이터베이스 객체를 만들고 저장하는 ModelForm 의 인스턴스 메서드
- 키워드 인자 instatnce 여부를 통해 생성 or 수정 결정
    
    ```python
    # CREATE
    form = ArticleForm(request.POST)
    form.save()
    
    # UPDATE
    form = ArticleForm(request.POST, instance = article)
    form.save()
    ```
    

## HTTP 요청 다루기

### 1. View 함수 구조 변화

- HTTP request method (POST, GET) 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 구조화

### 2. new & create 함수 결합

- views.py 에 new와 create 함수를 하나로 결합
    
    ```python
    # articles/views.py
    
    def create(request):
        if request.method == "POST":
            # create 부분 실행
            form = ArticleForm(request.POST)
    
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            # new 부분 실행
            form = ArticleForm()
        
        # new, create 공통 부분
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    
- 기존 new 가 있던 것들 모두 create로 수정
    - url, html, 연결 함수 등

### 3. edit & update 함수 결합

- views.py 에 edit과 update 함수를 하나로 결합
    
    ```python
    # articles/view.py
    
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == "POST":
            # 기존 update 부분
            form = ArticleForm(request.POST, instance=article)
    
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            # 기존 edit 부분
            form = ArticleForm(instance=article)
        
        # 공통 부분
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    
- 기존 edit 이 있던 부분 모두 update로 수정

## 참고

### 1. ModelForm 의 키워드 인자 구성

- data 인자 : 첫번째 인자로 생략 가능
- instance 인자 : 9번째 인자로 생략 불가능

### 2. Widgets 응용

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title 부분에 여러 widget 적용
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'ma-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    # content 부분에 여러 widget 적용
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )
    
    class Meta:
        model = Article
        fields = ('__all__')
```


### 3. 필드를 수동으로 렌더링

```python
{{ form.non_field_errors }}
  <form action="{% url "articles:create" %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      <label for="{{ form.title.id_for_label }}">Title:</label>
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      <label for="{{ form.content.id_for_label }}">Content: </label>
      {{ form.content }}
    </div>
    <input type="submit">
  </form>
```

