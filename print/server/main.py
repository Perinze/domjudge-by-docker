from typing import Union

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

import aiofiles

import subprocess


app = FastAPI()

@app.post("/print/")
async def printcode(file: UploadFile = File(...)):
    with open(file.filename, 'w') as out_file:
        content = await file.read()
        out_file.write(content.decode())
    subprocess.run(["./printsrc", file.filename])

    return {"result": "ok"}
