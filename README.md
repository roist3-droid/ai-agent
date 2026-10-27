# MOSHIMENT 업무 지원 에이전트

모쉬먼트 프랜차이즈·온라인 사업 업무를 지원하는
단일 에이전트 프로젝트입니다.

## 현재 구현

API 키 없이 실행하는 로컬 CLI 데모입니다.

- respond: 고객 문의를 접수 형식으로 정리
- explain: 제품·프로그램 설명에 필요한 확인 항목 출력
- organize: 입력한 영업자료를 줄 단위 번호 목록으로 정리

현재 AI 답변 생성, 의미 기반 요약, 공식 제품정보 검색,
메시지 발송, 예약 실행, 외부 서비스 연결은 구현하지 않았습니다.
승인된 자료 없이 가격·효능·계약 조건을 만들어내지 않습니다.

## 실행 환경

- Python 3.11 이상
- 외부 패키지 설치 불필요
- 모든 명령은 저장소 최상위 디렉터리에서 실행

## 로컬 실행

```sh
python -m moshiment_agent respond "가맹 상담을 받고 싶습니다."
python -m moshiment_agent explain "피부장벽 관리 프로그램"
python -m moshiment_agent organize "원장님 대상 세미나 안내"
```

여러 줄을 입력하면 organize가 각 줄에 번호를 붙입니다.
빈 입력과 지원하지 않는 작업은 오류로 처리합니다.

Windows에서 python 명령을 사용할 수 없다면 py -3으로 대체하세요.

## 환경설정

AGENT_MODE의 기본값은 demo입니다.
현재는 demo만 지원하며 API 키가 필요하지 않습니다.

.env.example은 설정 참고용입니다.
.env 파일을 자동으로 읽지는 않습니다.

macOS/Linux:

```sh
export AGENT_MODE=demo
```

Windows PowerShell:

```powershell
$env:AGENT_MODE = "demo"
```

## 테스트

```sh
python -m unittest discover -s tests -v
```

## 구조

- moshiment_agent/__main__.py: CLI와 도구 구성
- moshiment_agent/agent.py: 입력 검증과 실행 조정
- moshiment_agent/tools.py: 도구 인터페이스와 기본 구현
- tests/test_agent.py: 코어 및 CLI 테스트

새 도구는 run(text: str) -> str 인터페이스를 구현하고
진입점의 도구 목록과 CLI 선택지에 등록합니다.

## 다음 커밋 단위

1. 실행 가능한 CLI·도구·테스트·문서 추가
2. 공개 가능한 승인 자료와 출처 기반 조회 도구 추가
3. 단일 LLM 연결과 응답 품질·실패 처리 테스트 추가
4. 한 가지 반복 업무를 선정해 수동 실행 방식으로 연결

외부 발송이나 데이터 변경은 별도의 검토 단계를 둡니다.

## 데이터 관리

이 저장소는 공개 저장소입니다.
API 키, 고객 개인정보, 내부 영업자료는 커밋하지 않습니다.
실제 업무 자료와 모델 설정은 후속 단계에서 관리 방식을 정합니다.
