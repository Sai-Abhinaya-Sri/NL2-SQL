# 🚀 Setup Guide - MySQL Database Connection

## Step-by-Step Setup Instructions

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- streamlit
- pandas
- mysql-connector-python
- plotly
- requests

---

### Step 2: Create Your Config File

```bash
# Copy the template
cp config.template.py config.py
```

Then open `config.py` in your text editor.

---

### Step 3: Get Your MySQL Connection Details

#### Option A: Using MySQL Workbench

1. Open **MySQL Workbench**
2. Look at your connection details:
   - **Hostname:** Usually `localhost` or `127.0.0.1`
   - **Port:** Usually `3306` (check in connection settings)
   - **Username:** Your MySQL username (often `root`)
   - **Password:** Your MySQL password
   - **Database:** The database you want to query

#### Option B: Using Command Line

Test your connection first:

```bash
mysql -h localhost -P 3306 -u root -p
```

If this works, you have the right credentials!

---

### Step 4: Update config.py

Open `config.py` and fill in your details:

```python
MYSQL_CONFIG = {
    'host': 'localhost',              # ✅ Your MySQL host
    'port': 3306,                     # ✅ Your MySQL port
    'database': 'sales_database',     # ✅ CHANGE THIS to your database name
    'user': 'root',                   # ✅ CHANGE THIS to your username
    'password': 'MySecurePassword123', # ✅ CHANGE THIS to your password
    'charset': 'utf8mb4',
    'autocommit': True
}
```

**Example real config:**
```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'database': 'ecommerce_db',
    'user': 'admin',
    'password': 'Admin@2024',
    'charset': 'utf8mb4',
    'autocommit': True
}
```

---

### Step 5: Get Groq API Key

1. Go to https://console.groq.com
2. Sign up / Log in
3. Navigate to **API Keys**
4. Click **Create API Key**
5. Copy the key

Update in `config.py`:

```python
GROQ_API_CONFIG = {
    'api_key': 'gsk_xxxxxxxxxxxxxxxxxxxxx',  # ✅ Paste your key here
    'model_name': 'llama-3.3-70b-versatile',
    'temperature': 0.1,
    'max_tokens': 500,
    'timeout': 30
}
```

---

### Step 6: Verify MySQL is Running

#### Windows:
1. Open **Services** (Win + R, type `services.msc`)
2. Find **MySQL** service
3. Make sure it's **Running**

#### Mac:
```bash
brew services list | grep mysql
```

#### Linux:
```bash
sudo systemctl status mysql
```

If not running, start it:
```bash
# Mac
brew services start mysql

# Linux
sudo systemctl start mysql

# Windows
net start MySQL80  # or your MySQL service name
```

---

### Step 7: Test Your Connection

Run this Python script to test:

```python
import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='your_database',
        user='your_username',
        password='your_password'
    )
    
    if conn.is_connected():
        print("✅ Connection successful!")
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"Found {len(tables)} tables:")
        for table in tables:
            print(f"  - {table[0]}")
        conn.close()
    else:
        print("❌ Connection failed")
        
except Exception as e:
    print(f"❌ Error: {e}")
```

---

### Step 8: Run the App

```bash
streamlit run app.py
```

The app should:
1. ✅ Auto-connect to your MySQL database
2. ✅ Load all table schemas
3. ✅ Detect relationships
4. ✅ Be ready for queries!

---

## 🔧 Common Issues & Solutions

### Issue 1: "Access denied for user"

**Problem:** Wrong username or password

**Solution:**
```sql
-- Reset password in MySQL
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

---

### Issue 2: "Can't connect to MySQL server"

**Problem:** MySQL not running or wrong host/port

**Solutions:**
- Check MySQL is running (see Step 6)
- Try `127.0.0.1` instead of `localhost`
- Verify port number (could be 3307, 3308 if multiple MySQL instances)

---

### Issue 3: "Unknown database"

**Problem:** Database name doesn't exist

**Solution:**
```sql
-- List all databases
SHOW DATABASES;

-- Create database if needed
CREATE DATABASE my_database;
```

---

### Issue 4: "Module not found: mysql.connector"

**Problem:** Package not installed

**Solution:**
```bash
pip install mysql-connector-python
```

---

### Issue 5: Connection works but no tables shown

**Problem:** User doesn't have SELECT permissions

**Solution:**
```sql
-- Grant permissions
GRANT SELECT ON your_database.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## 🎯 Quick Checklist

Before running the app, verify:

- [ ] MySQL server is running
- [ ] Database exists and has tables
- [ ] Username/password are correct
- [ ] Port number is correct (usually 3306)
- [ ] User has SELECT permissions
- [ ] `config.py` exists with real credentials
- [ ] Groq API key is set
- [ ] All dependencies installed (`pip install -r requirements.txt`)

---

## 🔐 Security Best Practices

### 1. Never commit config.py to GitHub

The `.gitignore` file already blocks it, but double-check:

```bash
git status
# config.py should NOT appear in the list
```

### 2. Use environment variables (Advanced)

Create `.env` file:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypass
GROQ_API_KEY=gsk_xxx
```

Then modify `config.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}
```

Install: `pip install python-dotenv`

---

## 📊 Example Database Structure

If you don't have a database yet, here's a sample:

```sql
CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES 
(1, 'John Doe', 'john@email.com', 'New York'),
(2, 'Jane Smith', 'jane@email.com', 'Los Angeles');

INSERT INTO orders VALUES
(1, 1, '2024-01-15', 299.99),
(2, 1, '2024-02-20', 149.50),
(3, 2, '2024-01-10', 599.00);
```

---

## 🎉 You're Ready!

Once everything is set up:

```bash
streamlit run app.py
```

Try asking:
- "Show me all customers"
- "What's the total revenue?"
- "Which customer spent the most?"

Enjoy your NL2SQL Dashboard! 🚀
