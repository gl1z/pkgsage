import sqlite3
from pathlib import Path
from platformdirs import user_data_dir

def get_db_path() -> Path:
    data_dir = Path(user_data_dir("pkgsage", "pkgsage"))
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "symbols.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db_path = get_db_path()
    if db_path.exists():
        return

    seed_path = Path(__file__).parent.parent / "data" / "seed.sql"
    sql = seed_path.read_text()

    conn = get_connection()
    conn.executescript(sql)
    conn.close()

def lookup(symbol: str, namespace: str | None = None) -> list[sqlite3.Row]:
    conn = get_connection()
    if namespace:
        rows = conn.execute(
            "SELECT * FROM symbols WHERE symbol = ? AND namespace = ? ORDER BY confidence DESC",
            (symbol, namespace)
        ).fetchall()
        if rows:
            conn.close()
            return rows
    rows = conn.execute(
        "SELECT * FROM symbols WHERE symbol = ? ORDER BY confidence DESC LIMIT 3",
        (symbol,)
    ).fetchall()
    conn.close()
    return rows
