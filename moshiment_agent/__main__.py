import argparse
import os
from .agent import Agent
from .tools import ExplainTool, IntakeTool, OrganizeTool

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="MOSHIMENT 업무 도우미 데모")
    parser.add_argument("task", choices=["respond", "explain", "organize"])
    parser.add_argument("text", help="문의 또는 정리할 원문")
    args = parser.parse_args(argv)

    if os.getenv("AGENT_MODE", "demo") != "demo":
        parser.error("현재 버전은 AGENT_MODE=demo만 지원합니다.")

    agent = Agent({
        "respond": IntakeTool(),
        "explain": ExplainTool(),
        "organize": OrganizeTool(),
    })
    try:
        print(agent.run(args.task, args.text))
    except ValueError as exc:
        parser.error(str(exc))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
