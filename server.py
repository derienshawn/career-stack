from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes.user import user
from app.routes.project import project



app = FastAPI()
app.include_router(user)
app.include_router(project)



@app.get("/")
def index():
    content = """
    <html>
            <a href="https://career-stack.hub.loginradius.com/auth.aspx?return_url=https://career-stack.herokuapp.com"><h4>Login</h4></a>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)     