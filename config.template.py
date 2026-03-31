"""
Configuration Template for NL2SQL Dashboard
COPY THIS FILE TO config.py AND FILL IN YOUR CREDENTIALS
"""

# =============================================================================
# GROQ API CONFIGURATION
# =============================================================================
GROQ_API_CONFIG = {
    'api_key': 'YOUR_GROQ_API_KEY_HERE',  # Get from https://console.groq.com
    'model_name': 'llama-3.3-70b-versatile',
    'temperature': 0.1,
    'max_tokens': 500,
    'timeout': 30
}

# =============================================================================
# MYSQL DATABASE CONFIGURATION
# =============================================================================
MYSQL_CONFIG = {
    'host': 'localhost',        # Your MySQL host (e.g., 'localhost', '127.0.0.1', or IP)
    'port': 3306,              # MySQL port (default: 3306)
    'database': 'your_database_name',  # CHANGE THIS: Your database name
    'user': 'your_username',   # CHANGE THIS: Your MySQL username
    'password': 'your_password',  # CHANGE THIS: Your MySQL password
    'charset': 'utf8mb4',
    'autocommit': True
}

# Optional: Connection pool settings for better performance
MYSQL_POOL_CONFIG = {
    'pool_name': 'nl2sql_pool',
    'pool_size': 5,
    'pool_reset_session': True
}

# =============================================================================
# DATABASE BEHAVIOR
# =============================================================================
DATABASE_CONFIG = {
    'auto_connect_on_startup': True,  # Auto-connect to DB when app starts
    'show_all_tables': True,          # Load all tables or specific ones
    'excluded_tables': [],            # Tables to exclude (e.g., ['temp_table', 'logs'])
    'max_sample_rows': 3,             # Number of sample rows to fetch for schema
    'connection_timeout': 10          # Seconds to wait for connection
}

# =============================================================================
# UI CONFIGURATION
# =============================================================================
UI_CONFIG = {
    'page_title': 'NL2SQL Dashboard',
    'page_icon': '📊',
    'layout': 'wide'
}

# =============================================================================
# SAMPLE PROMPTS
# =============================================================================
SAMPLE_PROMPTS = [
    "Show me all records from customers table",
    "What are the top 10 products by sales?",
    "Count total orders by region",
    "Show revenue by month for 2024",
    "Find customers who spent more than $1000",
    "Which products have low stock (less than 10 units)?",
    "Show average order value by customer segment",
    "List top 5 sales representatives by total revenue"
]
