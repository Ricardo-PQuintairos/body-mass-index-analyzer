📊 BMI Health Analyzer (CLI + Streamlit - Python)

A Python project to calculate and classify Body Mass Index (BMI), available as both a Command-Line Interface (CLI) and a Streamlit web application.

This project focuses on clean code, input validation, data handling, and evolving a simple script into an interactive data application.

🔄 Project Evolution

v1 (Initial Version)

Saved data in .txt
Basic functionality
Focus on core logic

v2 (CLI Improved)

Uses pandas + CSV for structured storage
Displays history dynamically
Better validation and modularization

  ( Streamlit App)

Interactive web interface
Real-time BMI calculation
Table visualization of results
Improved user experience

🚀 Features
📌 BMI calculation and classification
🔄 Metric & Imperial unit support (auto conversion)
💾 Data saved to bmi_results.csv
📈 History tracking (CLI + Web)
🖥️ Two interfaces: CLI and Web (Streamlit)

📂 Project Structure
.
├── cli_version/
│   └── main.py
├── streamlit_app/
│   └── app.py
├── bmi_results.csv
└── README.md

💡 Example Output

CLI:

BMI: 22.86 kg/m²
Category: Healthy Weight

Web App:

Interactive inputs
Instant results
Table with history

▶️ How to Run (Streamlit Version)
Install dependencies:
pip install streamlit pandas
Navigate to the app folder:
cd streamlit_app
Run the app:
streamlit run app.py
Open in your browser:
http://localhost:8501

🤝 Feedback
This is a learning project — feedback and suggestions are welcome.

📜 License
This project is open-source and available under the MIT License.
