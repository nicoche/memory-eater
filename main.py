
import os
import uvicorn
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from time import sleep
import os

app = FastAPI()

@app.get("/")
async def health():
	return {"health": "ok"}

@app.get("/allocate")
async def allocate():
	print("hi")
	sleep(3)
	print("allocating...")
	xd = bytearray(4512000000)
	print("allocated")
	sleep(1)
	print(len(xd))
	return {}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
