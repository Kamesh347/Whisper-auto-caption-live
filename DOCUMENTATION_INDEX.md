# Whisper.cpp Project Documentation Summary

**Generated**: 2026-06-16  
**Project Version**: 1.8.6 (Stable)  
**Repository**: https://github.com/ggml-org/whisper.cpp

---

## 📋 Documentation Files Created

This comprehensive guide includes four detailed documentation files:

### 1. **COMPLETE_GUIDE.md** (Main Reference)

**The most comprehensive guide covering everything**

- 🎯 Project objectives and goals
- 🏗️ Architecture and components overview
- 🌍 Supported platforms and features
- 📦 Step-by-step installation instructions
- 🏃 How to run with detailed examples
- 🔧 Build configurations for all scenarios
- 🚀 Advanced optimization techniques
- 🌐 Language bindings and integrations
- 📊 Performance specifications
- 🐛 Troubleshooting guide

**Best for**: Deep learning and complete reference

---

### 2. **QUICK_REFERENCE.md** (Fast Lookup)

**Concise commands and quick solutions**

- ⚡ 5-minute quick start
- 📈 Model selection guide
- 🔨 Common build commands
- 💻 Frequently used commands
- 🎵 Audio format conversion
- 🌐 Server and API usage
- 🔄 Real-time transcription
- 📉 Troubleshooting quick fixes
- 🧬 One-liner recipes

**Best for**: Quick lookup when you know what you need

---

### 3. **TECHNICAL_REFERENCE.md** (Detailed Specs)

**Technical specifications and matrices**

- 📊 Model specifications and sizes
- 💾 Memory requirements matrix
- 🏗️ Build configuration matrix
- 🖥️ GPU backend comparison
- 📱 Platform support matrix
- 🔧 Compiler requirements
- 📦 Dependency matrix
- ⚡ Performance specifications
- 🔌 API reference
- 🌍 Environment variables

**Best for**: System configuration and technical details

---

### 4. **README.md (Original)**

**Already available with general overview**

- Project introduction
- Quick start guide
- Existing examples and features

---

## 🎯 Project Objectives

### Primary Goals

1. **High Performance**: Enable fast speech recognition on consumer hardware
2. **Lightweight**: Minimal dependencies, zero runtime allocations
3. **Cross-Platform**: Support all major operating systems
4. **Privacy**: On-device inference without cloud connectivity
5. **Accessibility**: Easy integration into applications

### Core Capabilities

- ✅ Speech-to-text transcription
- ✅ Multi-language support (99 languages)
- ✅ GPU acceleration (NVIDIA, AMD, Intel, Apple)
- ✅ Real-time streaming
- ✅ Word-level timestamps
- ✅ Language detection
- ✅ Speech translation to English
- ✅ Confidence scoring

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone repository
git clone https://github.com/ggml-org/whisper.cpp.git && cd whisper.cpp

# 2. Download model (142 MB, good balance)
sh ./models/download-ggml-model.sh base.en

# 3. Build
cmake -B build && cmake --build build -j

# 4. Download sample audio
wget https://cdn.openai.com/whisper/draft-20220913a/jfk.wav -O samples/jfk.wav

# 5. Transcribe
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav
```

---

## 📊 Model Overview

| Model        | Size   | Speed      | Quality    | Language | Use Case     |
| ------------ | ------ | ---------- | ---------- | -------- | ------------ |
| **tiny**     | 75 MB  | ⚡⚡⚡⚡⚡ | ⭐         | Multi    | Mobile/IoT   |
| **base**     | 142 MB | ⚡⚡⚡⚡   | ⭐⭐       | Multi    | General use  |
| **small**    | 466 MB | ⚡⚡⚡     | ⭐⭐⭐     | Multi    | Desktop      |
| **medium**   | 1.5 GB | ⚡⚡       | ⭐⭐⭐⭐   | Multi    | Servers      |
| **large-v3** | 2.9 GB | ⚡         | ⭐⭐⭐⭐⭐ | Multi    | Best quality |

---

## 🏗️ Architecture Summary

### Model Structure

```
Input (16 kHz Audio)
    ↓
Mel-Spectrogram (80 frequencies)
    ↓
Encoder (12-26 layers)
    ↓
Decoder (12-26 layers) + Language token
    ↓
Output (Text tokens → UTF-8 text)
```

### Core Components

- **whisper.h**: Main C API interface
- **whisper.cpp**: Implementation
- **GGML**: Embedded ML library
- **Examples**: CLI, server, streaming
- **Bindings**: Go, Java, JavaScript, Ruby

---

## 🛠️ Build Scenarios

### Basic CPU Build

```bash
cmake -B build && cmake --build build -j
```

### NVIDIA GPU (CUDA)

```bash
cmake -B build -DGGML_CUDA=1 && cmake --build build -j
```

### AMD GPU (ROCm)

```bash
cmake -B build -DGGML_HIP=1 -DAMDGPU_TARGETS="gfx1100" && cmake --build build -j
```

### Apple Silicon (Metal)

```bash
cmake -B build && cmake --build build -j
# Metal automatically enabled on Apple Silicon
```

### Intel GPU (OpenVINO)

```bash
cmake -B build -DWHISPER_OPENVINO=1 && cmake --build build -j
```

### Cross-Vendor (Vulkan)

```bash
cmake -B build -DGGML_VULKAN=1 && cmake --build build -j
```

---

## 📱 Supported Platforms

| Platform          | Status | Special Features    |
| ----------------- | ------ | ------------------- |
| **macOS (Intel)** | ✅     | Full SIMD           |
| **macOS (ARM64)** | ✅     | Metal, Core ML      |
| **iOS**           | ✅     | whisper.objc SDK    |
| **Android**       | ✅     | whisper.android SDK |
| **Linux**         | ✅     | All architectures   |
| **Windows**       | ✅     | MSVC compatible     |
| **Raspberry Pi**  | ✅     | NEON optimized      |
| **WebAssembly**   | ✅     | Browser-based       |
| **Docker**        | ✅     | Official images     |

---

## 💻 Common Commands

```bash
# Basic transcription (English only)
./build/bin/whisper-cli -m models/ggml-base.en.bin -f audio.wav

# Auto-detect language
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav

# With GPU acceleration
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu

# With multiple threads
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -t 8

# Output as JSON
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -j

# Output as SRT (subtitles)
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -srt

# Real-time from microphone
./build/bin/whisper-stream -m models/ggml-base.en.bin

# HTTP server
./build/bin/whisper-server -m models/ggml-base.bin --port 8080
```

---

## 🔊 Audio Format Support

### Native Format

- **16 kHz, mono, 16-bit PCM** (required)

### With FFmpeg

```bash
# Convert any format to required format
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

### Supported Formats (with FFmpeg)

- MP3, AAC, FLAC, OGG, OPUS, ALAC, WMA, WAV

---

## ⚡ Performance Metrics

### Approximate Inference Speed

| Model  | CPU (8 threads) | GPU (RTX 3090) |
| ------ | --------------- | -------------- |
| tiny   | 1.0x RT         | 0.15x RT       |
| base   | 0.6x RT         | 0.08x RT       |
| small  | 0.2x RT         | 0.05x RT       |
| medium | 0.1x RT         | 0.02x RT       |
| large  | 0.03x RT        | 0.01x RT       |

**RT** = Real-time (1.0x = processes audio as fast as it plays)

### Memory Usage

| Model  | Peak RAM |
| ------ | -------- |
| tiny   | 273 MB   |
| base   | 388 MB   |
| small  | 852 MB   |
| medium | 2.1 GB   |
| large  | 3.9 GB   |

---

## 🌍 Language Support

**99 Languages Supported Including:**

- English, Spanish, French, German, Italian, Portuguese
- Russian, Polish, Czech, Slovak, Bulgarian
- Japanese, Chinese (Simplified/Traditional), Korean, Vietnamese
- Arabic, Hebrew, Persian, Turkish
- Hindi, Bengali, Tamil, Telugu
- And 80+ more languages

---

## 📚 Documentation Map

| File                       | Purpose                 | Best For             |
| -------------------------- | ----------------------- | -------------------- |
| **COMPLETE_GUIDE.md**      | Comprehensive reference | Deep learning        |
| **QUICK_REFERENCE.md**     | Fast commands lookup    | Quick solutions      |
| **TECHNICAL_REFERENCE.md** | Specifications matrix   | Technical details    |
| **README.md**              | Project overview        | Getting started      |
| **CONTRIBUTING.md**        | Contribution guidelines | Contributing code    |
| **AGENTS.md**              | AI usage policy         | Contributing with AI |

---

## 🔧 Installation Checklist

- [ ] Clone repository: `git clone https://github.com/ggml-org/whisper.cpp.git`
- [ ] Download model: `sh ./models/download-ggml-model.sh base.en`
- [ ] Install CMake (3.5+)
- [ ] Install C++ compiler (GCC, Clang, or MSVC)
- [ ] Build: `cmake -B build && cmake --build build -j`
- [ ] Test: `./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav`

---

## 🚨 Common Issues & Solutions

| Issue                  | Solution                                                                 |
| ---------------------- | ------------------------------------------------------------------------ |
| "Model not found"      | Run: `sh ./models/download-ggml-model.sh base.en`                        |
| "Failed to read audio" | Convert: `ffmpeg -i audio.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav` |
| Slow performance       | Use GPU: `cmake -B build -DGGML_CUDA=1` or smaller model                 |
| Out of memory          | Use smaller model (tiny/base) or quantized version                       |
| Build fails            | Update compiler: `gcc --version` (should be 5.0+)                        |

---

## 🎓 Learning Path

1. **Start**: Read QUICK_REFERENCE.md for quick commands
2. **Explore**: Run basic transcription examples
3. **Learn**: Read COMPLETE_GUIDE.md sections as needed
4. **Reference**: Use TECHNICAL_REFERENCE.md for specifications
5. **Optimize**: Apply performance tips from COMPLETE_GUIDE.md
6. **Integrate**: Use language bindings for your application

---

## 📦 Project Statistics

| Metric                | Value                             |
| --------------------- | --------------------------------- |
| **Version**           | 1.8.6 (Stable)                    |
| **License**           | MIT (Free)                        |
| **Models**            | 12 sizes                          |
| **Languages**         | 99 supported                      |
| **GPU Backends**      | 8+ (CUDA, Metal, Vulkan, etc.)    |
| **CPU Platforms**     | 10+ (Linux, macOS, Windows, etc.) |
| **Language Bindings** | 4 (Go, Java, JavaScript, Ruby)    |
| **Code Size**         | ~15 MB source                     |

---

## 🔗 Resources

- **GitHub**: https://github.com/ggml-org/whisper.cpp
- **Issues**: https://github.com/ggml-org/whisper.cpp/issues
- **Models**: https://huggingface.co/ggerganov/whisper.cpp
- **GGML**: https://github.com/ggml-org/ggml
- **Whisper**: https://github.com/openai/whisper

---

## 📖 Which Document Should I Read?

### I want to...

**Get started quickly**
→ Start with **QUICK_REFERENCE.md**

**Understand everything deeply**
→ Read **COMPLETE_GUIDE.md**

**Find technical specifications**
→ Check **TECHNICAL_REFERENCE.md**

**Configure GPU support**
→ See GPU Backend Matrix in **TECHNICAL_REFERENCE.md**

**Troubleshoot build issues**
→ Go to "Troubleshooting" section in **COMPLETE_GUIDE.md**

**Find a specific command**
→ Search **QUICK_REFERENCE.md**

**Integrate into my app**
→ See "Language Bindings" in **COMPLETE_GUIDE.md**

---

## ✅ Verification

All four documentation files have been created and are ready for use:

```
✅ COMPLETE_GUIDE.md           (~50 KB)   - Full comprehensive guide
✅ QUICK_REFERENCE.md          (~30 KB)   - Quick command reference
✅ TECHNICAL_REFERENCE.md      (~40 KB)   - Technical specifications
✅ README.md                   (existing)  - Project overview
```

---

## 🎉 You Now Have

✨ **Complete Documentation** covering:

- ✅ Project objectives and goals
- ✅ Step-by-step installation (all platforms)
- ✅ How to run (all 5 modes + GPU variants)
- ✅ All 12 available models with specs
- ✅ All 8+ GPU backends
- ✅ All 10+ supported platforms
- ✅ 99 supported languages
- ✅ Build commands for every scenario
- ✅ Performance metrics and optimization tips
- ✅ Troubleshooting guide
- ✅ API reference
- ✅ Language bindings
- ✅ Docker support
- ✅ One-liner recipes

---

## 🚀 Next Steps

1. **Start Building**: `git clone https://github.com/ggml-org/whisper.cpp.git`
2. **Choose Model**: Based on your hardware and speed requirements
3. **Build**: Using appropriate configuration from documentation
4. **Test**: Run on sample audio files
5. **Deploy**: Integrate into your application

---

**Created**: 2026-06-16  
**Documentation Version**: 1.0  
**Status**: Complete and Ready to Use ✅

---

> **Note**: These comprehensive guides supplement the existing README.md and provide detailed information organized by use case and technical depth. Choose the guide that best matches your needs!
