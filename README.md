# Whisper.cpp Transcription API

A lightweight, fully offline speech-to-text API built with [whisper.cpp](https://github.com/ggerganov/whisper.cpp), [FastAPI](https://fastapi.tiangolo.com/), and Docker.  
Supports local Ukrainian, English, Polish, and other language transcriptions with minimal resource usage.

---

## Features

-  Runs fully offline
-  Fast and memory-efficient (`whisper.cpp`)
-  Upload `.wav` files and get text
-  Language selection via query parameter (`lang`)
-  Swagger UI documentation at `/docs`

---

##  Project Structure

```
whisper-api/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   └── model/
│       └── ggml-base.bin
```

---

## Build & Run

### 1. Clone and build Docker image
```bash
docker build -t whisper-api .
```

### 2. Run the API
```bash
docker run -p 8000:8000 whisper-api
```

---

## Example Request

### Using `curl`:
```bash
curl -X POST "http://localhost:8000/transcribe?lang=uk" \
  -F "file=@your_audio.wav"
```

### Or open in browser:
[http://localhost:8000/docs](http://localhost:8000/docs) — interactive Swagger UI

---

## Supported Languages

Use the `lang` query parameter:

| Language | Code |
|----------|------|
| Ukrainian | `uk` |
| English   | `en` |
| Polish    | `pl` |
| Russian   | `ru` |
| ...       | many more (`whisper.cpp` supports 100+)

---

## Model

Default model: [`ggml-base.bin`](https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.bin)  
Included automatically in Docker build.

You can change to a different model (e.g., `small`, `medium`) by replacing the file in `app/model/`.

---

## License

MIT. Based on open source work by Georgi Gerganov ([whisper.cpp](https://github.com/ggerganov/whisper.cpp))
