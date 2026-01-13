from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.configuration import collection

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static",check_dir=True), name="static")


@app.get("/")
async def home(request:Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request}
    )

@app.post("/user_msg")
async def add_user_detail(name:str = Form(...), email:str = Form(...), msg:str = Form(...)):
    collection.insert_one({
        "name":name,
        "email": email,
        "msg":msg
    })
    return RedirectResponse("/#contact",status_code=303)

#  THIS keeps Render awake
@app.get("/health")
def health():
    return {"status": "ok"}



