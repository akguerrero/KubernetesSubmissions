import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# 1. Initialize the FastAPI app
app = FastAPI(title="Todo App")

# 2. Get the port from the environment variable, default to 8080
port = int(os.environ.get("PORT", 8080))

# Define our HTML content as a string
html_content = """
<html>
    <head>
        <title>Todo App</title>
        <style>
            body { 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
                margin: 0; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                background-color: #f4f7f6;
            }
            div { 
                text-align: center; 
                padding: 2rem 3rem; 
                border-radius: 10px; 
                background-color: #ffffff; 
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }
            h1 { 
                color: #333; 
            }
            p { 
                color: #555; 
                font-size: 1.1rem; 
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Welcome to the Todo App</h1>
            <p>This is the main landing page. Our API is running!</p>
        </div>
    </body>
</html>
"""

# 3. Create a simple root endpoint to show it's working
@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(content=html_content)

# 4. Main entry point to run the server
if __name__ == "__main__":
    # 5. Print the user-requested startup message
    print(f"Server started in port {port}")
    
    # 6. Run the Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=port)