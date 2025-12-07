class SimpleSQLEngine:
    def __init__(self):
        self.tables = {}

    # ---------------- CREATE ----------------
    def create_table(self, table, columns):
        self.tables[table] = {
            "columns": columns,
            "rows": []
        }
        return f"Table '{table}' created with columns {columns}."

    # ---------------- INSERT ----------------
    def insert_row(self, table, values):
        if table not in self.tables:
            raise KeyError(table)

        row = {}
        for col in self.tables[table]["columns"]:
            row[col] = values.get(col, None)

        self.tables[table]["rows"].append(row)
        return "Row inserted."

    # ---------------- SELECT ----------------
    def select(self, table, columns, where, order_by):
        if table not in self.tables:
            raise KeyError(table)

        rows = self.tables[table]["rows"]

        # WHERE
        if where:
            col, val = where
            rows = [r for r in rows if str(r.get(col)) == str(val)]

        # ORDER BY
        if order_by:
            rows = sorted(rows, key=lambda r: str(r.get(order_by)))

        # Column selection
        if columns != ["*"]:
            rows = [{c: row[c] for c in columns} for row in rows]

        return rows

    # ---------------- UPDATE ----------------
    def update(self, table, updates, where):
        if table not in self.tables:
            raise KeyError(table)

        col, val = where
        count = 0

        for row in self.tables[table]["rows"]:
            if str(row.get(col)) == str(val):
                for key, value in updates.items():
                    row[key] = value
                count += 1

        return f"Rows updated."

    # ---------------- DELETE ----------------
    def delete(self, table, where):
        if table not in self.tables:
            raise KeyError(table)

        col, val = where
        before = len(self.tables[table]["rows"])
        self.tables[table]["rows"] = [r for r in self.tables[table]["rows"] if str(r.get(col)) != str(val)]
        after = len(self.tables[table]["rows"])

        return "Rows deleted."

    # Main executor
    def execute(self, command):
        action = command["action"]

        if action == "create":
            return self.create_table(command["table"], command["columns"])

        if action == "insert":
            return self.insert_row(command["table"], command["values"])

        if action == "select":
            return self.select(
                command["table"],
                command["columns"],
                command["where"],
                command["order_by"]
            )

        if action == "update":
            return self.update(command["table"], command["updates"], command["where"])

        if action == "delete":
            return self.delete(command["table"], command["where"])

        raise ValueError("Unknown action")