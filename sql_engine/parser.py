def parse(query):
    q = query.strip().rstrip(";")
    q_lower = q.lower()

    # ------------------ CREATE TABLE ------------------
    if q_lower.startswith("create table"):
        table = q.split()[2]
        cols_part = q[q.index("(") + 1 : q.index(")")]
        cols = [c.strip() for c in cols_part.split(",")]
        return {
            "action": "create",
            "table": table,
            "columns": cols
        }

    # ------------------ INSERT ------------------
    if q_lower.startswith("insert into"):
        parts = q.split()
        table = parts[2]
        assignments = {}

        for segment in parts[3:]:
            if "=" in segment:
                key, value = segment.split("=")
                assignments[key.strip()] = value.strip()

        return {
            "action": "insert",
            "table": table,
            "values": assignments
        }

    # ------------------ SELECT ------------------
    if q_lower.startswith("select"):
        select_part = q_lower.split("from")[0].replace("select", "").strip()
        columns = [c.strip() for c in select_part.split(",")]

        table = q_lower.split("from")[1].split()[0]

        # WHERE
        where = None
        if "where" in q_lower:
            where_part = q_lower.split("where")[1].split("order by")[0] if "order by" in q_lower else q_lower.split("where")[1]
            where_part = where_part.strip()
            where_col, where_val = where_part.split("=")
            where = (where_col.strip(), where_val.strip())

        # ORDER BY
        order_by = None
        if "order by" in q_lower:
            order_by = q_lower.split("order by")[1].strip()

        return {
            "action": "select",
            "table": table,
            "columns": columns,
            "where": where,
            "order_by": order_by
        }

    # ------------------ UPDATE ------------------
    if q_lower.startswith("update"):
        parts = q.split()
        table = parts[1]

        set_part = q_lower.split("set")[1].split("where")[0].strip()
        key, val = set_part.split("=")
        updates = {key.strip(): val.strip()}

        where_part = q_lower.split("where")[1].strip()
        where_col, where_val = where_part.split("=")
        where = (where_col.strip(), where_val.strip())

        return {
            "action": "update",
            "table": table,
            "updates": updates,
            "where": where
        }

    # ------------------ DELETE ------------------
    if q_lower.startswith("delete"):
        table = q_lower.split("from")[1].split("where")[0].strip()

        where_part = q_lower.split("where")[1].strip()
        where_col, where_val = where_part.split("=")

        return {
            "action": "delete",
            "table": table,
            "where": (where_col.strip(), where_val.strip())
        }

    raise ValueError("Unknown command")