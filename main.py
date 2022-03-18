from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home() -> dict:
    return {'message':'OK'}