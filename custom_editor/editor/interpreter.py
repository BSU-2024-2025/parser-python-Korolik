class Interpreter:
    """Интерпретатор для выполнения кода."""
    def __init__(self):
        self.variables = {}

    def execute(self, parsed_code):
        output = []
        for instruction in parsed_code:
            if instruction["type"] == "print":
                try:
                    output.append(str(eval(instruction["value"], {}, self.variables)))
                except Exception as e:
                    output.append(f"Error: {e}")
            elif instruction["type"] == "assignment":
                try:
                    self.variables[instruction["var"]] = eval(instruction["value"], {}, self.variables)
                except Exception as e:
                    output.append(f"Error: {e}")
            elif instruction["type"] == "condition":
                try:
                    condition = eval(instruction["value"], {}, self.variables)
                    output.append("Condition is True" if condition else "Condition is False")
                except Exception as e:
                    output.append(f"Error: {e}")
        return "\n".join(output)
