import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from moshiment_agent.agent import Agent
from moshiment_agent.tools import OrganizeTool
from moshiment_agent.__main__ import main


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.agent = Agent({"organize": OrganizeTool()})

    def test_organize_preserves_lines(self):
        result = self.agent.run("organize", " 상담 안내\n\n제품 소개 ")
        self.assertEqual(
            result,
            "[영업자료 정리]\n1. 상담 안내\n2. 제품 소개",
        )

    def test_blank_input_is_rejected(self):
        with self.assertRaises(ValueError):
            self.agent.run("organize", " \n ")

    def test_unknown_task_is_rejected(self):
        with self.assertRaises(ValueError):
            self.agent.run("unknown", "문의")

    @patch.dict("os.environ", {"AGENT_MODE": "demo"})
    def test_cli_tasks(self):
        for task in ("respond", "explain", "organize"):
            with self.subTest(task=task):
                with redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(main([task, "제품 문의"]), 0)
                self.assertIn("제품 문의", output.getvalue())

    @patch.dict("os.environ", {"AGENT_MODE": "invalid"})
    def test_invalid_mode_is_rejected(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                main(["respond", "문의"])
        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
