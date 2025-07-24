from lark import Lark, Transformer, v_args
from lark.tree import Tree

bridge_grammar = r"""
    start: show_stmt

    show_stmt: "SHOW" metric ("BY" field)?

    metric: CNAME
    field: CNAME

    %import common.CNAME
    %import common.WS
    %ignore WS
"""

parser = Lark(bridge_grammar, parser="lalr")

@v_args(inline=True)
class BridgeTransformer(Transformer):
    def metric(self, token):
        return str(token)

    def field(self, token):
        return str(token)

    def show_stmt(self, metric, group_by=None):
        return {
            "command": "show",
            "metric": metric,
            "group_by": group_by
        }

class FullTransformer(BridgeTransformer):
    def start(self, children):
        return children[0]

def parse_dsl(dsl_text: str) -> dict:
    tree = parser.parse(dsl_text)
    return FullTransformer().transform(tree)
