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

In Part 2, the analysis from the notebook is transformed into a fully functional RESTful API using Flask. The API connects to the same SQLite database and serves climate data through various well-structured routes.

A custom `SQLHelper` class is used to organize all database query logic and promote clean, modular code. Each route uses a method from this helper class to access and return relevant data as JSON.

The API provides endpoints for:
- Recent precipitation data
- List of weather observation stations
- Temperature observations from the most active station
- Min, max, and average temperature stats from a given start date or date range

This design allows users to programmatically access historical weather data from Honolulu, Hawaii.

---

## 🔗 Available API Routes

| Route | Description |
|-------|-------------|
| `/` | Welcome route with list of endpoints |
| `/api/v1.0/precipitation` | Last 12 months of precipitation data (date: prcp) |
| `/api/v1.0/stations` | List of all station IDs |
| `/api/v1.0/tobs` | Last 12 months of temperature observations from the most active station |
| `/api/v1.0/<start>` | Min, avg, and max temperature from start date to end |
| `/api/v1.0/<start>/<end>` | Min, avg, and max temperature for given date range |

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

[Seven G](https://github.com/DenverEro)  