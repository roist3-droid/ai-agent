from typing import Protocol

class Tool(Protocol):
    def run(self, text: str) -> str: ...

class IntakeTool:
    def run(self, text: str) -> str:
        return (
            f"[고객 응대 접수]\n문의: {text}\n"
            "답변 준비: 관련 제품·프로그램과 승인된 안내 자료 확인 필요"
        )

class ExplainTool:
    def run(self, text: str) -> str:
        return (
            f"[설명 요청]\n대상: {text}\n"
            "확인 필요: 공식 설명, 이용 방법, 가격, 주의사항\n"
            "승인된 자료가 없어 효능·가격을 생성하지 않았습니다."
        )

class OrganizeTool:
    def run(self, text: str) -> str:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "[영업자료 정리]\n" + "\n".join(
            f"{i}. {line}" for i, line in enumerate(lines, start=1)
        )
