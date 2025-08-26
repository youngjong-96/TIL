# Web CSS Layout

## CSS Box Model

### 1. display 속성

- 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐
- 박스 타입
    - Block 타입 : 하나의 독립된 덩어리처럼 동작하는 요소
        
        `display : block;` 
        
        - 항상 새로운 행으로 나뉨(한 줄 전체를 차지, 너비 100%)
        - width, height, margin, padding 모두 사용 가능
        - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
        - 대표적인 block 타입 태그 : h1~6, p, **div**, ul, li
    - Inline 타입 : 문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소
        
        `display : inline;`
        
        - 줄바꿈 없음
        - width 와 height 속성 사용 불가
        - 대표적인 inline 타입 태그 : a, img, **span**, strong

### 2. Normal flow

- normal flow : 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

### 3. 기타 display 속성

- inline - block  `display : inline-block`
    - inline 과 block 의 특징을 모두 가진 특별한 display 속성 값
    - block 과 inline 특징을 합친 것 - 줄바꿈 없이, 크기 지정 가능
    - width 및 height 속성 사용 가능
    - 주로 가로로 정렬된 네비게이션 메뉴나 여러 개의 버튼, 이미지 갤러리처럼 수평으로 나열하면서, 각 항목의 크기를 직접 제어하고 싶을 때 사용
- none `display : none`
    - 요소를 화면에 표시하지 않고, 공간도 부여하지 않음
    - “예비” 느낌

## CSS Position

- position 이동방향 : 상, 하, 좌, 우, Z축(모니터와 수직 방향)

### 1. Position 유형

- static - 기본 위치
    - 요소를 normal flow 에 따라 배치
    - top, right, bottom, left 속성이 적용되지 않음
    - 기본 값
- relative - 상대 위치
    - 요소를 normal flow 에 따라 배치
    - 자신의 원래 위치(static) 을 기준으로 이동
    - top, right, bottom, left 속성으로 위치를 조정
    - 다른 요소의 레이아웃에 영향을 주지 않음
- absolute - relative 부모 위치
    - 요소를 normal flow 에서 제거
    - 가장 가까운 relative 부모 요소를 기준으로 이동 ( 만족하는 부모 요소가 없으면 body 태그 기준)
    - top, right, bottom, left 속성으로 위치 조정
    - 문서에서 요소가 차지하는 공간이 없어짐
- fixed
    - 요소를 Normal Flow 에서 제거
    - 현재 화면영역을 기준으로 이동
    - 스크롤해도 항상 같은 위치에 유지
    - top, right, bottom, left 속성으로 위치를 조정
    - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
    - relative 와 fixed 의 특성을 결합한 속성 → relative 였다가 임계점을 만나면 fixed 로 바뀜
    - 스크롤 위치가 임계점에 도달하기 전에는 relative 처럼 동작
    - 스크롤 위치가 임계점에 도달하면 fixed 처럼 화면에 고정
    - 다음 sticky 요소가 나오면 이전 sticky 요소의 자리를 대체

### 2. z-index : 요소의 쌓임 순서를 정의 `z-index: 1`

- 정수 값을 사용해 Z 축 순서를 지정
- 값이 클수록 요소가 위에 쌓임
- static 이 아닌 요소에만 적용됨
- 기본값은 auto로 부모 요소의 z-index 값에 영향을 받음
- z-index 값이 같으면 HTML 문서에 적은 순서대로
- 부모의 z-index 가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음

## CSS Flexbox : 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식

`display : flex;` 

### 1. Flexbox 구성 요소

- main axis (주 축)
    - main start 에서 main end 방향으로 배치
- cross axis (교차 축)
    - cross start 에서 시작하여 cross end 방향으로 배치
- flex container
    - display: flex; 혹은 display: inline-flex; 가 설정된 부모 요소
    - 이 컨테이너의 1차 자식 요소들이 flex item이 됨
- flex item
    - flex ccontainer 내부 레이아웃 되는 항목

### 2. Flexbox 속성

- container 관련
    - display
    - flex - direction : flex item 이 나열되는 방향을 지정
    - flex - wrap : flex item 목록이 container 한 행에 들어가지 않을 경우, 다른 행에 배치할지 여부 결정
    - justify - content : 주 축을 따라 flex item 들을 정렬하고 간격을 조정
    - align - content : 컨테이너에 여러 줄의 flex item이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할지 지
    - align - items : 컨테이너 안에 있는 flex item 들의 교차 축 정렬 방법을 지정
- item 관련
    - align - self : 컨테이너 안에 있는 flex item 들을 교차 축을 따라 개별적으로 정렬
    - flex - grow
    - flex - basis
    - order
- 목적에 따른 속성 분류
    - 배치 (flex-direction, flex-wrap)
    - 공간 분배 (justify-content, align-content)
    - 정렬 (align-items, align-self)
- 속성 쉽게 이해하는 방법
    - justify - 주축
    - align - 교차 축
    - content - 여러 줄, items - 한 줄, self - 한 개
- flex - grow : 남는 행 여백을 비율에 따라 각 flex item에 분배
    
    → item 마다 각각 속성에다가 정수값으로 나눠가질 여백에 대한 비율 부여
    
- flex - basis : flex item의 초기 크기 값을 지정, width 값을 동시 적용하면 flex-basis가 우선

### 3. flex-wrap 응용

- 반응형 레이아웃 작성
    - 공간이 부족하면 여러 줄로 나누어지고, 여유 공간이 있으면 공간을 차지하며 늘어나도록 한다
    1. 컨테이너 display를 flex로 설정하고 flex-wrap에 wrap 속성 주기
    2. flex-basis 로 초기값을 주고, flex-grow로 여유 공간이 생길 때 여유공간을 분배하도록 설정
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        .card {
          width: 80%;
          border: 1px solid black;
          /* 1 */
          display: flex;
          /* 2 */
          flex-wrap: wrap;
        }
    
        img {
          width: 100%;
        }
    
        .thumbnail {
          /* 3 */
          flex-basis: 700px;
          /* 4 */
          flex-grow: 1;
        }
    
        .content {
          /* 3 */
          flex-basis: 350px;
          /* 4 */
          flex-grow: 1;
        }
      </style>
    </head>
    
    <body>
      <div class="card">
        <img class="thumbnail" src="images/sample.jpg" alt="sample">
        <div class="content">
          <h2>Heading</h2>
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis minus sed expedita ut nihil tempora
            neque autem odio eos, repudiandae blanditiis, molestiae consequatur. Adipisci illo dolor repellat alias
            maiores.
            Aut?</p>
        </div>
      </div>
    </body>
    
    </html>
    
    ```
    

## 참고

### 1. 마진 상쇄

- 두  block 타입 요소의 margin top 과 bottom 이 만나 더 큰 margin 으로 결합되는 현상
    
    20 + 40 = 40 됨
    
- 요소 간 간격을 일정하게 유지(일관성) 하고, 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만든다(단순성)

### 2. 박스 타입 별 수평 정렬

- Block 요소의 수평 정렬
    - `margin : auto` 사용
    - 블록의 너비를 지정하고 좌우 마진을 auto로 설정
    - 블록 요소에 직접 설정
- Inline 요소의 수평 정렬
    - `text-align` 사용
    - 부모 요소에 적용
- Inline-block 요소의 수평 정렬
    - `text-align` 사용
    - 부모 요소에 적용

### 3. 실제 Position 활용 예시

1. absolute - 특정 요소 위에 다른 요소를 겹쳐서 배치할 때 유용하게 사용 됨
2. fixed  - 페이지를 스크롤해도 항상 같은 자리에 표시되는 요소를 만들 때 사용
3. sticky - 일반적인 문서 흐름에 따라 배치되다가, 스크롤이 특정 위치에 도달하면 고정되는 속성

### 4. Flexbox Shorthand 속성

### 5. Flexbox 속성 정리

## 확인문제 및 활동정리


| 개념 | 설명 | 예시 |
| --- | --- | --- |
| display 속성 | 요소의 화면 배치 방식 정의 | .item{ display : block; } |
| position 속성 | 요소 위치를 특정 기준에 맞춰 배치 | .box{ position : absolute; } |
| z-index 속성 | 요소의 쌓이는 순서 정의 | .box{ z-index: 10; } |
| CSS Flexbox | 1차원 레이아웃 배치 및 정렬 방식 | .container{ display: flex; } |
| 주 축 방향 설정 | Flex 아이템이 나열될 방향 지정 | flex-direction : column; |
| 주 축 정렬 | 주 축의 아이템 정렬 및 간격 조정 | justify-content: center; |
| align-items | 교차 축의 아이템 한 줄 정렬 | align-items : center; |