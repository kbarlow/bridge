# Bridge DSL Compiler - Transpiles to SQL/Python
def compile_to_sql(ast: dict, config: dict) -> str:
    if ast["command"] != "show":
        raise NotImplementedError("Only SHOW command supported for now")

    metric = ast["metric"]
    group_by = ast.get("group_by")

    metric_sql = config["fields"].get(metric, metric)
    group_by_sql = config["fields"].get(group_by, group_by)

    table = config["tables"]["transactions"]

    query = f"SELECT {group_by_sql}, {metric_sql} AS {metric}\nFROM {table}"
    if group_by:
        query += f"\nGROUP BY {group_by_sql}"
    query += ";"
    return query
