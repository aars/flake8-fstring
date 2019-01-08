import ast
import flake8_self


def test_all():
    source_code = """amount = "one"
empty = f""
wrong = f"this does not contain any interpolation"
right = f"but this {amount} does"
"""
    tree = ast.parse(source_code)
    violations = list(flake8_self.Linter(tree).run())

    assert len(violations) == 2
    assert violations[0][0] == 2  # line_no 2
    assert violations[0][1] == 8  # col_offset 8
    assert violations[0][2] == flake8_self.ERRORS_FST001
    assert violations[1][0] == 3  # line_no 3
    assert violations[1][1] == 8  # col_offset 8
    assert violations[1][2] == flake8_self.ERRORS_FST001
