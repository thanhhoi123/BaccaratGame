from fastapi import FastAPI
from pydantic import BaseModel
from mybaccarat import gameStatus as game
from gameDB import gameDAO as db
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://localhost.baccarat.com",
    "https://localhost.baccarat.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.get("/play")
async def play():
    g = game.new()
    res = {"Banker_Cards": g.Banker_Cards,
    "Player_Cards": g.Player_Cards,
    "Banker_Score": g.Banker_Score,
    "Player_Score": g.Player_Score,
    "Results": g.Results}
    return res
if __name__ == "__main__":
    uvicorn.run("api:app", host="localhost", port=8000, log_level="info")