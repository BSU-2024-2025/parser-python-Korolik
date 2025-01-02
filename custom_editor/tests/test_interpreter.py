import unittest
from editor.parser import Parser
from editor.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_execution(self):
        code = "x = 5\nprint(x)"
        parsed = Parser.parse(code)
        interpreter = Interpreter()
        result = interpreter.execute(parsed)
        self.assertEqual(result, "5")
