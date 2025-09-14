from fastapi import FastAPI

app = FastAPI(title="MAYA Assistant")

@app.get("/")
def home():
    return {"message": "MAYA backend is running "}
