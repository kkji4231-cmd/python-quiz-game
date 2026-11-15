# Python Quiz Game

Python 기본 문법, 클래스, JSON 파일 저장, Git/GitHub 사용법을 학습하기 위한 콘솔 기반 퀴즈 게임 프로젝트입니다.

---

## 1. 프로젝트 개요

이 프로젝트는 터미널에서 실행하는 Python 콘솔 퀴즈 게임입니다.

사용자는 메뉴를 통해 다음 기능을 사용할 수 있습니다.

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 확인
4. 최고 점수 확인
5. 프로그램 종료

`Quiz` 클래스와 `QuizGame` 클래스를 사용하여 개별 문제와 게임 전체 진행 기능을 분리했습니다.

퀴즈 데이터와 최고 점수는 프로젝트 루트의 `state.json` 파일에 JSON 형식으로 저장됩니다.

프로그램을 종료한 후 다시 실행해도 사용자가 추가한 퀴즈와 최고 점수가 유지됩니다.

---

## 2. 퀴즈 주제

### CNC · 공작기계 · 품질 기초

공작기계와 품질 업무에서 자주 접하는 기본 용어를 Python 학습과 연결하기 위해 이 주제를 선정했습니다.

기본 문제에는 다음과 같은 내용이 포함되어 있습니다.

- CNC
- MCT
- Spindle
- Backlash
- CMM
- Root Cause Analysis

기본적으로 5개의 퀴즈를 제공하며 사용자가 새로운 문제를 추가할 수 있습니다.

---

## 3. 개발 환경

| 구분 | 환경 |
|---|---|
| OS | Windows |
| Editor | Visual Studio Code |
| Terminal | PowerShell |
| Python | 3.14.10 |
| Version Control | Git |
| Remote Repository | GitHub |

외부 Python 라이브러리는 사용하지 않았습니다.

Python 표준 라이브러리인 `json` 모듈만 사용했습니다.

---

## 4. 실행 방법

프로젝트 폴더에서 다음 명령을 실행합니다.

```powershell
python main.py
```

프로그램이 정상적으로 실행되면 다음 메뉴가 출력됩니다.

```text
========================================
       CNC · 품질 퀴즈 게임
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택:
```

메뉴에서 원하는 기능의 번호를 입력하여 실행합니다.

---

## 5. 기능 목록

### 5.1 퀴즈 풀기

메뉴에서 `1`을 선택하면 저장되어 있는 문제를 순서대로 풀 수 있습니다.

각 문제는 4개의 선택지를 가지고 있으며 사용자는 `1~4` 중 하나를 입력합니다.

정답인 경우:

```text
✅ 정답입니다!
```

오답인 경우:

```text
❌ 오답입니다. 정답은 N번입니다.
```

모든 문제를 풀고 나면 정답 개수와 점수가 표시됩니다.

예:

```text
🏆 결과: 6문제 중 6문제 정답! (100점)
🎉 새로운 최고 점수입니다!
```

---

### 5.2 퀴즈 추가

메뉴에서 `2`를 선택하면 새로운 문제를 등록할 수 있습니다.

입력 항목:

```text
문제
선택지 1
선택지 2
선택지 3
선택지 4
정답 번호
```

실제 테스트 예:

```text
문제를 입력하세요: ATC의 의미는?
선택지 1: Automatic Tool Changer
선택지 2: Automatic Table Control
선택지 3: Axis Tool Controller
선택지 4: Auto Turning Center
정답 번호 (1-4): 1
```

정상적으로 추가되면:

```text
✅ 퀴즈가 추가되었습니다!
현재 등록된 퀴즈: 6개
```

가 출력됩니다.

추가한 문제는 `state.json`에 저장됩니다.

---

### 5.3 퀴즈 목록

메뉴에서 `3`을 선택하면 현재 저장된 모든 퀴즈의 문제를 확인할 수 있습니다.

예:

```text
📋 등록된 퀴즈 목록
총 6개의 퀴즈가 등록되어 있습니다.
----------------------------------------
[1] CNC의 의미는 무엇인가?
[2] MCT에서 주로 절삭공구를 회전시키는 장치는 무엇인가?
[3] 공작기계에서 백래시(Backlash)의 의미로 가장 적절한 것은?
[4] 가공품의 치수와 형상을 정밀하게 측정하는 장비는?
[5] 품질관리에서 불량의 근본 원인을 찾는 활동과 가장 관련 있는 것은?
[6] ATC의 의미는?
----------------------------------------
```

---

### 5.4 최고 점수 확인

메뉴에서 `4`를 선택하면 지금까지 기록한 최고 점수를 확인할 수 있습니다.

퀴즈를 아직 풀지 않았다면:

```text
🏆 최고 점수 확인
아직 퀴즈를 플레이하지 않았습니다.
```

최고 점수가 존재하면:

```text
🏆 최고 점수 확인
현재 최고 점수: 100점
```

으로 표시됩니다.

새로운 최고 점수를 획득하면 자동으로 갱신하여 `state.json`에 저장합니다.

---

### 5.5 종료

메뉴에서 `5`를 선택하면 현재 데이터를 저장하고 프로그램을 종료합니다.

```text
퀴즈 게임을 종료합니다.
```

---

## 6. 입력 및 예외 처리

### 메뉴 입력

숫자가 아닌 값을 입력하는 경우:

```text
선택: abc
⚠️ 숫자만 입력하세요.
```

범위를 벗어난 숫자를 입력하는 경우:

```text
선택: 9
⚠️ 1~5 사이의 숫자를 입력하세요.
```

빈 값을 입력하는 경우:

```text
선택:
⚠️ 입력값이 없습니다. 1~5 사이의 숫자를 입력하세요.
```

---

### 정답 입력

정답 입력은 `1~4` 범위만 허용합니다.

다음 입력들을 예외 처리합니다.

- 빈 입력
- 문자를 입력한 경우
- 1~4 범위를 벗어난 숫자

---

### Ctrl+C

프로그램 실행 중 `Ctrl+C`가 입력되더라도 Traceback으로 비정상 종료하지 않도록 처리했습니다.

```text
⚠️ Ctrl+C가 입력되었습니다.
데이터를 저장하고 안전하게 종료합니다.
```

종료 전에 현재 상태를 `state.json`에 저장합니다.

---

### EOFError

입력 스트림이 종료되는 상황에서도 예외를 처리합니다.

```text
⚠️ 입력 스트림이 종료되었습니다.
데이터를 저장하고 안전하게 종료합니다.
```

---

### state.json 오류

`state.json`이 없는 첫 실행에서는 기본 퀴즈 데이터로 새로운 파일을 생성합니다.

JSON 파일이 손상되어 정상적으로 읽을 수 없는 경우에는 `try/except`로 오류를 처리하고 기본 퀴즈 데이터로 복구합니다.

---

## 7. 파일 구조

```text
python-quiz-game/
├── .gitignore
├── README.md
├── main.py
├── quiz.py
├── quiz_data.py
├── quiz_game.py
└── state.json
```

### 파일별 역할

| 파일 | 역할 |
|---|---|
| `.gitignore` | Python 캐시, VS Code 설정 등 Git 제외 항목 관리 |
| `README.md` | 프로젝트 설명 및 실행 방법 문서 |
| `main.py` | 프로그램 시작 및 Ctrl+C/EOF 안전 종료 |
| `quiz.py` | 개별 퀴즈를 담당하는 `Quiz` 클래스 |
| `quiz_data.py` | 기본 퀴즈 데이터 생성 |
| `quiz_game.py` | 메뉴, 플레이, 추가, 목록, 점수, JSON 저장/불러오기 관리 |
| `state.json` | 저장된 퀴즈 목록과 최고 점수 데이터 |

---

## 8. 클래스 구조

### Quiz 클래스

개별 퀴즈 한 문제를 표현합니다.

주요 속성:

```text
question
choices
answer
```

주요 메서드:

```text
display()
check_answer()
to_dict()
from_dict()
```

`to_dict()`는 Quiz 객체를 JSON으로 저장 가능한 `dict` 형태로 변경합니다.

`from_dict()`는 저장된 JSON 데이터를 다시 Quiz 객체로 변환합니다.

---

### QuizGame 클래스

퀴즈 게임 전체를 관리합니다.

주요 속성:

```text
quizzes
best_score
state_file
```

주요 기능:

```text
메뉴 표시
메뉴 입력 처리
정답 입력 처리
퀴즈 플레이
퀴즈 추가
퀴즈 목록
최고 점수 확인
JSON 저장
JSON 불러오기
```

---

## 9. state.json

`state.json`은 프로젝트 루트에 위치합니다.

파일 인코딩은 UTF-8을 사용합니다.

퀴즈와 최고 점수를 프로그램 종료 후에도 유지하기 위한 데이터 파일입니다.

### 데이터 구조

```json
{
    "quizzes": [
        {
            "question": "CNC의 의미는 무엇인가?",
            "choices": [
                "Computer Numerical Control",
                "Central Network Controller",
                "Computer Network Code",
                "Control Number Computer"
            ],
            "answer": 1
        }
    ],
    "best_score": 100
}
```

### 필드 설명

| 필드 | 설명 |
|---|---|
| `quizzes` | 저장된 퀴즈 목록 |
| `question` | 퀴즈 문제 |
| `choices` | 4개의 선택지 |
| `answer` | 정답 번호 |
| `best_score` | 최고 점수 |

---

## 10. 데이터 영속성 검증

기본 5개의 문제에서 새로운 퀴즈를 추가했습니다.

```text
ATC의 의미는?

1. Automatic Tool Changer
2. Automatic Table Control
3. Axis Tool Controller
4. Auto Turning Center

정답: 1
```

추가 결과:

```text
✅ 퀴즈가 추가되었습니다!
현재 등록된 퀴즈: 6개
```

프로그램을 종료한 후 다시 실행했습니다.

```powershell
python main.py
```

재실행 결과:

```text
📂 저장된 데이터를 불러왔습니다. (퀴즈 6개)
```

퀴즈 목록에서도 다음 문제를 확인했습니다.

```text
[6] ATC의 의미는?
```

따라서 사용자가 추가한 퀴즈가 프로그램 종료 후에도 유지되는 것을 확인했습니다.

---

### 최고 점수 영속성

6개의 문제를 모두 맞혀 100점을 기록했습니다.

```text
🏆 결과: 6문제 중 6문제 정답! (100점)
🎉 새로운 최고 점수입니다!
```

프로그램을 완전히 종료하고 다시 실행한 후 메뉴 `4`를 선택했습니다.

```text
🏆 최고 점수 확인
현재 최고 점수: 100점
```

따라서 최고 점수 역시 프로그램 재실행 후 유지되는 것을 확인했습니다.

---

## 11. Git 기본 작업

프로젝트에서 다음 명령들을 사용했습니다.

```text
git init
git add
git commit
git push
git checkout
git merge
```

기능 단위로 변경한 후 의미 있는 커밋을 생성했습니다.

주요 커밋 예:

```text
Init: 프로젝트 기본 구조 생성
Feat: Quiz 클래스 구현
Feat: 기본 퀴즈 데이터 추가
Feat: 메뉴 및 입력 검증 기능 구현
Feat: 퀴즈 플레이 기능 구현
Feat: 퀴즈 추가 기능 구현
Feat: 퀴즈 목록 기능 구현
Feat: 최고 점수 확인 및 갱신 기능 구현
Feat: Quiz JSON 변환 기능 구현
Feat: JSON 데이터 저장 및 불러오기 구현
Fix: Ctrl+C 및 EOF 안전 종료 처리
```

---

## 12. Git 브랜치 및 병합

퀴즈 플레이 기능은 별도의 Feature Branch에서 구현했습니다.

### 브랜치 생성 및 이동

```powershell
git checkout -b feature/quiz-play
```

확인:

```powershell
git branch
```

결과:

```text
* feature/quiz-play
  main
```

Feature Branch에서 퀴즈 플레이 기능을 구현한 후 커밋했습니다.

```powershell
git add quiz_game.py
git commit -m "Feat: 퀴즈 플레이 기능 구현"
```

Feature Branch를 GitHub에 Push했습니다.

```powershell
git push -u origin feature/quiz-play
```

다시 `main` 브랜치로 이동했습니다.

```powershell
git checkout main
```

퀴즈 플레이 브랜치를 `main`으로 병합했습니다.

```powershell
git merge feature/quiz-play
```

병합 결과:

```text
Fast-forward
quiz_game.py | 54 +++++++++++++++++++++++++++++++++++++++++++++++++++++-
```

병합 후 `main` 브랜치를 GitHub에 Push했습니다.

```powershell
git push
```

이를 통해 별도의 Feature Branch에서 기능을 개발한 뒤 `main`으로 병합하는 Git Workflow를 실습했습니다.

---

## 13. Python 학습 내용

이번 프로젝트를 통해 다음 Python 기초 내용을 실습했습니다.

### 자료형

- `int`
- `str`
- `bool`
- `list`
- `dict`

### 제어문

- `if`
- `elif`
- `else`
- `for`
- `while`

### 함수

- 함수 정의
- 매개변수
- 반환값
- `return`

### 클래스

- 클래스와 객체
- `__init__`
- `self`
- 속성
- 메서드
- `classmethod`

### 파일 처리

- 파일 읽기
- 파일 쓰기
- UTF-8
- JSON
- `json.load()`
- `json.dump()`

### 예외 처리

- `try`
- `except`
- `ValueError`
- `FileNotFoundError`
- `JSONDecodeError`
- `OSError`
- `KeyboardInterrupt`
- `EOFError`

---

## 14. Git 학습 내용

이번 프로젝트에서 사용한 주요 Git 명령:

```text
git init
git status
git add
git commit
git push
git checkout
git branch
git merge
```

프로젝트 완료 후 아래 명령도 실습하여 Git 기초 명령어 요구사항을 충족합니다.

```text
git clone
git pull
```

---

## 15. Git 저장소 복제 실습

이 항목은 프로젝트 개발 완료 후 Git의 `clone`과 `pull` 동작을 검증하기 위한 실습입니다.

진행 순서:

```text
GitHub Repository
       ↓
git clone
       ↓
별도 로컬 폴더
       ↓
README 간단 수정
       ↓
commit
       ↓
push
       ↓
기존 프로젝트
       ↓
git pull
       ↓
변경사항 반영 확인
```

실습 완료 후 실제 명령과 결과를 이 항목에 추가합니다.

---

## 16. 실행 결과 증거

최종 제출 전 다음 실행 결과를 캡처하여 저장소에 추가합니다.

- 개발 환경 및 Python 버전
- VS Code 프로젝트 화면
- 메인 메뉴
- 퀴즈 플레이
- 퀴즈 추가
- 퀴즈 목록
- 최고 점수
- 프로그램 재실행 후 데이터 유지
- `git log --oneline --graph`

---

## 17. 실행 요약

실행 명령:

```powershell
python main.py
```

게임 흐름:

```text
프로그램 시작
    ↓
state.json 불러오기
    ↓
메인 메뉴
    ├─ 1. 퀴즈 풀기
    ├─ 2. 퀴즈 추가
    ├─ 3. 퀴즈 목록
    ├─ 4. 점수 확인
    └─ 5. 종료
            ↓
        state.json 저장
            ↓
           종료
```

이 프로젝트를 통해 Python 기초 문법에서부터 객체지향 구조, JSON 데이터 영속성, 예외 처리, Git 버전 관리 및 Feature Branch 병합까지 직접 구현하고 검증했습니다.