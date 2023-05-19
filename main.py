from fastapi import fastAPI

app=FastAPI()
@app.get("/")
def index():
    return"hola a todos, quieres saber de futbol