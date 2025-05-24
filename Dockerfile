FROM ubuntu:22.04

# Install system dependencies (including libomp-dev for whisper.cpp)
RUN apt-get update && apt-get install -y \
    python3 python3-pip ffmpeg build-essential git cmake curl wget \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Збираємо, залишаємо бінарник прямо в папці
RUN git clone https://github.com/ggerganov/whisper.cpp.git \
    && cd whisper.cpp \
    && make

ENV PATH=\"/app/whisper.cpp/build/bin:$PATH\"

# Install Python dependencies (including multipart support)
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Download whisper model (ggml-base.bin)
RUN mkdir -p /app/app/model \
    && curl -L -o /app/app/model/ggml-base.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.bin

# Copy application source code
COPY app ./app

EXPOSE 8000

# Run FastAPI server with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]