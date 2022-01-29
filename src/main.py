import uvicorn
from fastapi import FastAPI

from text_parser import parse_test

app = FastAPI()


@app.get("/")
async def root():
    parse_test()
    return {"message": "The End."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
