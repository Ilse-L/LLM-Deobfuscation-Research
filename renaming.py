import ast
from pathlib import Path

def rename_top_function_to_task_id(source_code: str, task_id_num: int) -> str:
    tree = ast.parse(source_code)

    class FuncRenamer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            # rename only the first top-level function
            node.name = f"task_id_{task_id_num}"
            return node

    # apply renaming
    renamer = FuncRenamer()
    new_tree = renamer.visit(tree)
    ast.fix_missing_locations(new_tree)

    # Convert AST back to source code
    if hasattr(ast, "unparse"):
        return ast.unparse(new_tree)
    else:
        import astor
        return astor.to_source(new_tree)
