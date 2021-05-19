from ast import *

from pytest_ast_transformer.transformer import PytestTransformer


class PrintASTTransformer(PytestTransformer):
    context = {
        'random_object': object()
    }
    allow_inheritance_ctx = True


    def visit_Name(self, node):
        if node.id == "print" or node.id == "add":
            return fix_missing_locations(Call(
                func=Name(id='F', ctx=Load()),
                args=[Name(id=node.id, ctx=Load())],
                keywords=[]))
        return fix_missing_locations(node)
