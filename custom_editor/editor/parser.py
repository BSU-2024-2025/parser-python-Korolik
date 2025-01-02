class ParserError(Exception):
    """Класс для ошибок парсера."""
    pass

class Parser:
    """Простой парсер для языка."""
    @staticmethod
    def parse(code):
        lines = code.splitlines()
        parsed = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("print"):
                parsed.append({"type": "print", "value": line[6:-1].strip()})
            elif "=" in line:
                var, expr = line.split("=", 1)
                parsed.append({"type": "assignment", "var": var.strip(), "value": expr.strip()})
            elif line.startswith("if") and line.endswith(":"):
                parsed.append({"type": "condition", "value": line[3:-1].strip()})
            else:
                raise ParserError(f"Unknown syntax: {line}")
        return parsed
