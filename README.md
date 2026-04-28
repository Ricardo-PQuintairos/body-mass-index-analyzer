# 📊 BMI Health Analyzer (CLI - Python)

A simple Command-Line Interface (CLI) application built in Python to calculate and classify Body Mass Index (BMI), with support for both metric and imperial units.

This project focuses on practicing clean code structure, input validation, and basic application design rather than just solving the calculation itself.

---

## 🚀 Features

* 📌 BMI calculation using weight and height
* 📊 Classification based on standard BMI categories
* 🔄 Support for:

  * Metric units (kg, meters)
  * Imperial units (lbs, inches) with automatic conversion
* 🛡️ Input validation and error handling
* 🔁 Continuous execution loop for repeated use
* 💾 Data persistence: saves results to a `.txt` file

---

## 🧠 What I Learned

* Writing modular and reusable functions
* Structuring a small application using control flow (loops and conditionals)
* Handling user input safely with exception handling
* Separating logic (calculation, classification, conversion, persistence)
* Thinking beyond scripts and towards simple software design

---



## 📂 Project Structure (Current)

```bash
.
├── main.py
├── bmi_results.txt
└── README.md
```

---

## 💡 Example Output

```text
BMI: 22.86 kg/m²
Category: Healthy Weight
```

Saved to file:

```text
Weight: 70.00 kg | Height: 1.75 m | BMI: 22.86 kg/m² | Category: Healthy Weight
```

---

## 🔧 Future Improvements

* ⏱️ Add timestamps to saved results
* 🖥️ Improve user interface (CLI enhancements or GUI)
* 📈 Add data analysis features (history, averages, trends)
* 🌐 Potential web version using Flask

---

## 🤝 Feedback

This is a learning project, so feedback, suggestions, and improvements are welcome.

---

## 📜 License

This project is open-source and available under the MIT License.
