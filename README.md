BMI Analyzer

A command-line BMI (Body Mass Index) tracker built with Python, SQLite, and pandas. Logs weight/height entries, keeps a per-user history, and visualizes trends with matplotlib.

This is a rebuild of an earlier version of the project, refactored to apply things learned in Alura's Python for Data Science track — pandas, SQL, and general code structure.

Features
Log BMI entries in metric (kg, m) or imperial (lbs, inches) units
Persistent per-user history in a local SQLite database
Summary stats: average, min, max, and a 3-entry rolling average (pandas)
Trend plot over time (matplotlib)
Core logic covered by unit tests
Example
Enter your name: Juan
Choose unit system: [M]etric (kg, m) or [I]mperial (lbs, inches): m
Enter your weight (kg): 70
Enter your height (m): 1.76

BMI: 22.60 kg/m²
Category: Healthy Weight

Data saved to the database.

History of results:
 id name  weight  height  bmi        category            timestamp
  8 Juan    70.0    1.76 22.60  Healthy Weight  2026-09-03 16:14:57

Average BMI: 22.60
Min BMI: 22.60
Max BMI: 22.60
Project structure
bmi_analyzer/
├── main.py              # CLI entry point, input handling, main loop
├── bmi_logic.py         # Pure calculation/classification logic (no I/O)
├── database.py          # SQLite persistence layer
├── visualization.py     # Summary stats and plotting
├── tests/
│   └── test_bmi_logic.py
└── requirements.txt

The split keeps the pure logic (bmi_logic.py) completely free of I/O, which is what makes it possible to unit test without mocking input() or a database connection.

Setup
bash
pip install -r requirements.txt
python main.py                    # uses bmi_data.db in the current directory
python main.py --db custom.db     # or point it at a different file
Running tests
bash
pytest tests/
Known limitations
Users are identified by name (case-insensitive), not by a stable ID — fine for a single-user hobby tool, but a real multi-user version should key history by user ID instead.
Input validation checks that weight/height are positive, but not that they're realistic (e.g. a height of 0.1m would still be accepted).
Single-file SQLite database with no migrations; schema changes would need to be handled manually.

License

MIT — feel free to use this as a learning reference.
