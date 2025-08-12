# server.py  (or assignment2/server.py)
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"ok": True}

# simple check endpoint that uses Authorization header (optional)
@app.get("/api/ping")
async def ping(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(400, "Missing Authorization header")
    return {"token_preview": authorization[:10] + "..."}
