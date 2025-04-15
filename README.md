# 유용한 터미널 코드

## 가상환경 관련   
* 가상환경 만들기 : `python -m venv [가상환경 이름]`
* 가상환경 실행 : (가상환경 있는 폴더 들어가서) `source [가상환경이름]/bin/activate`
* 가상환경에 설치한 패키지 확인 : `venv/lib` 에 들어가서 확인하기
* sudo 붙여서 가상환경 내 python 사용하기:  `sudo [가상환경경로]/bin/python3`
* 사용중인 python 경로 확인:  `which python`

## tmux
### tmux 구성 요소
```
session: 여러 윈도우로 구성
window: 터미널 화면, 세션 내에서 탭처럼 사용 가능
pane: 하나의 윈도우 내에서의 화면 분할
```

### session 관련 명령어
* 새로운 세션 생성: tmux new -s (session_name)
* 세션 만들면서 윈도우랑 같이 생성: tmux new -s (session_name) -n (window_name)
* 세션 종료 exit
* 세션 목록 tmux ls
* 세션 다시 시작하기(다시 불러오기) tmux attach -t session_number
* 세션 중단하기 `(ctrl + b)` `d`
* 스크롤하기 `ctrl + b` + `[`
* 특정 세션 강제 종료 tmux kill-session -t session_number

### 윈도우 관련 명령어
* 새 윈도우 생성 `(ctrl + b) c`
* 새 윈도우 이동 `(ctrl + b) b` `(숫자)`

### 틀 관련 명령어
* 틀 나누기
  * `(ctrl + b)` `%` #좌우로 나누기
  * `(ctrl + b)` `"` #위아래로 나누기
* 틀끼리 이동하기
  * `(ctrl + b)` `방향키`
* 틀 삭제
  * `(ctrl + d)`

### 단축키 목록 확인하기
`(ctrl + b)` `?`

## 디스크 저장공간 잔량 확인

`df` : 디스크의 남은 용량을 확인

`df -k` : 킬로바이트 단위로 현재 남은 용량을 확인

`df -m` : 메가바이트 단위로 남은 용량을 왁인

`df -h` : 보기 좋게 보여줌

`df .` : 현재 디렉토리가 포함된 파티션의 남은 용량을 확인

`du` : 현재 디렉토리에서 서브디렉토리까지의 사용량을 확인

`du -a` : 현재 디렉토리의 사용량을 파일단위 출력

`du -s` : 총 사용량을 확인

`du -h` : 보기 좋게 바꿔줌

`du -sh` : 한단계 서브디렉토리 기준으로 보여준다.


