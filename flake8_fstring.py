import ast

__version__ = "0.1.0"

ERRORS_FST001 = "FST001 formatted string used but nothing to format."


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.violations = []

    def visit_JoinedStr(self, node):
        if not node.values:
            self.violations.append(node)
        elif not [n for n in node.values if isinstance(n, ast.FormattedValue)]:
            self.violations.append(node)


class Linter(object):
    name = "flake8_fstring"
    version = __version__

    def __init__(self, tree, filename=None):
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        pass

    @classmethod
    def parse_options(cls, options):
        pass

    def run(self):
        visitor = Visitor()
        visitor.visit(self.tree)
        for v in visitor.violations:
            yield v.lineno, v.col_offset, ERRORS_FST001, type(self)
