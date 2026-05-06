📊 BMI Health Analyzer (CLI - Python)

A simple Command-Line Interface (CLI) application built in Python to calculate and classify Body Mass Index (BMI), with support for both metric and imperial units.

This project focuses on practicing clean code structure, input validation, data handling, and small application design, going beyond just performing the calculation.

🚀 Features

📌 BMI calculation using weight and height

📊 Classification based on standard BMI categories

🔄 Support for:

Metric units (kg, meters)
Imperial units (lbs, inches) with automatic conversion

🛡️ Input validation and error handling

🔁 Continuous execution loop for repeated use

💾 Data persistence: saves results to a CSV file

📈 Displays history of previous results directly in the terminal

🧠 What I Learned
Writing modular and reusable functions
Structuring a small application using control flow (loops and conditionals)
Handling user input safely with exception handling
Working with pandas for data storage and retrieval
Managing file operations (create, append, read)
Separating responsibilities (calculation, classification, conversion, persistence)
Thinking beyond scripts and towards simple software design
📂 Project Structure (Current)
.
├── main.py
├── bmi_results.csv
└── README.md
💡 Example Output
BMI: 22.86 kg/m²
Category: Healthy Weight

Saved to file (bmi_results.csv):

Weight (kg) | Height (m) | BMI  | Category
70.0        | 1.75       | 22.86| Healthy Weight

Terminal history display:

History of results:
[DataFrame output shown here]

🤝 Feedback

This is a learning project, so feedback, suggestions, and improvements are always welcome.

📜 License

This project is open-source and available under the MIT License.
