import os
import uvicorn
from fastapi import FastAPI

# 1. Initialize the FastAPI app
app = FastAPI(title="Todo App")

# 2. Get the port from the environment variable, default to 8080
port = int(os.environ.get("PORT", 8080))

# 3. Create a simple root endpoint to show it's working
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API"}

# 4. Main entry point to run the server
if __name__ == "__main__":
    # 5. Print the user-requested startup message
    print(f"Server started in port {port}")
    
    # 6. Run the Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=port)