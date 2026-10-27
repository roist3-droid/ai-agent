from .tools import Tool

class Agent:
    def __init__(self, tools: dict[str, Tool]):
        self.tools = dict(tools)

    def run(self, task: str, text: str) -> str:
        if not text.strip():
            raise ValueError("내용을 입력해 주세요.")
        if task not in self.tools:
            raise ValueError(f"지원하지 않는 작업: {task}")
        return self.tools[task].run(text.strip())
