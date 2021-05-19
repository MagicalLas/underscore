from pytest_ast_transformer.ast_manager import ASTManager

from underscore.ast_transformer import PrintASTTransformer


def pytest_register_ast_transformer(ast_manager: ASTManager):
    ast_manager.add_transformer(PrintASTTransformer())
