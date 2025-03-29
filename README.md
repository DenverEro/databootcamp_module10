# 🌴 Hawaii Climate Analysis API

This project is a two-part climate data analysis and web application designed for a bootcamp homework assignment. In Part 1, data analysis is conducted in a Jupyter Notebook using SQLAlchemy and Pandas. In Part 2, a Flask API is built to expose climate data from a SQLite database via multiple routes.

---

## 📊 Part 1: Climate Data Analysis (Jupyter Notebook)

The notebook performs analysis on Honolulu, Hawaii’s historical climate data.

Key tasks:
- Connect to a SQLite database using SQLAlchemy ORM
- Retrieve and analyze precipitation and temperature data
- Identify the most active weather station
- Plot precipitation and temperature histograms
- Print summary statistics
- Close the session at the end

---

## 🌐 Part 2: Climate API (Flask App)

A RESTful API was built using Flask to serve climate data using clean, reusable query logic in `sql_helper.py`.

### 🚀 How to Run the App

1. Install required packages:

```bash
pip install flask sqlalchemy pandas

---

## 🧠 Technologies Used

- Python  
- Flask  
- SQLAlchemy ORM  
- Pandas  
- Matplotlib (in notebook)  
- SQLite

---

## ✅ Assignment Goals Met

- ✔️ ORM and SQL queries with SQLAlchemy  
- ✔️ Data visualization using Pandas/Matplotlib  
- ✔️ RESTful API using Flask  
- ✔️ DRY code with helper class (`SQLHelper`)  
- ✔️ Dynamic routes handling date-based queries  
- ✔️ Code tested and validated

---

## ✍️ Author

[Seven G] 