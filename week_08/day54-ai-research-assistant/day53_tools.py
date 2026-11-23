
# DAY 53 - AI Agent Research Tools
# Tools: Calculator, Database Search, Document Search

import sqlite3
from pathlib import Path
import logging
import operator


# ----------------------------------
# 1. CONFIGURATION
# ----------------------------------

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "company.db"
DOCS_PATH = BASE_DIR / "documents"

MAX_RESULTS = 10
MAX_QUERY_LENGTH = 200

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# ----------------------------------
# 2. DATABASE INITIALIZATION
# ----------------------------------

def initialize_database():

    try:
        with sqlite3.connect(DB_PATH) as conn:

            conn.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    city TEXT NOT NULL
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    product TEXT NOT NULL,
                    amount REAL NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY(customer_id)
                    REFERENCES customers(id)
                )
            """)

            customer_count = conn.execute(
                "SELECT COUNT(*) FROM customers"
            ).fetchone()[0]

            if customer_count == 0:

                conn.executemany(
                    """
                    INSERT INTO customers
                    (name, email, city)
                    VALUES (?, ?, ?)
                    """,
                    [
                        ("Ramesh", "ramesh@example.com", "Bengaluru"),
                        ("Arun", "arun@example.com", "Chennai"),
                        ("Priya", "priya@example.com", "Mumbai")
                    ]
                )

                conn.executemany(
                    """
                    INSERT INTO orders
                    (customer_id, product, amount, status)
                    VALUES (?, ?, ?, ?)
                    """,
                    [
                        (1, "Laptop", 75000, "Completed"),
                        (1, "Keyboard", 2000, "Completed"),
                        (2, "Monitor", 15000, "Pending"),
                        (3, "Laptop", 80000, "Completed")
                    ]
                )

            conn.commit()

        logging.info("Database initialized.")

    except sqlite3.Error as error:
        logging.error("Database initialization failed: %s", error)
        raise


# ----------------------------------
# 3. TOOL 1 - CALCULATOR
# ----------------------------------

def calculator(operation, numbers):

    operations = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv
    }

    if operation not in operations:
        return {
            "success": False,
            "error": "Unsupported mathematical operation."
        }

    if len(numbers) != 2:
        return {
            "success": False,
            "error": "Exactly two numbers are required."
        }

    if not all(
        isinstance(n, (int, float)) and not isinstance(n, bool)
        for n in numbers
    ):
        return {
            "success": False,
            "error": "Inputs must be numbers."
        }

    if operation == "divide" and numbers[1] == 0:
        return {
            "success": False,
            "error": "Division by zero is not allowed."
        }

    try:

        result = operations[operation](*numbers)

        return {
            "success": True,
            "result": result
        }

    except (ArithmeticError, TypeError) as error:

        return {
            "success": False,
            "error": str(error)
        }


# ----------------------------------
# 4. TOOL 2 - DATABASE SEARCH
# ----------------------------------

def database_search(keyword):

    if not isinstance(keyword, str) or not keyword.strip():
        return {
            "success": False,
            "error": "A non-empty search keyword is required."
        }

    if len(keyword) > MAX_QUERY_LENGTH:
        return {
            "success": False,
            "error": "Search keyword is too long."
        }

    try:

        with sqlite3.connect(DB_PATH, timeout=5) as conn:

            conn.row_factory = sqlite3.Row

            query = """
                SELECT
                    customers.name,
                    customers.email,
                    customers.city,
                    orders.product,
                    orders.amount,
                    orders.status
                FROM customers
                LEFT JOIN orders
                ON customers.id = orders.customer_id
                WHERE customers.name LIKE ?
                LIMIT ?
            """

            rows = conn.execute(
                query,
                (f"%{keyword.strip()}%", MAX_RESULTS)
            ).fetchall()

            return {
                "success": True,
                "count": len(rows),
                "results": [dict(row) for row in rows]
            }

    except sqlite3.Error as error:

        logging.error("Database search failed: %s", error)

        return {
            "success": False,
            "error": "Database search failed."
        }


# ----------------------------------
# 5. TOOL 3 - DOCUMENT SEARCH
# ----------------------------------

def document_search(keyword):

    if not isinstance(keyword, str) or not keyword.strip():
        return {
            "success": False,
            "error": "A non-empty search keyword is required."
        }

    if len(keyword) > MAX_QUERY_LENGTH:
        return {
            "success": False,
            "error": "Search keyword is too long."
        }

    try:

        if not DOCS_PATH.is_dir():
            return {
                "success": False,
                "error": "Documents directory not found."
            }

        results = []

        search_terms = keyword.lower().split()

        for file_path in DOCS_PATH.glob("*.txt"):

            if file_path.is_symlink():
                continue

            if file_path.stat().st_size > 1_000_000:
                continue

            content = file_path.read_text(
                encoding="utf-8"
            )

            for line_number, line in enumerate(
                content.splitlines(), start=1
            ):

                if all(
                    term in line.lower()
                    for term in search_terms
                ):

                    results.append({
                        "file": file_path.name,
                        "line": line_number,
                        "content": line.strip()
                    })

                    if len(results) >= MAX_RESULTS:
                        break

            if len(results) >= MAX_RESULTS:
                break

        return {
            "success": True,
            "count": len(results),
            "results": results
        }

    except (OSError, UnicodeError) as error:

        logging.error("Document search failed: %s", error)

        return {
            "success": False,
            "error": "Document search failed."
        }


# ----------------------------------
# 6. TOOL REGISTRY
# ----------------------------------

TOOLS = {
    "calculator": calculator,
    "database_search": database_search,
    "document_search": document_search
}


# ----------------------------------
# 7. EXECUTION CONTROL
# ----------------------------------

def execute_tool(tool_name, **arguments):

    if tool_name not in TOOLS:

        return {
            "success": False,
            "error": "Unknown tool."
        }

    try:

        logging.info("Executing tool: %s", tool_name)

        return TOOLS[tool_name](**arguments)

    except Exception:

        logging.exception("Unexpected tool failure.")

        return {
            "success": False,
            "error": "Unexpected tool execution failure."
        }


# ----------------------------------
# 8. TESTING
# ----------------------------------

def run_tests():

    initialize_database()

    print("\n--- TOOL 1: CALCULATOR ---")

    print(
        execute_tool(
            "calculator",
            operation="add",
            numbers=[10, 20]
        )
    )

    print("\n--- TOOL 2: DATABASE SEARCH ---")

    print(
        execute_tool(
            "database_search",
            keyword="Ramesh"
        )
    )

    print("\n--- TOOL 3: DOCUMENT SEARCH ---")

    print(
        execute_tool(
            "document_search",
            keyword="AI agents"
        )
    )

    print("\n--- ERROR TESTS ---")

    print(
        execute_tool(
            "calculator",
            operation="divide",
            numbers=[10, 0]
        )
    )

    print(
        execute_tool(
            "database_search",
            keyword=""
        )
    )

    print(
        execute_tool(
            "unknown_tool"
        )
    )


if __name__ == "__main__":

    run_tests()
