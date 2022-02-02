from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.user import user


app = FastAPI()
app.include_router(user)

@app.get("/")
def index():
    content = """
    <html>
            <a href="https://career-stack.hub.loginradius.com/auth.aspx?return_url=https://career-stack.herokuapp.com"><h4>Login</h4></a>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)     

