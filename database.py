"""Persistence layer: SQLite storage and retrieval for BMI history."""
import sqlite3
from datetime import datetime

import pandas as pd


def create_connection(db_path: str = "bmi_data.db") -> sqlite3.Connection:
    """Create (if needed) and return a connection to the BMI database."""
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS bmi_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
        """
    )
    return conn


def save_entry(
    conn: sqlite3.Connection,
    name: str,
    weight: float,
    height: float,
    bmi: float,
    category: str,
) -> None:
    """Persist a single BMI measurement for a user."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        """INSERT INTO bmi_results (name, weight, height, bmi, category, timestamp)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (name, weight, height, round(bmi, 2), category, timestamp),
    )
    conn.commit()


def load_user_history(conn: sqlite3.Connection, name: str) -> pd.DataFrame:
    """Load all entries for a user, matched case-insensitively on name.

    Note: matching is case-insensitive (via SQL LOWER()) but names are
    stored exactly as entered — "Ricardo" and "ricardo" will both be
    returned by this query for either input, but each row keeps its own
    original casing in the `name` column. This is a deliberate trade-off:
    good enough for a single-machine hobby tracker, but a multi-user
    version should key users by ID rather than by name string.
    """
    query = "SELECT * FROM bmi_results WHERE LOWER(name) = LOWER(?)"
    return pd.read_sql_query(query, conn, params=(name,))
