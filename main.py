fromm fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
return {"message": "FitBuddy AI Fitness Plan Generator Ready!"} 