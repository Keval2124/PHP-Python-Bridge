from fastapi import FastAPI, HTTPException
import mysql.connector

# Initialize FastAPI
app = FastAPI()

# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'test'
}

# Connect to MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Endpoint to execute SQL query

@app.post("/query")
async def execute_query(query: str):
    try:
        # Execute the SQL query
        cursor.execute(query)

        # Fetch all results
        result = cursor.fetchall()

        # Return results as JSON
        return {"result": result}
    except Exception as e:
        # Handle exceptions and return as HTTP 400 error
        raise HTTPException(status_code=400, detail=str(e))
