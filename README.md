# hunmin
백성을 가르치는 바른 언어

### 1. `.hmn` 파일 실행법
상호작용(`interaction`)이 존재하는 실행환경에서 `.hmn` 파일을 실행하려면,
`interactiveConsole.py`를 실행하거나, 혹은 `release`의 `interactiveHunminConsole.exe`를 실행시키면 됩니다.

명령어 : `컴파일 <파일명.hmn>` 또는 `실행 <파일명.hmn>`

파일은 `.py` 파일로 컴파일 되며, `.py` 파일을 실행하는 방식으로 작동합니다.

### 2. `hunmin` 프로젝트 컴파일 하는 방법
`hunmin` 프로젝트라 함은,
```
src
└ ...

```
과 같은 구조를 갖는 폴더를 말합니다.

`hunmin` 컴파일러는 자동으로 `src` 폴더를 프로젝트의 소스파일 폴더로 인식하여 컴파일합니다.

상호작용이 존재하는 프로젝트 환경에서 `.hmn` 파일을 실행하려면,
`interactiveProjectManager.py`를 실행하거나, 혹은 `release`의 `interactiveHunminProjectManager.exe`를 실행시키면 됩니다. 

명령어 : `컴파일 <프로젝트명>`

그럼, `src`와 동일한 폴더상에 `build` 폴더에 모든 파일이 `.py`로 컴파일 된 상태로 추가됩니다.

단, 이때 파일 실행은 1과 같습니다.
