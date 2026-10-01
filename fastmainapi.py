from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Anniversary Greeting API",
    description="A simple FastAPI application to send warm anniversary greetings.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Anniversary Greeting API! 💐"
    }


@app.get("/anniversary/{name}")
def anniversary_greeting(name: str):

    current_year = datetime.now().year

    return {
        "name": name,
        "year": current_year,
        "message": (
            f"🌸 Warmest anniversary wishes, {name}! 💐 "
            f"May this special anniversary bring you lots of happiness, "
            f"love, laughter, and beautiful memories. "
            f"Have a wonderful anniversary celebration! ❤️🎉"
        )
    }