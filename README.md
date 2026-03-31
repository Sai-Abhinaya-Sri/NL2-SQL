# 📊 NL2SQL Dashboard - MySQL Database Edition

Convert natural language questions into SQL queries and get instant results from your MySQL database!

## ✨ What Changed?

**Before:** CSV files in `data_dump` folder  
**Now:** Direct MySQL database connection

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Database Connection

Open `config.py` and update your MySQL credentials:

```python
MYSQL_CONFIG = {
    'host': 'localhost',        # Your MySQL host (e.g., 'localhost' or IP address)
    'port': 3306,              # MySQL port (default: 3306)
    'database': 'your_database_name',  # YOUR DATABASE NAME HERE
    'user': 'your_username',   # YOUR MYSQL USERNAME
    'password': 'your_password',  # YOUR MYSQL PASSWORD
    'charset': 'utf8mb4',
    'autocommit': True
}
```

### 3. Set Groq API Key

In the same `config.py` file:

```python
GROQ_API_CONFIG = {
    'api_key': 'YOUR_GROQ_API_KEY_HERE',  # Get from https://console.groq.com
    ...
}
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🔧 Configuration Options

### Database Behavior

```python
DATABASE_CONFIG = {
    'auto_connect_on_startup': True,  # Auto-connect when app loads
    'show_all_tables': True,          # Load all tables
    'excluded_tables': [],            # Tables to skip (e.g., ['logs', 'temp'])
    'max_sample_rows': 3,             # Sample rows for AI context
    'connection_timeout': 10          # Connection timeout in seconds
}
```

### Connection Pooling

For better performance with multiple users:

```python
MYSQL_POOL_CONFIG = {
    'pool_name': 'nl2sql_pool',
    'pool_size': 5,               # Number of connections in pool
    'pool_reset_session': True
}
```

## 📋 Features

✅ **Direct MySQL Connection** - No CSV files needed  
✅ **Auto Schema Detection** - Automatically reads your database structure  
✅ **Relationship Detection** - Finds foreign key relationships  
✅ **Natural Language Queries** - "Show me top 10 customers by revenue"  
✅ **Auto-fix SQL Syntax** - Corrects common MySQL syntax errors  
✅ **Smart Visualizations** - Auto-selects best chart type  
✅ **Query History** - Track all your queries  
✅ **Save Queries** - Bookmark frequently used queries  
✅ **Table Explorer** - Browse your database tables  
✅ **Connection Pooling** - Better performance for multiple users  

## 🔍 How It Works

1. **Connect** - App connects to your MySQL database on startup
2. **Scan** - Reads all table schemas, columns, and relationships
3. **Ask** - You ask questions in plain English
4. **Generate** - Groq AI generates MySQL SQL query
5. **Execute** - Query runs on your database
6. **Visualize** - Results shown as tables and charts

## 💡 Example Queries

```
Show me all customers from California
What are the top 10 products by revenue?
Count orders by status
Show average order value by month
Find customers who haven't ordered in 90 days
Which products are low in stock?
Show sales by region for 2024
```

## 🛠️ Troubleshooting

### Connection Failed?

**Check:**
- ✅ MySQL server is running
- ✅ Database name exists
- ✅ Username/password are correct
- ✅ Host and port are correct
- ✅ User has SELECT permissions
- ✅ Firewall isn't blocking connection

### Test Connection from Terminal:

```bash
mysql -h localhost -P 3306 -u your_username -p your_database
```

### Common MySQL Ports:
- **Default:** 3306
- **XAMPP:** 3306
- **MAMP:** 8889
- **Docker:** Usually 3306 (check your docker-compose)

## 🔐 Security Notes

⚠️ **Never commit `config.py` with real credentials to GitHub!**

Add to `.gitignore`:
```
config.py
*.pyc
__pycache__/
.env
```

### Better: Use Environment Variables

```python
import os

MYSQL_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}
```

Then create `.env` file:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
```

## 📦 Dependencies

- **streamlit** - Web interface
- **pandas** - Data manipulation
- **mysql-connector-python** - MySQL database connector
- **plotly** - Interactive charts
- **requests** - API calls to Groq

## 🆚 Differences from CSV Version

| Feature | CSV Version | MySQL Version |
|---------|-------------|---------------|
| Data Source | CSV files in folder | MySQL database |
| Setup | Copy CSV files | Configure credentials |
| Real-time | No | Yes (live data) |
| Data Size | Limited by memory | Database limited |
| Updates | Manual file replacement | Automatic |
| Connection | In-memory SQLite | MySQL connection pool |

## 🔄 Migration from CSV Version

If you have the old CSV version:

1. **Import CSVs to MySQL:**
   ```sql
   LOAD DATA INFILE '/path/to/file.csv'
   INTO TABLE tablename
   FIELDS TERMINATED BY ','
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n'
   IGNORE 1 ROWS;
   ```

2. **Or use Python:**
   ```python
   import pandas as pd
   import mysql.connector
   
   conn = mysql.connector.connect(...)
   df = pd.read_csv('file.csv')
   df.to_sql('tablename', conn, if_exists='replace', index=False)
   ```

3. **Update config.py** with MySQL credentials

4. **Run the new app!**

## 📞 Support

Issues? Questions?
- Check `config.py` settings
- Verify MySQL connection manually
- Check Groq API key is valid
- Review error messages in sidebar

## 📄 License

MIT License - Feel free to use and modify!

---

**Happy Querying! 🚀**
