from bridge_dsl.parser import parse_dsl
from bridge_dsl.compiler import compile_to_sql
from bridge_dsl.config import load_config

with open("examples/customer_churn.bridge") as f:
    dsl = f.read()

ast = parse_dsl(dsl)
config = load_config()

sql = compile_to_sql(ast, config)
print(sql)

