### Git

- ‘분산’ ‘버전관리’ 시스템
    - **버전관리**: 최종 버전과 변경 사항들을 관리 → 매번 파일 전체를 기록하는게 아니라 “변경 사항”을 저장
    - **분산**: 각자 컴퓨터에 전체 파일 전체를 가지고 있음    ↔ 중앙집중식 ex. 위키피디아, 나무위키
        - 중앙서버 의존 x
        - 백업 및 복구 용이
        - 인터넷에 연결되지 않아도 각자 작업할 수 있음
- git 의 3가지 영역
    1. working directory: 작업실 - 일하는데, 지금 작업중~~~
    2. staging area: 임시 저장공간 - 일단 했는데 최종 저장할지 몰라서 임시 저장
    3. repository: 실제 저장공간 - 최종 결정돼서 저장한 거 모음zip
- git 사용하기
    1. repository 로 사용할 폴더에서 VS code 열기
    2. terminal 열기
    
    [초기 설정 - 처음에 한 번만 하면 됨ㅇㅇ]
    
    1.  `git init` : repository 초기화
    2. `git config --global [user.email](http://user.email) “이메일”` : git 계정 등록
    3. `git config --global [user.name](http://user.name) "이름"` : git 사용자 이름 등록
    
    [사용 - 앞으로 계속 하는거]
    
    1. 파일 생성 후 `git add "파일명"` : 변경사항이 있는 파일을 staging area에 추가 (버전 관리 시작)
    2. `git comit -m "메시지"` : 커밋하기 (staging area에 있는 파일들을 저장소에 기록)
- 기타 git 명령어
    - `git status` : 현재 변경 사항 내역 + staging area 표시
    - `git log` : 현재까지 변경 내역들 확인
    - `git log --oneline` : commit 목록 한 줄로 보기
    - `git config --global -l` : git global 설정 정보 보기
- git 사용 시 주의사항 및 잘못했을 때
    - 프로젝트를 진행하는 폴더 내에 있는 폴더에서 git init하면 정상적으로 git 관리 불가!
    - 하나의 프로젝트가 하나의 폴더이고 그 폴더를 계속 열어서 작업해야 관리 가장 편함 ㅇㅇ
    - 파일 수정 후에 a → c → p 과정 전에는 항상 파일을 저장해야 함 ㅇㅇ
    - `git commit --amend` : 파일을 다 포함하지 못한 경우, 해당 파일을 add 한 후에 실행
       (창 종료 시에는 esc 누르고 `:wq` )    
    - `git commit --amend -m "수정된 메시지"` : commit 메시지 수정
    - `rm -rf .git/` : 잘못 git init한 경우 git 관리 삭제하는 명령어