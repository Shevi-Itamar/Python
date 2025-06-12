import ast


class CodeAnalysis:

    @staticmethod
    def number_of_lines(code: str):
        tree = ast.parse(code)
        line_numbers = [node.lineno for node in ast.walk(tree) if hasattr(node, 'lineno')]
        return max(line_numbers) if line_numbers else 0

    @staticmethod
    def get_functions_lengths(code: str) -> dict:
        tree = ast.parse(code)
        func_lengths = {}

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno
                end_line = max(
                    [n.lineno for n in ast.walk(node) if hasattr(n, 'lineno')],
                    default=start_line
                )
                func_lengths[node.name] = end_line - start_line + 1

        return func_lengths

    @staticmethod
    def get_unused_variables(code: str) -> list:
        tree = ast.parse(code)
        defined, used = set(), set()

        class Visitor(ast.NodeVisitor):
            def visit_Assign(self, node):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        defined.add(t.id)
                self.generic_visit(node)

            def visit_AnnAssign(self, node):
                if isinstance(node.target, ast.Name):
                    defined.add(node.target.id)
                self.generic_visit(node)

            def visit_For(self, node):
                if isinstance(node.target, ast.Name):
                    defined.add(node.target.id)
                self.generic_visit(node)

            def visit_arg(self, node):
                defined.add(node.arg)

            def visit_Name(self, node):
                if isinstance(node.ctx, ast.Load):
                    used.add(node.id)

        Visitor().visit(tree)
        return list(defined - used)

    @staticmethod
    def get_functions_without_docstrings(code: str) -> list:
        tree = ast.parse(code)
        functions_without_docstring = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if ast.get_docstring(node) is None:
                    functions_without_docstring.append(node.name)

        return functions_without_docstring
