# Whisper.cpp Quick Reference Guide

## Project at a Glance

**What**: High-performance C/C++ implementation of OpenAI's Whisper speech recognition  
**Why**: Offline, fast, lightweight inference with no external dependencies  
**Where**: Linux, macOS, Windows, Android, iOS, WebAssembly, Raspberry Pi, Docker  
**How**: Clone → Download Model → Build → Run  
**Version**: 1.8.6 (Stable)

---

## 5-Minute Quick Start

```bash
# 1. Clone
git clone https://github.com/ggml-org/whisper.cpp.git && cd whisper.cpp

# 2. Download model (choose one)
sh ./models/download-ggml-model.sh base.en    # Fast, English-only (142 MB)
sh ./models/download-ggml-model.sh base       # Fast, multilingual (142 MB)
sh ./models/download-ggml-model.sh tiny       # Fastest (75 MB)
sh ./models/download-ggml-model.sh large-v3   # Best quality (2.9 GB)

# 3. Build
cmake -B build && cmake --build build -j --config Release

# 4. Download sample audio
wget https://cdn.openai.com/whisper/draft-20220913a/jfk.wav -O samples/jfk.wav

# 5. Transcribe
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav
```

---

## Model Selection Guide

| Use Case               | Recommended Model | Size   | Speed      | Quality    |
| ---------------------- | ----------------- | ------ | ---------- | ---------- |
| 📱 Mobile/Raspberry Pi | tiny              | 75 MB  | ⚡⚡⚡⚡⚡ | ⭐         |
| 🚀 Real-time chat      | base              | 142 MB | ⚡⚡⚡⚡   | ⭐⭐       |
| 💻 Desktop (general)   | small             | 466 MB | ⚡⚡⚡     | ⭐⭐⭐     |
| 🎙️ Podcasts/audio      | medium            | 1.5 GB | ⚡⚡       | ⭐⭐⭐⭐   |
| 🏆 Best quality        | large-v3          | 2.9 GB | ⚡         | ⭐⭐⭐⭐⭐ |
| ⚖️ Balanced            | large-v3-turbo    | 1.5 GB | ⚡⚡⚡     | ⭐⭐⭐⭐   |

---

## Build Commands

```bash
# Basic (CPU only)
cmake -B build && cmake --build build -j

# With GPU (NVIDIA CUDA)
cmake -B build -DGGML_CUDA=1 && cmake --build build -j

# With GPU (AMD ROCm)
cmake -B build -DGGML_HIP=1 -DAMDGPU_TARGETS="gfx1100" && cmake --build build -j

# With GPU (Intel/OpenVINO)
cmake -B build -DWHISPER_OPENVINO=1 && cmake --build build -j

# With GPU (Cross-vendor Vulkan)
cmake -B build -DGGML_VULKAN=1 && cmake --build build -j

# Apple Silicon (Core ML)
./models/generate-coreml-model.sh base.en
cmake -B build -DWHISPER_COREML=1 && cmake --build build -j

# With FFmpeg (extended audio formats)
cmake -B build -DWHISPER_COMMON_FFMPEG=ON && cmake --build build -j

# With Real-time audio (SDL2)
cmake -B build -DWHISPER_SDL2=ON && cmake --build build -j

# With CPU acceleration (OpenBLAS)
cmake -B build -DGGML_BLAS=1 && cmake --build build -j
```

---

## Common Commands

```bash
# Basic transcription
./build/bin/whisper-cli -m models/ggml-base.en.bin -f audio.wav

# Multilingual + auto-detect language
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav

# Specify language
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l es
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l fr
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l de

# With GPU
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu

# Multiple threads (faster on multi-core CPUs)
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t 8

# Word-level timestamps
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -ml 1

# Output as JSON
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -j

# Output as SRT (subtitles)
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -srt

# With confidence color-coding
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav --print-colors

# Translate to English
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -tr
```

---

## Audio Format Conversion

```bash
# Convert MP3 to 16-bit WAV (required format)
ffmpeg -i audio.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Convert M4A (iPhone audio)
ffmpeg -i audio.m4a -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Convert FLAC
ffmpeg -i audio.flac -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Convert OGG
ffmpeg -i audio.ogg -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Batch convert all MP3s
for file in *.mp3; do
    ffmpeg -i "$file" -ar 16000 -ac 1 -c:a pcm_s16le "${file%.mp3}.wav"
done
```

---

## Server Mode

```bash
# Start server
./build/bin/whisper-server -m models/ggml-base.bin --host 127.0.0.1 --port 8080

# Web UI: http://localhost:8080

# API call (Python)
import requests
resp = requests.post('http://localhost:8080/inference',
    files={'file': open('audio.wav', 'rb')},
    data={'language': 'en'})
print(resp.json())

# API call (cURL)
curl -X POST -F "file=@audio.wav" -F "language=en" \
    http://localhost:8080/inference
```

---

## Real-Time Transcription

```bash
# From microphone (requires SDL2)
cmake -B build -DWHISPER_SDL2=ON
cmake --build build -j
./build/bin/whisper-stream -m models/ggml-base.en.bin

# Custom parameters
./build/bin/whisper-stream -m models/ggml-base.bin \
    -t 4 \
    --step 500 \
    --length 5000
```

---

## Model Quantization

```bash
# Quantize for ~65% size reduction with minimal quality loss
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0

# Use quantized model (faster, smaller)
./build/bin/whisper-cli -m models/ggml-base-q5_0.bin -f audio.wav

# Quantization methods:
# q4_0 - Smallest/fastest
# q4_1 - Good balance
# q5_0 - Best balance (RECOMMENDED)
# q5_1 - Near lossless
```

---

## Docker

```bash
# Download model
docker run -it --rm -v $(pwd)/models:/models \
    ghcr.io/ggml-org/whisper.cpp:main \
    "./models/download-ggml-model.sh base /models"

# Transcribe
docker run -it --rm \
    -v $(pwd)/models:/models \
    -v $(pwd)/audio:/audio \
    ghcr.io/ggml-org/whisper.cpp:main \
    "whisper-cli -m /models/ggml-base.bin -f /audio/audio.wav"

# Server
docker run -d -p 8080:8080 -v $(pwd)/models:/models \
    ghcr.io/ggml-org/whisper.cpp:main \
    "whisper-server -m /models/ggml-base.bin --host 0.0.0.0"

# Available images:
# ghcr.io/ggml-org/whisper.cpp:main        - CPU
# ghcr.io/ggml-org/whisper.cpp:main-cuda   - NVIDIA GPU
# ghcr.io/ggml-org/whisper.cpp:main-vulkan - Vulkan GPU
```

---

## Supported Languages

```bash
# English
-l en

# Spanish
-l es

# French
-l fr

# German
-l de

# Chinese (simplified)
-l zh

# Japanese
-l ja

# Russian
-l ru

# Arabic
-l ar

# Hindi
-l hi

# Korean
-l ko

# Auto-detect
-l auto

# Full list: 99 languages supported
./build/bin/whisper-cli -h  # Shows all language codes
```

---

## Troubleshooting

### Build Issues

```bash
# Clean rebuild
rm -rf build && cmake -B build && cmake --build build -j

# Specific compiler
cmake -B build -DCMAKE_CXX_COMPILER=g++-11
cmake --build build -j

# Check for errors
cmake --build build 2>&1 | grep error

# Verbose output
cmake --build build -v
```

### Runtime Issues

```bash
# Model not found
ls -lh models/
# If missing, download:
sh ./models/download-ggml-model.sh base.en

# Audio format error
file audio.wav
# Must be 16-bit PCM, 16 kHz, mono
ffmpeg -i audio.wav -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# GPU not working
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav | grep -i gpu

# Out of memory
# Use smaller model: tiny, base, or small
# Or use quantized version: -q5_0
```

---

## Performance Tips

```bash
# 1. Use quantized models
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0

# 2. Enable GPU (10-100x faster)
cmake -B build -DGGML_CUDA=1  # or -DGGML_VULKAN=1, etc.

# 3. Use smaller model (tiny, base, small)
./build/bin/whisper-cli -m models/ggml-tiny.bin -f audio.wav

# 4. Match threads to CPU cores
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t $(nproc)

# 5. Disable timestamps if not needed
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav --no-timestamps

# 6. Use compiled-with-GPU version
# Compile with GPU support: -DGGML_CUDA=1, -DGGML_VULKAN=1, etc.
```

---

## Language Bindings

```bash
# Go
cd bindings/go && go build

# Java
cd bindings/java && ./mvnw clean install

# JavaScript/Node.js
cd bindings/javascript && npm install

# Ruby
cd bindings/ruby && gem install whisper_cpp

# Python (use C library directly via ctypes)
import ctypes
whisper = ctypes.CDLL('./build/libwhisper.so')
```

---

## File Structure

```
whisper.cpp/
├── include/whisper.h         ← Main C API
├── src/whisper.cpp           ← Implementation
├── examples/
│   ├── cli/                  ← Command-line tool
│   ├── server/               ← HTTP server
│   ├── stream/               ← Real-time audio
│   ├── whisper.wasm/         ← WebAssembly
│   └── [others]
├── models/                   ← Model scripts & binaries
├── bindings/                 ← Language bindings
├── ggml/                     ← ML library (embedded)
└── CMakeLists.txt            ← Build configuration
```

---

## Useful Links

- **GitHub**: https://github.com/ggml-org/whisper.cpp
- **Issues**: https://github.com/ggml-org/whisper.cpp/issues
- **Models**: https://huggingface.co/ggerganov/whisper.cpp
- **GGML**: https://github.com/ggml-org/ggml
- **OpenAI Whisper**: https://github.com/openai/whisper

---

## Environment Variables

```bash
# Enable debug logging
WHISPER_DEBUG=1 ./build/bin/whisper-cli ...

# Set OpenMP threads
OMP_NUM_THREADS=8 ./build/bin/whisper-cli ...

# CUDA device selection
CUDA_VISIBLE_DEVICES=0 ./build/bin/whisper-cli ...
```

---

## One-Liner Recipes

```bash
# Clone, build, and transcribe in one command
git clone https://github.com/ggml-org/whisper.cpp.git && cd whisper.cpp && \
  sh ./models/download-ggml-model.sh base.en && \
  cmake -B build && cmake --build build -j && \
  wget https://cdn.openai.com/whisper/draft-20220913a/jfk.wav -O samples/jfk.wav && \
  ./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

# Transcribe all WAV files in a folder
for f in *.wav; do
  ./build/bin/whisper-cli -m models/ggml-base.en.bin -f "$f" > "${f%.wav}.txt"
done

# Batch convert and transcribe
for f in *.mp3; do
  ffmpeg -i "$f" -ar 16000 -ac 1 -c:a pcm_s16le "${f%.mp3}.wav" && \
  ./build/bin/whisper-cli -m models/ggml-base.bin -f "${f%.mp3}.wav"
done

# Docker one-liner transcription
docker run --rm -v "$(pwd):/data" ghcr.io/ggml-org/whisper.cpp:main \
  sh -c "cd /data && ./models/download-ggml-model.sh base && \
  whisper-cli -m models/ggml-base.bin -f input.wav"
```

---

## Key Statistics

- **Current Version**: 1.8.6
- **Models Available**: 12 (tiny→large-v3)
- **Languages Supported**: 99
- **GPU Backends**: 8+ (CUDA, Metal, ROCm, Vulkan, OpenVINO, etc.)
- **Platforms**: 10+ (Windows, macOS, Linux, iOS, Android, WASM, etc.)
- **Performance**: 1-200x CPU speed depending on model & hardware
- **License**: MIT (Free for commercial use)

---

Last updated: 2026-06-16
