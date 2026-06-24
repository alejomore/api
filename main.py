from fastapi import FastAPI

app = FastAPI()

def mimensaje():
    return "¡Hola, Fast API!"

@app.get("/")
def read_root():
    return {"message": mimensaje()}