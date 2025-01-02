import unittest
from editor.parser import Parser, ParserError

class TestParser(unittest.TestCase):
    def test_valid_code(self):
        code = "x = 5\nprint(x)"
        parsed = Parser.parse(code)
        self.assertEqual(len(parsed), 2)

    def test_invalid_code(self):
        with self.assertRaises(ParserError):
            Parser.parse("unknown syntax")
