from .parser import parse
from .engine import SimpleSQLEngine

def run_cli():
    db = SimpleSQLEngine()

    print("Simple SQL Engine")
    print("Type your SQL query or 'exit' to quit.\n")

    while True:
        query = input("sql> ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        try:
            command = parse(query)
            result = db.execute(command)
            print(result)
        except Exception as e:
            print("Error:", e)