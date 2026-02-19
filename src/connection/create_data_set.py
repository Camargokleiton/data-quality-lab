from connection import conn
import pandas as pd

# Function to create DataFrame from SQL query
def create_dataframe(table_name):
    connection = conn.connection()
    query = f"SELECT * FROM {table_name};"    
    result = conn.execute_read_query(connection, query)
    conn.close_connection(connection)
    df = pd.DataFrame(result)
    return df