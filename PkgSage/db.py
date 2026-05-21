import sqlite3
import time
from pathlib import Path
from platformdirs import user_data_dir

def get_db_path():
    data_dir = Path(user_data_dir("pkgsage", "pkgsage"))
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "symbols.db"

def get_connection():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS nuget_cache (
            package TEXT PRIMARY KEY,
            found INTEGER NOT NULL,
            latest_version TEXT,
            checked_at INTEGER NOT NULL
        )
    """)
    conn.commit()

    symbols_exist = conn.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='symbols'"
    ).fetchone()[0]

    if not symbols_exist:
        seed_path = Path(__file__).parent.parent / "data" / "seed.sql"
        sql = seed_path.read_text()
        conn.executescript(sql)

    conn.close()

def lookup(symbol, namespace=None):
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

def get_cached_nuget(package):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM nuget_cache WHERE package = ?", (package.lower(),)
    ).fetchone()
    conn.close()
    if row and (time.time() - row["checked_at"]) < 86400:
        return dict(row)
    return None

def set_cached_nuget(package, found, latest_version=None):
    conn = get_connection()
    conn.execute(
        "INSERT OR REPLACE INTO nuget_cache (package, found, latest_version, checked_at) VALUES (?, ?, ?, ?)",
        (package.lower(), int(found), latest_version, int(time.time()))
    )
    conn.commit()
    conn.close()