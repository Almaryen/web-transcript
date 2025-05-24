from fastapi import FastAPI, File, UploadFile, Query
import subprocess
import uuid
import os

app = FastAPI()

WHISPER_MODEL = "/app/app/model/ggml-base.bin"

@app.post("/transcribe/", summary="Transcribe audio", description="Upload a .wav file and get its transcription.")
async def transcribe(
    file: UploadFile = File(...),
    lang: str = Query("uk", description="Language code (e.g., uk, en, pl, ru)")
):
    temp_input = f"/tmp/{uuid.uuid4()}.wav"
    temp_output = temp_input + ".txt"

    # Save uploaded file
    with open(temp_input, "wb") as f:
        f.write(await file.read())

    # Run whisper-cli with language parameter
    result = subprocess.run([
        "/app/whisper.cpp/build/bin/whisper-cli",
        "-m", WHISPER_MODEL,
        "-f", temp_input,
        "-otxt",
        "-l", lang
    ], capture_output=True, text=True)

    if result.returncode != 0:
        return {"error": result.stderr}

    try:
        with open(temp_output, "r") as f:
            text = f.read()
    except FileNotFoundError:
        return {"error": "Output file not found"}

    os.remove(temp_input)
    os.remove(temp_output)

    return {"text": text}