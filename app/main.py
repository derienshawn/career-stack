from fastapi.responses import HTMLResponse
from server import *

@app.get("/")
def index():
    content = """
    <html>
            <a href="https://career-stack.hub.loginradius.com/auth.aspx?return_url=https://career-stack.herokuapp.com"><h4>Login</h4></a>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)     
