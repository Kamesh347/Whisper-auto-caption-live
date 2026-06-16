# Whisper.cpp - Complete Comprehensive Guide

**Last Updated**: 2026-06-16  
**Project Version**: 1.8.6 (Stable)  
**License**: MIT  
**Repository**: https://github.com/ggml-org/whisper.cpp

---

## Table of Contents

1. [Project Overview & Objectives](#project-overview--objectives)
2. [Architecture & Components](#architecture--components)
3. [Supported Platforms](#supported-platforms)
4. [Installation & Setup](#installation--setup)
5. [Available Models](#available-models)
6. [Building the Project](#building-the-project)
7. [Running Examples](#running-examples)
8. [Advanced Configuration](#advanced-configuration)
9. [Language Bindings](#language-bindings)
10. [Performance & Optimization](#performance--optimization)
11. [Troubleshooting](#troubleshooting)

---

## Project Overview & Objectives

### What is Whisper.cpp?

**Whisper.cpp** is a high-performance, lightweight C/C++ implementation of OpenAI's Whisper automatic speech recognition (ASR) model. It enables real-time, offline speech-to-text transcription with minimal dependencies.

### Primary Objectives

1. **High Performance**: Deliver fast speech recognition inference on consumer hardware
2. **Lightweight**: Minimal memory footprint and zero runtime allocations
3. **Cross-Platform**: Support diverse hardware platforms and operating systems
4. **No Dependencies**: Pure C/C++ implementation without external requirements
5. **GPU Acceleration**: Leverage hardware accelerators (NVIDIA, AMD, Apple Silicon, etc.)
6. **Privacy**: Enable on-device inference without cloud connectivity
7. **Portability**: Easy integration into applications and embedded systems

### Key Features

- ✅ Plain C/C++ implementation without dependencies
- ✅ Apple Silicon optimized (ARM NEON, Accelerate, Metal, Core ML)
- ✅ x86 AVX intrinsics support
- ✅ POWER architecture VSX support
- ✅ Mixed F16/F32 precision
- ✅ Integer quantization for reduced memory usage
- ✅ Zero memory allocations at runtime
- ✅ Multiple GPU backends (Vulkan, CUDA, HIP, OpenVINO, etc.)
- ✅ CPU-only inference support
- ✅ Voice Activity Detection (VAD)
- ✅ Real-time streaming support
- ✅ Word-level timestamps
- ✅ Multiple language support

---

## Architecture & Components

### Project Structure

```
whisper.cpp/
├── include/               # Public C API headers
│   └── whisper.h         # Main API interface
├── src/                   # Core implementation
│   ├── whisper.cpp       # Main Whisper implementation
│   ├── ggml.c            # GGML tensor library (embedded)
│   └── [platform-specific code]
├── examples/             # Reference implementations
│   ├── cli/              # Command-line tool
│   ├── server/           # HTTP server interface
│   ├── stream/           # Real-time streaming
│   ├── command/          # Voice command recognition
│   ├── python/           # Python examples
│   ├── whisper.wasm/     # WebAssembly support
│   ├── whisper.android/  # Android SDK
│   ├── whisper.objc/     # iOS/macOS SDK
│   ├── whisper.swiftui/  # SwiftUI wrapper
│   └── [other examples]
├── bindings/             # Language bindings
│   ├── go/               # Go bindings
│   ├── java/             # Java bindings
│   ├── javascript/       # JavaScript bindings
│   └── ruby/             # Ruby bindings
├── ggml/                 # GGML machine learning library
│   ├── include/          # GGML headers
│   ├── src/              # GGML implementation
│   └── cmake/            # GGML CMake configuration
├── models/               # Model conversion and download scripts
├── cmake/                # CMake build configuration
├── grammars/             # GBNF grammar files
├── tests/                # Test suite
├── CMakeLists.txt        # Primary CMake configuration
├── Makefile              # Quick build commands
└── README.md             # Main documentation
```

### Core Components

#### 1. **whisper.h (Public C API)**

- Defines the complete interface for using Whisper
- Thread-safe operations (when context is not shared)
- C-style interface for maximum compatibility

#### 2. **GGML Library**

- Embedded tensor computation library
- Handles all matrix operations for the model
- Supports various hardware backends
- Zero-copy memory management where possible

#### 3. **Examples**

- **whisper-cli**: Command-line tool for transcription
- **whisper-server**: HTTP API server
- **whisper-stream**: Real-time microphone input
- **whisper-command**: Voice command detection
- **quantize**: Model quantization tool
- **lsp**: Language Server Protocol implementation

#### 4. **Platform-Specific Implementations**

- Core ML acceleration (macOS/iOS)
- CUDA kernels (NVIDIA)
- HIP kernels (AMD)
- Vulkan compute shaders (cross-vendor)

---

## Supported Platforms

### Operating Systems

| Platform              | Status             | Notes                          |
| --------------------- | ------------------ | ------------------------------ |
| macOS (Intel)         | ✅ Fully Supported | Native Metal GPU support       |
| macOS (Apple Silicon) | ✅ Optimized       | First-class M1/M2/M3 support   |
| iOS                   | ✅ Supported       | See `examples/whisper.objc`    |
| iPadOS                | ✅ Supported       | Same as iOS                    |
| Android               | ✅ Supported       | See `examples/whisper.android` |
| Linux                 | ✅ Fully Supported | All major distributions        |
| FreeBSD               | ✅ Supported       | Community tested               |
| Windows               | ✅ Fully Supported | MSVC and MinGW compatible      |
| Raspberry Pi          | ✅ Supported       | ARMv7/ARMv8 optimized          |
| WebAssembly           | ✅ Supported       | Browser-based inference        |
| Docker                | ✅ Supported       | Pre-built images available     |

### Processor Architectures

- **x86-64**: Full AVX/AVX2/AVX512 support
- **ARM64 (Apple Silicon)**: NEON, Accelerate, Metal optimized
- **ARM32/ARMv7**: NEON optimized
- **POWER9/POWER10**: VSX intrinsics support
- **RISC-V**: Basic support

### GPU Backends

| GPU Backend        | Platforms       | Performance    | Status       |
| ------------------ | --------------- | -------------- | ------------ |
| **Metal**          | macOS, iOS      | ~3x vs CPU     | ✅ Mature    |
| **Core ML (ANE)**  | Apple Silicon   | Best on device | ✅ Mature    |
| **CUDA**           | NVIDIA GPUs     | Excellent      | ✅ Mature    |
| **HIP (ROCm)**     | AMD GPUs        | Good           | ✅ Mature    |
| **Vulkan**         | Cross-vendor    | Good           | ✅ Mature    |
| **OpenVINO**       | Intel CPUs/GPUs | Good           | ✅ Mature    |
| **Ascend NPU**     | Huawei          | Excellent      | ✅ Supported |
| **Moore Threads**  | MT GPUs         | Good           | ✅ Supported |
| **CPU (OpenBLAS)** | All platforms   | Moderate       | ✅ Supported |

---

## Installation & Setup

### Prerequisites

#### Base Requirements

- Git
- CMake 3.5+ (or Make for quick builds)
- C/C++ compiler:
  - **macOS**: Xcode Command Line Tools
  - **Linux**: GCC or Clang
  - **Windows**: MSVC or MinGW
  - **Emscripten** (for WebAssembly)

#### Optional Dependencies (for specific features)

- **FFmpeg**: Extended audio format support
- **SDL2**: Real-time audio input
- **CUDA Toolkit**: NVIDIA GPU acceleration
- **ROCm**: AMD GPU acceleration
- **Vulkan SDK**: Vulkan GPU support
- **OpenVINO**: Intel GPU/CPU acceleration
- **Core ML Tools**: macOS Neural Engine support
- **libcurl**: Model downloading from URLs

### Step 1: Clone the Repository

```bash
# Clone the main repository
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp

# Create a working directory for models and samples
mkdir -p models samples
```

### Step 2: Download a Model

```bash
# Method 1: Using provided script (RECOMMENDED)
# Download base.en model (English-only, faster, smaller)
sh ./models/download-ggml-model.sh base.en

# Alternative models:
sh ./models/download-ggml-model.sh tiny.en      # Fastest, smallest (English only)
sh ./models/download-ggml-model.sh base          # Fast, multilingual
sh ./models/download-ggml-model.sh small         # Medium speed/quality
sh ./models/download-ggml-model.sh medium        # High quality
sh ./models/download-ggml-model.sh large-v3      # Best quality (slow)

# Method 2: Manual download from Hugging Face
# https://huggingface.co/ggerganov/whisper.cpp/tree/main
# Place the .bin file in the models/ directory

# Method 3: Convert PyTorch models manually
# See "Converting Custom Models" section below
```

### Step 3: Prepare Audio Files

#### Supported Audio Formats

- **Native**: 16-bit WAV files (recommended)
- **With FFmpeg**: MP3, FLAC, OGG, M4A, OPUS, etc.
- **Sample rate**: 16 kHz (automatically resampled if different)

#### Download Sample Audio

```bash
# Option 1: Quick sample
wget https://cdn.openai.com/whisper/draft-20220913a/jfk.wav -O samples/jfk.wav

# Option 2: Download multiple samples
make samples

# Option 3: Use your own audio file
# Convert any audio to 16 kHz WAV format:
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
ffmpeg -i input.m4a -ar 16000 -ac 1 -c:a pcm_s16le output.wav
ffmpeg -i input.flac -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

### Step 4: Install Optional Dependencies (Platform-Specific)

#### macOS

```bash
# Install Xcode Command Line Tools
xcode-select --install

# For FFmpeg support
brew install ffmpeg

# For real-time audio (SDL2)
brew install sdl2

# For M1/M2/M3 optimization (optional)
# Already included in the system
```

#### Ubuntu/Debian

```bash
# Essential build tools
sudo apt install -y build-essential cmake

# For FFmpeg support
sudo apt install -y libavcodec-dev libavformat-dev libavutil-dev

# For real-time audio (SDL2)
sudo apt install -y libsdl2-dev

# For NVIDIA GPU (optional)
# See CUDA installation guide
```

#### Windows (MSVC)

```powershell
# Install Visual Studio 2019 or 2022 with C++ workload
# Download from: https://visualstudio.microsoft.com/

# For FFmpeg support
# Download pre-built FFmpeg binaries or use vcpkg

# For CUDA support (NVIDIA GPU)
# Download from: https://developer.nvidia.com/cuda-downloads
```

#### Fedora/RHEL

```bash
# Essential build tools
sudo dnf install -y gcc g++ cmake

# For FFmpeg support
sudo dnf install -y libavcodec-free-devel libavformat-free-devel libavutil-free-devel
```

---

## Available Models

### Model Comparison

| Model              | Disk   | RAM     | Speed      | Quality    | Multilingual | Use Case                   |
| ------------------ | ------ | ------- | ---------- | ---------- | ------------ | -------------------------- |
| **tiny.en**        | 75 MB  | ~273 MB | ⚡⚡⚡⚡⚡ | ⭐         | ❌           | Real-time, IoT, mobile     |
| **tiny**           | 75 MB  | ~273 MB | ⚡⚡⚡⚡⚡ | ⭐         | ✅           | Real-time multilingual     |
| **base.en**        | 142 MB | ~388 MB | ⚡⚡⚡⚡   | ⭐⭐       | ❌           | Fast English transcription |
| **base**           | 142 MB | ~388 MB | ⚡⚡⚡⚡   | ⭐⭐       | ✅           | General multilingual       |
| **small.en**       | 466 MB | ~852 MB | ⚡⚡⚡     | ⭐⭐⭐     | ❌           | High-quality English       |
| **small**          | 466 MB | ~852 MB | ⚡⚡⚡     | ⭐⭐⭐     | ✅           | High-quality multilingual  |
| **medium.en**      | 1.5 GB | ~2.1 GB | ⚡⚡       | ⭐⭐⭐⭐   | ❌           | Excellent English          |
| **medium**         | 1.5 GB | ~2.1 GB | ⚡⚡       | ⭐⭐⭐⭐   | ✅           | Excellent multilingual     |
| **large-v1**       | 2.9 GB | ~3.9 GB | ⚡         | ⭐⭐⭐⭐⭐ | ✅           | Best quality (slow)        |
| **large-v2**       | 2.9 GB | ~3.9 GB | ⚡         | ⭐⭐⭐⭐⭐ | ✅           | Best quality (slow)        |
| **large-v3**       | 2.9 GB | ~3.9 GB | ⚡         | ⭐⭐⭐⭐⭐ | ✅           | Optimized large model      |
| **large-v3-turbo** | 1.5 GB | ~2.1 GB | ⚡⚡⚡     | ⭐⭐⭐⭐   | ✅           | Balance of quality/speed   |

### Downloading Models

```bash
# Quick download (one-liner for each model)
bash ./models/download-ggml-model.sh tiny.en
bash ./models/download-ggml-model.sh base.en
bash ./models/download-ggml-model.sh small
bash ./models/download-ggml-model.sh medium
bash ./models/download-ggml-model.sh large-v3

# Verify download
ls -lh models/
```

### Model Quantization

Quantized models use less disk space and memory with minimal quality loss:

```bash
# Build with quantization support
cmake -B build
cmake --build build -j

# Quantize a model (Q5_0 method - good balance)
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0

# Quantization methods available:
# q4_0 - Very fast, lowest quality
# q4_1 - Good speed/quality balance
# q5_0 - Excellent balance (RECOMMENDED)
# q5_1 - Best quality
# q8_0 - Near lossless (larger files)

# Use quantized model
./build/bin/whisper-cli -m models/ggml-base-q5_0.bin -f samples/jfk.wav
```

---

## Building the Project

### Method 1: Quick Build (Makefile)

```bash
# Simple build (default Release)
make build

# Build and download a specific model, then run on samples
make base.en

# Download additional audio samples
make samples

# Clean build
make clean
```

### Method 2: CMake Build (Recommended)

#### Basic Build

```bash
# Create build directory
cmake -B build

# Compile (Release mode, multi-threaded)
cmake --build build -j --config Release

# Binary location
./build/bin/whisper-cli
./build/bin/whisper-server
./build/bin/quantize
```

#### Build with Specific Options

```bash
# With FFmpeg support (for extended audio formats)
cmake -B build -DWHISPER_COMMON_FFMPEG=ON
cmake --build build -j --config Release

# With SDL2 support (real-time audio)
cmake -B build -DWHISPER_SDL2=ON
cmake --build build -j --config Release

# Both FFmpeg and SDL2
cmake -B build -DWHISPER_COMMON_FFMPEG=ON -DWHISPER_SDL2=ON
cmake --build build -j --config Release
```

#### GPU-Accelerated Builds

##### NVIDIA CUDA

```bash
# Prerequisites: CUDA Toolkit installed
# https://developer.nvidia.com/cuda-downloads

cmake -B build -DGGML_CUDA=1
cmake --build build -j --config Release

# For newer GPUs (RTX 4000+ series, compute capability 8.6+)
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="86"
cmake --build build -j --config Release

# For older GPUs (RTX 2000 series, compute capability 7.5)
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="75"
cmake --build build -j --config Release

# RTX 5000 series (compute capability 9.0)
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="90"
cmake --build build -j --config Release
```

##### AMD ROCm (HIP)

```bash
# Prerequisites: ROCm installed
# https://rocm.docs.amd.com/

# Find your GPU architecture
rocminfo | grep "gfx"

# Common architectures:
# RX 7900 XTX: gfx1100
# RX 7800 XT: gfx1101
# RX 9070 XT: gfx1201

cmake -B build -DGGML_HIP=1 -DAMDGPU_TARGETS="gfx1100"
cmake --build build -j --config Release

# Multiple GPU architectures
cmake -B build -DGGML_HIP=1 -DAMDGPU_TARGETS="gfx1100;gfx1101"
cmake --build build -j --config Release
```

##### Vulkan (Cross-Vendor)

```bash
# Prerequisites: Vulkan SDK installed
# https://vulkan.lunarg.com/sdk/home

cmake -B build -DGGML_VULKAN=1
cmake --build build -j --config Release
```

##### Intel GPUs (OpenVINO)

```bash
# Prerequisites: OpenVINO Toolkit installed
# https://github.com/openvinotoolkit/openvino/releases

# On Linux, source the setupvars script first:
source /path/to/openvino/setupvars.sh

# On Windows:
# C:\path\to\openvino\setupvars.bat

cmake -B build -DWHISPER_OPENVINO=1
cmake --build build -j --config Release
```

##### Apple Silicon (Core ML)

```bash
# Prerequisites:
# - Xcode Command Line Tools
# - Python 3.11 with:
#   pip install ane_transformers openai-whisper coremltools

# Generate Core ML model
./models/generate-coreml-model.sh base.en

# Build with Core ML
cmake -B build -DWHISPER_COREML=1
cmake --build build -j --config Release

# Optional: Allow CPU fallback if Core ML unavailable
cmake -B build -DWHISPER_COREML=1 -DWHISPER_COREML_ALLOW_FALLBACK=1
cmake --build build -j --config Release
```

##### CPU Acceleration (OpenBLAS)

```bash
# Prerequisites: OpenBLAS installed
# macOS: brew install openblas
# Linux: sudo apt install libopenblas-dev
# Windows: vcpkg install openblas:x64-windows

cmake -B build -DGGML_BLAS=1
cmake --build build -j --config Release
```

##### POWER Architecture (VSX)

```bash
# For POWER9/POWER10 systems
cmake -B build -DGGML_BLAS=1
cmake --build build -j --config Release
./build/bin/whisper-cli [...]
```

### Build Options Summary

| Option                     | Default | Purpose                          |
| -------------------------- | ------- | -------------------------------- |
| `WHISPER_COMMON_FFMPEG`    | OFF     | Extended audio format support    |
| `WHISPER_SDL2`             | OFF     | Real-time audio input            |
| `WHISPER_COREML`           | OFF     | Apple Neural Engine acceleration |
| `WHISPER_OPENVINO`         | OFF     | Intel GPU/CPU acceleration       |
| `GGML_CUDA`                | OFF     | NVIDIA GPU acceleration          |
| `GGML_HIP`                 | OFF     | AMD GPU acceleration             |
| `GGML_VULKAN`              | OFF     | Cross-vendor GPU support         |
| `GGML_BLAS`                | OFF     | CPU BLAS acceleration            |
| `WHISPER_BUILD_TESTS`      | ON      | Build test suite                 |
| `WHISPER_BUILD_EXAMPLES`   | ON      | Build example programs           |
| `WHISPER_BUILD_SERVER`     | ON      | Build HTTP server                |
| `WHISPER_SANITIZE_THREAD`  | OFF     | Thread sanitizer                 |
| `WHISPER_SANITIZE_ADDRESS` | OFF     | Address sanitizer                |

---

## Running Examples

### 1. Command-Line Interface (whisper-cli)

#### Basic Transcription

```bash
# Transcribe an audio file (English)
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

# Multilingual transcription (auto-detect language)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav

# Specify language explicitly
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -l en
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -l es
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -l fr
```

#### Performance Options

```bash
# Use multiple threads (default: automatic)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -t 4

# Maximum number of threads for your CPU (best for performance)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -t 8

# Single thread (useful for low-resource devices)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -t 1

# GPU processing (if compiled with GPU support)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -gpu
```

#### Output Formatting

```bash
# Print word-level timestamps (experimental)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -ml 1

# Limit line length to N characters
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -ml 50

# Print with confidence color-coding
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav --print-colors

# Output as JSON
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -j

# Output as SRT (subtitle format)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -srt

# Output as VTT (WebVTT format)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -vtt

# Output to file
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -of output.txt
```

#### Task Options

```bash
# Transcription (default) - convert speech to text
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav --no-timestamps

# Translation - translate audio to English
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -tr

# Automatic language detection
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav -l auto

# Detect language only (don't transcribe)
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav --detect-language
```

#### Help and Examples

```bash
# Full help message
./build/bin/whisper-cli -h

# Example: Transcribe multiple files
for file in samples/*.wav; do
    ./build/bin/whisper-cli -m models/ggml-base.bin -f "$file"
done
```

### 2. Real-Time Streaming (whisper-stream)

Requires SDL2 to be installed and compiled with `-DWHISPER_SDL2=ON`

```bash
# Prerequisites
cmake -B build -DWHISPER_SDL2=ON
cmake --build build -j --config Release

# Real-time transcription from microphone
./build/bin/whisper-stream -m models/ggml-base.en.bin

# With custom parameters
./build/bin/whisper-stream -m models/ggml-base.bin \
    -t 8 \
    --step 500 \
    --length 5000

# Options:
# -t N          : number of threads
# --step MS     : audio chunk size in milliseconds (default: 500)
# --length MS   : sliding window length (default: 5000)
```

### 3. Voice Command Recognition (whisper-command)

```bash
# Build the command example
cmake -B build -DWHISPER_BUILD_EXAMPLES=ON
cmake --build build -j --config Release

# Run command recognition
./build/bin/whisper-command -m models/ggml-base.en.bin -c samples/commands.txt

# Create commands.txt:
# add
# subtract
# multiply
# divide
```

### 4. HTTP Server (whisper-server)

```bash
# Prerequisites
cmake -B build -DWHISPER_BUILD_SERVER=ON
cmake --build build -j --config Release

# Start server
./build/bin/whisper-server -m models/ggml-base.bin --host 127.0.0.1 --port 8080

# Access the server
# Web UI: http://localhost:8080
# API: http://localhost:8080/inference

# REST API Example (Python)
import requests

response = requests.post(
    'http://localhost:8080/inference',
    files={'file': open('samples/jfk.wav', 'rb')},
    data={'language': 'en'}
)
print(response.json())

# REST API Example (cURL)
curl -X POST \
    -F "file=@samples/jfk.wav" \
    -F "language=en" \
    http://localhost:8080/inference
```

### 5. Model Quantization Tool

```bash
# Quantize models for smaller size and faster inference
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0

# Available methods:
# - q4_0: Smallest, fastest (4-bit)
# - q4_1: Good balance
# - q5_0: Recommended (5-bit)
# - q5_1: Best quality (5-bit)
# - q8_0: Near lossless (8-bit)

# Usage comparison
ls -lh models/ggml-base*
# Original: ~142 MB
# q5_0: ~50 MB (size reduction ~65%)
```

---

## Advanced Configuration

### Custom Audio Processing

#### Audio Format Conversion

```bash
# Convert any format to 16-bit WAV (required format)
ffmpeg -i audio.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
ffmpeg -i audio.m4a -ar 16000 -ac 1 -c:a pcm_s16le output.wav
ffmpeg -i audio.flac -ar 16000 -ac 1 -c:a pcm_s16le output.wav
ffmpeg -i audio.opus -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Batch conversion
for file in *.mp3; do
    ffmpeg -i "$file" -ar 16000 -ac 1 -c:a pcm_s16le "${file%.mp3}.wav"
done
```

### Using with Docker

```bash
# Pull image
docker pull ghcr.io/ggml-org/whisper.cpp:main

# Download model and persist it
docker run -it --rm \
  -v $(pwd)/models:/models \
  ghcr.io/ggml-org/whisper.cpp:main \
  "./models/download-ggml-model.sh base /models"

# Transcribe audio
docker run -it --rm \
  -v $(pwd)/models:/models \
  -v $(pwd)/audio:/audio \
  ghcr.io/ggml-org/whisper.cpp:main \
  "whisper-cli -m /models/ggml-base.bin -f /audio/sample.wav"

# Run web server
docker run -d -p 8080:8080 \
  -v $(pwd)/models:/models \
  ghcr.io/ggml-org/whisper.cpp:main \
  "whisper-server -m /models/ggml-base.bin --host 0.0.0.0"

# Available Docker images:
# ghcr.io/ggml-org/whisper.cpp:main          - CPU only
# ghcr.io/ggml-org/whisper.cpp:main-cuda     - NVIDIA GPU
# ghcr.io/ggml-org/whisper.cpp:main-vulkan   - Vulkan GPU
# ghcr.io/ggml-org/whisper.cpp:main-musa     - Moore Threads GPU
```

### Web Assembly (Browser-Based)

```bash
# Prerequisites:
# 1. Install Emscripten SDK
# 2. Download a small model (tiny.en recommended)

mkdir -p build-wasm
cd build-wasm

# Configure for WebAssembly
emcmake cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -j

# The JavaScript library will be in build-wasm/
# See examples/whisper.wasm/ for usage examples
```

### Core ML Support (Apple Silicon)

```bash
# Step 1: Generate Core ML model
pip install ane_transformers openai-whisper coremltools
./models/generate-coreml-model.sh base.en

# Step 2: Build with Core ML
cmake -B build -DWHISPER_COREML=1
cmake --build build -j --config Release

# Step 3: Run (automatically uses Core ML)
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

# Verify Core ML is loaded:
# Output should show: COREML = 1
```

### Language Settings

#### Supported Languages

Whisper supports 99 languages. Common ones:

```bash
# English
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l en

# Spanish
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l es

# French
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l fr

# German
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l de

# Japanese
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l ja

# Chinese (Simplified)
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l zh

# Russian
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l ru

# Arabic
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l ar

# Auto-detect language
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -l auto
```

---

## Language Bindings

### Go Binding

```bash
cd bindings/go
go mod tidy
go build
```

### Java Binding

```bash
cd bindings/java
./mvnw clean install

# Use in your Java project:
# Add dependency to pom.xml and use:
// initialization
WhisperCppJNI whisper = new WhisperCppJNI();
whisper.loadModel("models/ggml-base.bin");

// transcription
String result = whisper.transcribe("audio.wav");
```

### JavaScript Binding

```bash
cd bindings/javascript
npm install

# Use in Node.js or browser:
const Whisper = require('whisper.cpp');
const whisper = new Whisper('models/ggml-base.bin');
whisper.transcribe('audio.wav').then(result => console.log(result));
```

### Ruby Binding

```bash
cd bindings/ruby
gem install whisper_cpp

# Use in Ruby:
require 'whisper_cpp'
whisper = WhisperCpp.new('models/ggml-base.bin')
result = whisper.transcribe('audio.wav')
puts result
```

### Python Integration

```python
# Direct interface example (compile as library)
import ctypes
import numpy as np

# Load the library
whisper = ctypes.CDLL('./build/libwhisper.so')

# Load model
ctx = whisper.whisper_init_from_file(b'models/ggml-base.bin')

# Read audio
audio = np.fromfile('audio.wav', dtype=np.float32)

# Run inference
whisper.whisper_full(ctx, params, audio, len(audio))

# Get results
n_segments = whisper.whisper_full_n_segments(ctx)
for i in range(n_segments):
    text = whisper.whisper_full_get_segment_text(ctx, i)
    print(text.decode())
```

---

## Performance & Optimization

### CPU Performance Optimization

```bash
# 1. Use quantized models
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0
./build/bin/whisper-cli -m models/ggml-base-q5_0.bin -f audio.wav

# 2. Match thread count to CPU cores
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t $(nproc)

# 3. Use smaller model for speed
./build/bin/whisper-cli -m models/ggml-tiny.bin -f audio.wav

# 4. Disable timestamps if not needed
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav --no-timestamps
```

### GPU Performance Tips

```bash
# 1. Verify GPU is being used
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu
# Check output for GPU initialization messages

# 2. Use GPU with appropriate thread count
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu -t 4

# 3. Use CUDA for NVIDIA (most optimized)
# Build with: -DGGML_CUDA=1

# 4. Use Metal for Apple Silicon (most optimized)
# Automatically used on macOS with Apple Silicon
```

### Memory Usage by Model

| Model          | Disk   | Peak RAM | Optimal Use            |
| -------------- | ------ | -------- | ---------------------- |
| tiny.en        | 75 MB  | 273 MB   | IoT, edge devices      |
| base.en        | 142 MB | 388 MB   | Mobile devices         |
| small          | 466 MB | 852 MB   | Regular computers      |
| medium         | 1.5 GB | 2.1 GB   | Servers, high-end      |
| large-v3       | 2.9 GB | 3.9 GB   | Best quality scenarios |
| large-v3-turbo | 1.5 GB | 2.1 GB   | Balance (recommended)  |

### Benchmarking

```bash
# Build benchmark tool
cmake -B build -DWHISPER_BUILD_EXAMPLES=ON
cmake --build build -j

# Run benchmark on all samples
./build/bin/whisper-bench -m models/ggml-base.bin

# Run benchmark with specific thread count
./build/bin/whisper-bench -m models/ggml-base.bin -t 8

# Benchmark on a specific audio file
./build/bin/whisper-bench -m models/ggml-base.bin -f samples/jfk.wav
```

---

## Troubleshooting

### Common Issues & Solutions

#### 1. "Model not found" Error

```bash
# Problem: whisper-cli cannot find the model

# Solution 1: Check if model exists
ls -lh models/

# Solution 2: Download the model
sh ./models/download-ggml-model.sh base.en

# Solution 3: Use absolute path
./build/bin/whisper-cli -m /full/path/to/models/ggml-base.en.bin -f audio.wav

# Solution 4: Check file permissions
chmod +r models/ggml-base.en.bin
```

#### 2. Build Fails with CUDA Error

```bash
# Problem: CMake cannot find CUDA

# Solution 1: Verify CUDA installation
nvcc --version
nvidia-smi

# Solution 2: Set CUDA path explicitly
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_COMPILER=/path/to/nvcc
cmake --build build -j

# Solution 3: Clear CMake cache and rebuild
rm -rf build/
cmake -B build -DGGML_CUDA=1
cmake --build build -j
```

#### 3. Audio File Issues

```bash
# Problem: "Failed to read audio" or "Invalid audio format"

# Solution 1: Verify audio format
file audio.wav

# Solution 2: Convert to correct format
ffmpeg -i audio.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav

# Solution 3: Check audio sample rate
ffmpeg -i audio.wav
# Should show: Sample rate: 16000 Hz

# Solution 4: Verify mono audio
ffmpeg -i audio.wav
# Should show: 1 channel (mono)
```

#### 4. Slow Performance

```bash
# Problem: Transcription is very slow

# Solution 1: Check if GPU is enabled
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu

# Solution 2: Use faster model
./build/bin/whisper-cli -m models/ggml-tiny.bin -f audio.wav

# Solution 3: Use quantized model
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0
./build/bin/whisper-cli -m models/ggml-base-q5_0.bin -f audio.wav

# Solution 4: Increase threads (if CPU)
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t 8

# Solution 5: Use Raspberry Pi optimized build
# Compile on the Raspberry Pi or cross-compile with ARM flags
```

#### 5. Out of Memory Error

```bash
# Problem: "Cannot allocate memory" or "OOM killer"

# Solution 1: Use smaller model
./build/bin/whisper-cli -m models/ggml-tiny.bin -f audio.wav

# Solution 2: Use quantized model
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0
./build/bin/whisper-cli -m models/ggml-base-q5_0.bin -f audio.wav

# Solution 3: Reduce thread count
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t 1

# Solution 4: Check available memory
free -h  # Linux
vm_stat  # macOS
Get-ComputerInfo | Select-Object CsPhyicallyInstalledMemory  # Windows
```

#### 6. Compilation Errors

```bash
# Problem: "Compiler not found" or "No C++ compiler"

# Solution 1: Install build tools
# macOS:
xcode-select --install

# Linux (Ubuntu/Debian):
sudo apt install build-essential cmake

# Linux (Fedora):
sudo dnf install gcc-c++ cmake

# Windows:
# Download Visual Studio 2019+ with C++ workload

# Solution 2: Specify compiler explicitly
cmake -B build -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++
cmake --build build -j
```

#### 7. GPU Not Detected

```bash
# Problem: GPU compilation succeeds but GPU is not used

# For NVIDIA:
# 1. Verify CUDA availability
nvcc --version
nvidia-smi

# 2. Check if built with CUDA
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav | grep CUDA
# Should show: CUDA = 1

# For AMD ROCm:
# 1. Verify ROCm installation
rocm-smi

# 2. Check architecture match
rocminfo | grep "gfx"

# For Vulkan:
# 1. Verify Vulkan drivers
vulkaninfo

# 2. Clear cache and rebuild
rm -rf build/
cmake -B build -DGGML_VULKAN=1
cmake --build build -j
```

### Getting Help

```bash
# Check help for command-line tool
./build/bin/whisper-cli -h

# Check system capabilities
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav 2>&1 | grep -E "system_info|CUDA|METAL|VULKAN"

# Enable verbose logging
WHISPER_DEBUG=1 ./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav

# Report issues
# GitHub: https://github.com/ggml-org/whisper.cpp/issues
# Include: OS, hardware, build command, error message, model used
```

---

## Version Information

### Project Versions

- **Current Stable**: 1.8.6
- **Release Cycle**: Regular updates and patches
- **Breaking Changes**: Managed carefully, documented in CHANGELOG

### Component Versions

- **GGML**: Embedded (latest compatible version)
- **OpenAI Whisper Models**: Based on official releases
- **CMake**: Requires 3.5+
- **C++ Standard**: C++11 minimum (C++17 for WASM)

### Supported OpenAI Model Versions

- Whisper v2 (current, all sizes)
- Whisper v1 (legacy support)
- Custom converted models (via conversion script)

---

## Quick Reference Commands

```bash
# Clone
git clone https://github.com/ggml-org/whisper.cpp.git && cd whisper.cpp

# Download model
sh ./models/download-ggml-model.sh base.en

# Build
cmake -B build && cmake --build build -j --config Release

# Transcribe
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

# Server
./build/bin/whisper-server -m models/ggml-base.bin --port 8080

# Quantize
./build/bin/quantize models/ggml-base.bin models/ggml-base-q5_0.bin q5_0

# Real-time
./build/bin/whisper-stream -m models/ggml-base.en.bin

# With GPU
cmake -B build -DGGML_CUDA=1 && cmake --build build -j && ./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu
```

---

## Additional Resources

- **GitHub Repository**: https://github.com/ggml-org/whisper.cpp
- **Issues & Discussions**: https://github.com/ggml-org/whisper.cpp/issues
- **GGML Library**: https://github.com/ggml-org/ggml
- **OpenAI Whisper**: https://github.com/openai/whisper
- **Model Downloads**: https://huggingface.co/ggerganov/whisper.cpp

---

**Last Updated**: 2026-06-16  
**Documentation Version**: 1.0
