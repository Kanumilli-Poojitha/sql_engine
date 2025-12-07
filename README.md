# Simple SQL Engine (Python)

A lightweight custom SQL Engine built in Python without using any external database libraries.  
It can parse and execute basic SQL-like commands such as:

- CREATE TABLE  
- INSERT  
- SELECT  
- UPDATE  
- DELETE  
- WHERE clause  
- ORDER BY clause  

### Features

### ✔ CREATE TABLE
Create new tables dynamically with any number of columns:

CREATE TABLE users (name, age, city);

### ✔ INSERT
Insert new rows easily:

INSERT INTO users name=Arjun age=26 city=Hyderabad;

### ✔ SELECT  
Select all columns:

SELECT * FROM users;

Or select specific columns:

SELECT name, city FROM users;

### ✔ WHERE Support

SELECT * FROM users WHERE age=26;

### ✔ ORDER BY

SELECT * FROM users ORDER BY name;

### ✔ UPDATE

UPDATE users SET city=Mumbai WHERE name=Arjun;

### ✔ DELETE

DELETE FROM users WHERE age=22;

---

## ▶ How to Run

Make sure you're inside the project directory.

### 1️⃣ Activate virtual environment
Windows:

venv\Scripts\activate

### 2️⃣ Run the CLI

python main.py

## 🧪 Example Execution
   Take a look at Screenshot.png