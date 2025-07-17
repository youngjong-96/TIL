### GitHub

add → commit → push의 사이클….

- Github 초기 설정하기
    1. github에서 새로운 repository 만들고 해당 주소를 복사
    2. 터미널에서 `git remote add origin "repository주소"`
        
        (origin(이름인데 보통 origin사용)이라는 원격 저장소 추가)
        
- 내 컴퓨터에 있는 파일들 Github에 올리기 (push)
    - 터미널에서 `git push origin master` (origin이라는 공간에 master 브랜치 업로드)
        
        → 지금까지 commit한 내용이 업로드
        
- Github에 있는 파일들 내 컴퓨터로 가져오기 (pull or clone)
    1. `git clone "github repository 주소"` : github repository 복사
        
        ![image.png](image%201.png)
        
    2. `git pull origin master` : origin에 master 브랜치에 있는 파일들 가져오기
- gitignore : Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
    
    ![image.png](image%202.png)
    
    - gitignore.txt 파일 안에 추적하지 않을 파일명을 추가하면 됨.
    - but. 이미 추적중인 파일은 이후에 추가해도 무시되지 않음.
        
        → `git rm --cached` 명령어로 git 캐시에서 삭제 필요
        
    - gitignore 파일도 프로젝트의 일부임으로 수정 사항이 있으면 push 해야 함.
    - 참고. [https://www.toptal.com/developers/gitignore/](https://www.toptal.com/developers/gitignore/)
    - 프로젝트 진행 시 gitignore 먼저 만들고 시작!