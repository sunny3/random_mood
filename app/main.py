from fastapi import FastAPI
from typing import List, Dict
import random
import json

app = FastAPI()

with open("./config.json") as f:
    bot_mood_mapping = json.load(f)
    
@app.get("/random_mood/")
async def random_mood(bot_id: str):
    if bot_id in bot_mood_mapping:
        moods = bot_mood_mapping[bot_id][:3]
        random_mood = random.choice(moods)
        return {"bot_id": bot_id, "random_mood": random_mood}
    else:
        return {"error": "Bot ID not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)