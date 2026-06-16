# Whisper.cpp Technical Reference & System Information

**Version**: 1.8.6 (Stable)  
**Last Updated**: 2026-06-16  
**License**: MIT  
**Repository**: https://github.com/ggml-org/whisper.cpp

---

## Table of Contents

1. [Project Specifications](#project-specifications)
2. [Model Specifications](#model-specifications)
3. [Build Configurations](#build-configurations)
4. [GPU Backend Matrix](#gpu-backend-matrix)
5. [Platform Support Matrix](#platform-support-matrix)
6. [Compiler Requirements](#compiler-requirements)
7. [Dependency Matrix](#dependency-matrix)
8. [Performance Specifications](#performance-specifications)
9. [API Reference](#api-reference)
10. [Environment Variables](#environment-variables)

---

## Project Specifications

### Project Metadata

| Property            | Value                                    |
| ------------------- | ---------------------------------------- |
| **Name**            | whisper.cpp                              |
| **Current Version** | 1.8.6                                    |
| **Release Date**    | Latest stable                            |
| **License**         | MIT                                      |
| **Repository**      | github.com/ggml-org/whisper.cpp          |
| **Language**        | C/C++ (C++11 minimum)                    |
| **Primary API**     | C (C-style)                              |
| **Thread Safety**   | Single-context (not multi-threaded)      |
| **Memory Model**    | Stack-based, zero allocations at runtime |
| **SIMD Support**    | AVX, AVX2, NEON, VSX                     |
| **Model Format**    | GGML binary (.bin)                       |

### Key Capabilities

```
Speech Recognition:
├─ Task: Transcription (convert speech → text)
├─ Task: Translation (convert speech → English text)
├─ Task: Language Detection (identify input language)
└─ Task: Confidence Scoring (confidence per word)

Audio Processing:
├─ Sample Rate: 16 kHz (automatically resampled)
├─ Channel: Mono (1 channel, stereo converted)
├─ Format: PCM 16-bit or 32-bit float
├─ Duration: Unlimited (processed in chunks)
└─ Encoding: Multi-pass encoder-decoder architecture

Optimization:
├─ Precision: Mixed F16/F32
├─ Quantization: Q4_0, Q4_1, Q5_0, Q5_1, Q8_0
├─ Acceleration: GPU, SIMD, BLAS
└─ Memory: Zero allocations post-initialization
```

---

## Model Specifications

### Official OpenAI Whisper Models

#### Encoder-Decoder Architecture

```
Input: Audio (16 kHz PCM)
  ↓
Mel-spectrogram: 80 frequencies × time steps
  ↓
Encoder:
├─ Layer 1-12: Self-attention + feed-forward
├─ Positional encoding: Relative position bias
└─ Output: 1500 hidden state dim
  ↓
Decoder:
├─ Layer 1-12: Cross-attention to encoder
├─ Layer 1-12: Causal self-attention
└─ Output: Token probabilities
  ↓
Tokenizer: BPE with 50,257 vocabulary
  ↓
Output: Text tokens → UTF-8 text
```

### Model Sizes & Performance

| Model          | Parameters | Encoder Layers | Decoder Layers | Hidden Dim | Parameters    |
| -------------- | ---------- | -------------- | -------------- | ---------- | ------------- |
| tiny           | 39M        | 4              | 4              | 384        | 39,000,000    |
| base           | 74M        | 6              | 6              | 512        | 74,000,000    |
| small          | 244M       | 12             | 12             | 768        | 244,000,000   |
| medium         | 769M       | 24             | 24             | 1024       | 769,000,000   |
| large-v1/v2    | 1550M      | 26             | 26             | 1280       | 1,550,000,000 |
| large-v3       | 1550M      | 26             | 26             | 1280       | 1,550,000,000 |
| large-v3-turbo | 769M       | 24             | 24             | 1024       | 769,000,000   |

### Model Memory Requirements

| Model  | Disk   | FP32   | FP16   | Q8_0   | Q5_1   | Q5_0   | Q4_1   | Q4_0   |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| tiny   | 75 MB  | 146 MB | 73 MB  | 55 MB  | 50 MB  | 47 MB  | 44 MB  | 42 MB  |
| base   | 142 MB | 279 MB | 140 MB | 105 MB | 95 MB  | 89 MB  | 83 MB  | 79 MB  |
| small  | 466 MB | 917 MB | 458 MB | 344 MB | 312 MB | 293 MB | 273 MB | 260 MB |
| medium | 1.5 GB | 2.9 GB | 1.5 GB | 1.1 GB | 1.0 GB | 941 MB | 878 MB | 835 MB |
| large  | 2.9 GB | 5.8 GB | 2.9 GB | 2.2 GB | 2.0 GB | 1.9 GB | 1.7 GB | 1.6 GB |

### Model Download URLs

```
Base URL: https://huggingface.co/ggerganov/whisper.cpp/resolve/main/

Files:
- ggml-tiny.bin           (75 MB)
- ggml-tiny.en.bin        (75 MB)
- ggml-base.bin          (142 MB)
- ggml-base.en.bin       (142 MB)
- ggml-small.bin         (466 MB)
- ggml-small.en.bin      (466 MB)
- ggml-medium.bin        (1.5 GB)
- ggml-medium.en.bin     (1.5 GB)
- ggml-large-v1.bin      (2.9 GB)
- ggml-large-v2.bin      (2.9 GB)
- ggml-large-v3.bin      (2.9 GB)
- ggml-large-v3-turbo.bin (1.5 GB)

Speed (typical from Hugging Face):
- 4-10 MB/s on good connections
- ~20-45 seconds for base (142 MB)
- ~3-5 minutes for large (2.9 GB)
```

### Language Support Matrix

| Region             | Languages                                                        | Count  |
| ------------------ | ---------------------------------------------------------------- | ------ |
| **Romance**        | French, Spanish, Portuguese, Italian, Romanian                   | 5      |
| **Germanic**       | English, German, Dutch, Danish, Swedish                          | 5      |
| **Slavic**         | Russian, Polish, Czech, Slovak, Bulgarian                        | 5      |
| **Asian**          | Mandarin, Cantonese, Japanese, Korean, Vietnamese, Thai, Burmese | 8      |
| **Middle Eastern** | Arabic, Hebrew, Persian, Turkish                                 | 4      |
| **South Asian**    | Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Punjabi        | 7      |
| **African**        | Swahili, Zulu, Yoruba, Igbo, Hausa, Amharic                      | 6      |
| **Other**          | Greek, Hungarian, Finnish, Norwegian, Filipino, etc.             | 54     |
| **Total**          | **99 languages**                                                 | **99** |

---

## Build Configurations

### CMake Build Options

#### Core Build Options

```cmake
# Build type
-DCMAKE_BUILD_TYPE=Release      # Default: Release (optimized)
                                # Options: Debug, Release, RelWithDebInfo, MinSizeRel

# Shared vs Static
-DBUILD_SHARED_LIBS=ON          # Default: ON for Linux/macOS, OFF for Windows
                                # ON = .so/.dll, OFF = .a/.lib

# Installation prefix
-DCMAKE_INSTALL_PREFIX=/path    # Where to install after build
```

#### Feature Flags

```cmake
# Build components
-DWHISPER_BUILD_TESTS=ON        # Build test suite (default: ON in standalone)
-DWHISPER_BUILD_EXAMPLES=ON     # Build examples (default: ON in standalone)
-DWHISPER_BUILD_SERVER=ON       # Build HTTP server (default: ON in standalone)

# Warning levels
-DWHISPER_ALL_WARNINGS=ON       # Enable all warnings (default: ON)
-DWHISPER_FATAL_WARNINGS=OFF    # Treat warnings as errors (default: OFF)

# Code analysis
-DWHISPER_SANITIZE_THREAD=OFF   # Thread sanitizer
-DWHISPER_SANITIZE_ADDRESS=OFF  # Address sanitizer
-DWHISPER_SANITIZE_UNDEFINED=OFF # Undefined behavior sanitizer
```

#### GPU Support Options

```cmake
# NVIDIA CUDA
-DGGML_CUDA=1                   # Enable CUDA support
-DCMAKE_CUDA_ARCHITECTURES=75   # GPU architecture (compute capability)
                                # 70=V100, 75=RTX2000, 80=A100, 86=RTX4000, 89=RTX6000, 90=RTX5000

# AMD ROCm/HIP
-DGGML_HIP=1                    # Enable HIP support
-DAMDGPU_TARGETS=gfx1100        # GPU architecture
                                # gfx900=Radeon VII, gfx906=MI50, gfx1030=RX6800
                                # gfx1100=RX7900XTX, gfx1101=RX7800XT, gfx1201=RX9070XT

# Intel GPU/OpenVINO
-DWHISPER_OPENVINO=1            # Enable OpenVINO support

# Vulkan (cross-vendor)
-DGGML_VULKAN=1                 # Enable Vulkan support

# CPU acceleration
-DGGML_BLAS=1                   # Enable OpenBLAS acceleration
-DGGML_CANN=1                   # Enable Ascend NPU support
-DGGML_MUSA=1                   # Enable Moore Threads GPU support
```

#### Platform-Specific Options

```cmake
# macOS/iOS
-DWHISPER_COREML=1              # Apple Neural Engine acceleration
-DWHISPER_COREML_ALLOW_FALLBACK=1 # Allow CPU fallback if Core ML fails

# Web Assembly
-DEMSCRIPTEN=1                  # Auto-set by Emscripten SDK
-DWHISPER_WASM_SINGLE_FILE=ON   # Embed WASM in .js

# Windows
-DCMAKE_C_COMPILER=cl           # Use MSVC compiler
-DCMAKE_CXX_COMPILER=cl

# 3rd-party library support
-DWHISPER_COMMON_FFMPEG=ON      # FFmpeg for audio decoding
-DWHISPER_SDL2=ON               # SDL2 for real-time audio
-DWHISPER_CURL=ON               # libcurl for HTTP downloads
```

#### System Build Options

```cmake
# Use system libraries
-DWHISPER_USE_SYSTEM_GGML=OFF   # Use system-installed GGML (default: embed)

# C++ standard
-DCMAKE_CXX_STANDARD=17         # Default: 11
-DCMAKE_CXX_STANDARD_REQUIRED=ON

# Optimization flags
-DCMAKE_CXX_FLAGS_RELEASE="-O3 -march=native" # Custom optimization

# Link-time optimization
-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON # Enable LTO (slower build, better performance)
```

### Build Configuration Examples

```bash
# Minimal (CPU only, small binary)
cmake -B build -DCMAKE_BUILD_TYPE=MinSizeRel
cmake --build build -j

# Fast CPU (with optimization)
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-O3 -march=native"
cmake --build build -j

# NVIDIA GPU (with CUDA)
cmake -B build -DGGML_CUDA=1
cmake --build build -j

# Apple Metal (automatic on M1/M2/M3)
cmake -B build
cmake --build build -j

# Server deployment (static linking)
cmake -B build -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release
cmake --build build -j

# Debug build (with symbols, sanitizers)
cmake -B build -DCMAKE_BUILD_TYPE=Debug \
    -DWHISPER_SANITIZE_ADDRESS=ON \
    -DWHISPER_SANITIZE_UNDEFINED=ON
cmake --build build -j

# WebAssembly
emcmake cmake -B build-wasm -DCMAKE_BUILD_TYPE=Release
cmake --build build-wasm -j
```

---

## GPU Backend Matrix

### GPU Backend Comparison

| Backend           | Vendor        | Platforms      | Performance              | Status       | Build Flag             |
| ----------------- | ------------- | -------------- | ------------------------ | ------------ | ---------------------- |
| **Metal**         | Apple         | macOS, iOS     | ⭐⭐⭐⭐⭐ 3-5x faster   | ✅ Mature    | Auto-detected          |
| **Core ML (ANE)** | Apple Silicon | M1/M2/M3       | ⭐⭐⭐⭐⭐ 5-10x faster  | ✅ Mature    | `-DWHISPER_COREML=1`   |
| **CUDA**          | NVIDIA        | Linux, Windows | ⭐⭐⭐⭐⭐ 10-50x faster | ✅ Mature    | `-DGGML_CUDA=1`        |
| **HIP (ROCm)**    | AMD           | Linux          | ⭐⭐⭐⭐ 8-40x faster    | ✅ Mature    | `-DGGML_HIP=1`         |
| **Vulkan**        | Cross-vendor  | Linux, Windows | ⭐⭐⭐⭐ 5-30x faster    | ✅ Stable    | `-DGGML_VULKAN=1`      |
| **OpenVINO**      | Intel         | Linux, Windows | ⭐⭐⭐⭐ 5-20x faster    | ✅ Mature    | `-DWHISPER_OPENVINO=1` |
| **CANN**          | Huawei/Ascend | Linux          | ⭐⭐⭐⭐ 10-30x faster   | ✅ Supported | `-DGGML_CANN=1`        |
| **MUSA**          | Moore Threads | Linux          | ⭐⭐⭐ 5-15x faster      | ✅ Supported | `-DGGML_MUSA=1`        |
| **OpenBLAS**      | CPU           | All            | ⭐⭐ 2-3x faster         | ✅ Supported | `-DGGML_BLAS=1`        |

### CUDA Architecture Versions

| Architecture | Compute Capability | GPUs                      | Build Flag |
| ------------ | ------------------ | ------------------------- | ---------- |
| Turing       | 7.5                | RTX 2000 series, GTX 1600 | `75`       |
| Ampere       | 8.0                | RTX 3000 series           | `80`       |
| Ampere       | 8.6                | RTX 4000 series           | `86`       |
| Ampere       | 8.7                | RTX A series              | `87`       |
| Ada Lovelace | 8.9                | RTX 5000 series           | `89`       |
| Hopper       | 9.0                | H100, H200                | `90`       |

### ROCm GPU Architectures

| Architecture | GPU                     | Build Code               |
| ------------ | ----------------------- | ------------------------ |
| RDNA1        | RX 5000 series          | `gfx1010`                |
| RDNA2        | RX 6000 series, RX 6800 | `gfx1030`                |
| RDNA3        | RX 7000 series          | `gfx1100`, `gfx1101`     |
| RDNA4        | RX 9000 series          | `gfx1201`                |
| MI series    | MI100/200/300           | `gfx908`, `gfx90a`, etc. |

---

## Platform Support Matrix

### Operating System Support

| OS               | Version | Architecture          | Status             | Notes                       |
| ---------------- | ------- | --------------------- | ------------------ | --------------------------- |
| **macOS**        | 10.13+  | Intel                 | ✅ Supported       | Full SIMD support           |
| **macOS**        | 11.0+   | Apple Silicon (ARM64) | ✅ Optimized       | Metal/Core ML acceleration  |
| **iOS**          | 14.0+   | ARM64                 | ✅ Supported       | See whisper.objc example    |
| **iPadOS**       | 14.0+   | ARM64                 | ✅ Supported       | Same as iOS                 |
| **Linux**        | Any     | x86-64                | ✅ Fully Supported | All distributions           |
| **Linux**        | Any     | ARM64                 | ✅ Supported       | Raspberry Pi 4, etc.        |
| **Linux**        | Any     | ARMv7                 | ✅ Supported       | Older Raspberry Pi          |
| **Windows**      | 7+      | x86-64                | ✅ Supported       | MSVC and MinGW              |
| **FreeBSD**      | 12+     | x86-64                | ✅ Supported       | Community tested            |
| **Android**      | 21+     | ARM64                 | ✅ Supported       | See whisper.android example |
| **WebAssembly**  | -       | WASM                  | ✅ Supported       | Browser-based inference     |
| **Raspberry Pi** | Any     | ARMv7/ARM64           | ✅ Supported       | Optimized NEON              |
| **Docker**       | Any     | x86-64, ARM64         | ✅ Supported       | Official images available   |

### Raspberry Pi Versions

| Model  | CPU           | RAM    | GPU          | Status       |
| ------ | ------------- | ------ | ------------ | ------------ |
| Zero W | ARMv6         | 512 MB | None         | ⚠️ Limited   |
| 3B+    | ARMv8 1.4 GHz | 1 GB   | None         | ✅ Supported |
| 4B     | ARMv8 1.5 GHz | 2-8 GB | VideoCore VI | ✅ Optimized |
| 5      | ARMv8 2.4 GHz | 4-8 GB | None         | ✅ Optimized |
| 400    | ARMv8 2.3 GHz | 4 GB   | None         | ✅ Optimized |

---

## Compiler Requirements

### Compiler Versions

| Compiler         | Minimum | Recommended | Status             |
| ---------------- | ------- | ----------- | ------------------ |
| **GCC**          | 5.0     | 11+, 12+    | ✅ Fully Supported |
| **Clang**        | 3.8     | 14+, 15+    | ✅ Fully Supported |
| **MSVC**         | 2015    | 2019, 2022  | ✅ Fully Supported |
| **Emscripten**   | 2.0     | 3.1+        | ✅ Supported       |
| **Apple Clang**  | 11      | 14+         | ✅ Fully Supported |
| **ICC**          | 2019    | 2021+       | ✅ Supported       |
| **ARM Compiler** | 6.0     | 6.15+       | ✅ Supported       |

### C/C++ Standard Support

| Standard | Status           | Usage                  |
| -------- | ---------------- | ---------------------- |
| C++98    | ❌ Not supported | Too old                |
| C++03    | ❌ Not supported | Too old                |
| C++11    | ✅ Minimum       | Base requirement       |
| C++14    | ✅ Supported     | Preferred              |
| C++17    | ✅ Supported     | WebAssembly (WASM)     |
| C++20    | ⚠️ Partial       | Some advanced features |

---

## Dependency Matrix

### Required Dependencies

| Dependency   | Category | Linux        | macOS          | Windows     | Usage              |
| ------------ | -------- | ------------ | -------------- | ----------- | ------------------ |
| CMake        | Build    | ✅ 3.5+      | ✅ 3.5+        | ✅ 3.5+     | Build system       |
| C++ Compiler | Build    | ✅ GCC/Clang | ✅ Apple Clang | ✅ MSVC     | Compilation        |
| Make         | Build    | ✅ Optional  | ✅ Optional    | ✅ Optional | Quick builds       |
| Git          | Tools    | ✅           | ✅             | ✅          | Repository cloning |

### Optional Dependencies

| Package          | Purpose                | Platforms             | Installation                                               |
| ---------------- | ---------------------- | --------------------- | ---------------------------------------------------------- |
| **FFmpeg**       | Extended audio formats | Linux, macOS, Windows | `apt install libavcodec-dev`, `brew install ffmpeg`, vcpkg |
| **SDL2**         | Real-time audio input  | Linux, macOS, Windows | `apt install libsdl2-dev`, `brew install sdl2`             |
| **CUDA Toolkit** | NVIDIA GPU support     | Linux, Windows        | https://developer.nvidia.com/cuda-downloads                |
| **ROCm**         | AMD GPU support        | Linux                 | https://rocm.docs.amd.com                                  |
| **Vulkan SDK**   | Cross-vendor GPU       | Linux, Windows        | https://vulkan.lunarg.com/sdk                              |
| **OpenVINO**     | Intel GPU/CPU          | Linux, Windows        | https://github.com/openvinotoolkit/openvino                |
| **CANN**         | Ascend NPU             | Linux                 | https://www.hiascend.com/software/cann                     |
| **libcurl**      | HTTP downloads         | All                   | System package or vcpkg                                    |
| **OpenBLAS**     | CPU acceleration       | All                   | `apt install libopenblas-dev`, `brew install openblas`     |

### Development Tools

| Tool             | Purpose                     |
| ---------------- | --------------------------- |
| Python 3.11      | Core ML model conversion    |
| pip              | Package installation        |
| ane_transformers | Apple Neural Engine support |
| openai-whisper   | Reference implementation    |
| coremltools      | Core ML model generation    |

---

## Performance Specifications

### Inference Speed (Approximate)

Real-world performance on Intel i7-11700K, 16 GB RAM, no GPU:

| Model  | 1 Thread | 8 Threads | RTX 3090 | Notes        |
| ------ | -------- | --------- | -------- | ------------ |
| tiny   | 7x RT    | 1.0x RT   | 0.15x RT | ~50ms/sec    |
| base   | 4x RT    | 0.6x RT   | 0.08x RT | ~170ms/sec   |
| small  | 1.5x RT  | 0.2x RT   | 0.05x RT | ~6sec/min    |
| medium | 0.5x RT  | 0.1x RT   | 0.02x RT | ~200sec/min  |
| large  | 0.2x RT  | 0.03x RT  | 0.01x RT | ~1000sec/min |

### Explanation

- **RT** = Real-time (1.0x = same as duration of audio)
- Example: tiny model on single thread: 7x RT = processes 7 seconds of audio per 1 second
- **RTX 3090**: Typical NVIDIA flagship GPU acceleration

### Memory Usage During Inference

| Model  | Peak Memory | Notes                           |
| ------ | ----------- | ------------------------------- |
| tiny   | 273 MB      | RAM for inference only          |
| base   | 388 MB      | ~400 MB typical                 |
| small  | 852 MB      | ~850 MB typical                 |
| medium | 2.1 GB      | Requires modern PC              |
| large  | 3.9 GB      | Requires high-end GPU for speed |

### Audio Processing Specifications

```
Input Audio Format:
  Sample Rate: 16,000 Hz (auto-resampled if different)
  Bit Depth: 16-bit PCM or 32-bit float
  Channels: 1 (mono) - stereo converted to mono
  Duration: Unlimited (processed in 30-second chunks)
  Encoding: Linear PCM, µ-law, A-law supported

Output:
  Text Encoding: UTF-8
  Timestamps: Start→End (millisecond precision)
  Tokens: BPE with 50,257 vocabulary
  Confidence: 0.0-1.0 per word (if requested)

Processing Pipeline:
  1. Resampling (if not 16 kHz)
  2. Mono conversion (if stereo)
  3. Windowing (30-second chunks with overlap)
  4. Mel-spectrogram generation (80 frequency bins)
  5. Encoder inference
  6. Decoder inference
  7. Post-processing (confidence scoring, timestamps)
```

### Quantization Impact

Relative performance/size compared to original FP32:

| Method | Size | Speed | Quality Loss |
| ------ | ---- | ----- | ------------ |
| FP32   | 100% | 100%  | -            |
| FP16   | 50%  | 100%  | Negligible   |
| Q8_0   | 25%  | 105%  | <1%          |
| Q5_1   | 20%  | 110%  | 1-2%         |
| Q5_0   | 19%  | 115%  | 1-2%         |
| Q4_1   | 16%  | 125%  | 2-3%         |
| Q4_0   | 15%  | 135%  | 3-5%         |

---

## API Reference

### Core C API Functions

#### Initialization

```c
// Create context from file
struct whisper_context * ctx = whisper_init_from_file("/path/to/model.bin");

// Create with parameters
whisper_context_params cparams = whisper_context_default_params();
cparams.use_gpu = true;
struct whisper_context * ctx = whisper_init_from_file_with_params(path, cparams);

// Cleanup
whisper_free(ctx);
```

#### Inference

```c
// Full inference
whisper_full_params wparams = whisper_full_default_params(WHISPER_SAMPLING_GREEDY);
wparams.n_threads = 4;
wparams.language = "en";
wparams.print_progress = false;
wparams.print_realtime = true;
whisper_full(ctx, wparams, samples, n_samples);

// Get results
int n_segments = whisper_full_n_segments(ctx);
for (int i = 0; i < n_segments; ++i) {
    const char * text = whisper_full_get_segment_text(ctx, i);
    int64_t t0 = whisper_full_get_segment_t0(ctx, i);
    int64_t t1 = whisper_full_get_segment_t1(ctx, i);
}
```

#### Language Detection

```c
// Detect language
const char * lang = whisper_lang_str(whisper_full_lang_id(ctx));

// Get detected language probability
float probability = whisper_full_get_lang_probs(ctx)[lang_id];
```

#### System Information

```c
// Get system info
whisper_print_system_info();

// Get model info
const char * desc = whisper_model_desc(ctx);
```

### Full API Functions List

```
Initialization:
  whisper_init_from_file()
  whisper_init_from_file_with_params()
  whisper_init_from_buffer()
  whisper_free()

Context Parameters:
  whisper_context_default_params()
  whisper_context_params.use_gpu
  whisper_context_params.gpu_device

Full Inference:
  whisper_full()
  whisper_full_parallel()
  whisper_full_with_state()

Results Access:
  whisper_full_n_segments()
  whisper_full_get_segment_text()
  whisper_full_get_segment_t0()
  whisper_full_get_segment_t1()
  whisper_full_get_token_data()
  whisper_full_get_token_p()

Language:
  whisper_lang_str()
  whisper_lang_id()
  whisper_full_lang_id()
  whisper_full_get_lang_probs()

Model Information:
  whisper_model_desc()
  whisper_n_vocab()
  whisper_token_eot()

Sampling Strategies:
  WHISPER_SAMPLING_GREEDY
  WHISPER_SAMPLING_BEAM_SEARCH

System:
  whisper_print_system_info()
  whisper_free_params()
  whisper_free_context()
```

---

## Environment Variables

### Runtime Environment Variables

```bash
# Debugging
WHISPER_DEBUG=1                 # Enable debug logging
WHISPER_LOG_LEVEL=DEBUG         # Set log level

# GPU Control
CUDA_VISIBLE_DEVICES=0          # CUDA: use GPU 0
CUDA_VISIBLE_DEVICES=0,1        # CUDA: use GPUs 0 and 1
CUDA_LAUNCH_BLOCKING=1          # CUDA: synchronous execution (slower, easier debug)
HIP_VISIBLE_DEVICES=0           # ROCm: use GPU 0
ROCR_VISIBLE_DEVICES=0          # ROCm: alternative setting

# Performance Tuning
OMP_NUM_THREADS=8               # OpenMP threads (if using BLAS)
MKL_NUM_THREADS=8               # MKL threads (if using Intel MKL)
OMP_DYNAMIC=FALSE               # Disable dynamic OpenMP threads

# CUDA Specific
CUDA_LAUNCH_BLOCKING=0          # Async execution (faster)
CUDA_DEVICE_ORDER=PCI_BUS_ID    # GPU ordering by PCI bus
NCCL_DEBUG=INFO                 # NVIDIA collective communication debug

# Vulkan
VK_LAYER_PATH=/path/to/layers   # Vulkan layer path
VK_LOADER_DEBUG=all             # Verbose Vulkan loading

# Memory
MALLOC_TRIM_THRESHOLD_=131072   # Memory trimming threshold
LD_PRELOAD=/path/to/jemalloc.so # Use alternative allocator
```

### Build-Time Configuration

```bash
# Build type
CMAKE_BUILD_TYPE=Release        # Build configuration
CMAKE_CXX_FLAGS="-O3 -march=native"  # Custom optimization flags

# Compiler selection
CC=gcc-12                       # C compiler
CXX=g++-12                      # C++ compiler
AR=ar                           # Archiver

# Cross-compilation
CMAKE_SYSTEM_NAME=Linux         # Target system
CMAKE_SYSTEM_PROCESSOR=aarch64  # Target architecture
CMAKE_C_COMPILER=aarch64-linux-gnu-gcc
CMAKE_CXX_COMPILER=aarch64-linux-gnu-g++

# Installation
CMAKE_INSTALL_PREFIX=/usr/local # Installation directory
```

---

## Detailed Build Commands by Scenario

### Scenario 1: Linux Server (CPU Only)

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
# Binary at: ./build/bin/whisper-cli
```

### Scenario 2: Linux Server (NVIDIA GPU)

```bash
# Verify CUDA installation
nvcc --version
nvidia-smi

# Build with CUDA
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="86"
cmake --build build -j$(nproc)

# Run on GPU
./build/bin/whisper-cli -m models/ggml-base.bin -f audio.wav -gpu
```

### Scenario 3: Raspberry Pi (ARM Optimization)

```bash
# On Raspberry Pi directly
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
./build/bin/whisper-cli -m models/ggml-tiny.bin -f audio.wav -t 4
```

### Scenario 4: macOS M1/M2/M3 (Apple Silicon)

```bash
# Core ML models (optional, for better performance)
pip install ane_transformers openai-whisper coremltools
./models/generate-coreml-model.sh base.en

# Build with Core ML
cmake -B build -DWHISPER_COREML=1
cmake --build build -j$(sysctl -n hw.ncpu)

# Run (auto-uses Metal/Core ML)
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav
```

### Scenario 5: Windows (MSVC)

```powershell
# Open Visual Studio 2022 Command Prompt (x64)
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j %NUMBER_OF_PROCESSORS%
# Binary at: .\build\bin\Release\whisper-cli.exe
```

### Scenario 6: WebAssembly (Browser)

```bash
# Install Emscripten SDK first
emsdk install latest
emsdk activate latest
source ./emsdk_env.sh

# Build for WebAssembly
cd whisper.cpp
emcmake cmake -B build-wasm -DCMAKE_BUILD_TYPE=Release
cmake --build build-wasm -j$(nproc)

# JavaScript output in: ./build-wasm/
```

### Scenario 7: Docker Container

```bash
# Build image
docker build -t whisper-cpp .

# Run transcription
docker run --rm -v "$(pwd)/models:/models" \
    -v "$(pwd)/audio:/audio" \
    whisper-cpp:latest \
    whisper-cli -m /models/ggml-base.bin -f /audio/input.wav
```

---

## Continuous Integration Matrix

### Tested Platforms (GitHub Actions)

| OS      | Arch   | Compiler | GPU   | Status |
| ------- | ------ | -------- | ----- | ------ |
| Ubuntu  | x86-64 | GCC      | CPU   | ✅     |
| Ubuntu  | x86-64 | GCC      | CUDA  | ✅     |
| Ubuntu  | ARM64  | GCC      | CPU   | ✅     |
| macOS   | x86-64 | Clang    | CPU   | ✅     |
| macOS   | ARM64  | Clang    | Metal | ✅     |
| Windows | x86-64 | MSVC     | CPU   | ✅     |
| Docker  | x86-64 | GCC      | CPU   | ✅     |
| Docker  | x86-64 | GCC      | CUDA  | ✅     |

---

## Release Notes

### Version 1.8.6 (Current Stable)

**Key Features:**

- Stable multi-GPU support
- Improved quantization methods
- Enhanced Core ML support
- Better memory efficiency

**Breaking Changes:**
None

**Deprecations:**

- Older model formats (pre-v1.0)

**Migration Guide:**
Existing code should work without changes

---

## Additional Resources & Links

- **Official Repository**: https://github.com/ggml-org/whisper.cpp
- **Model Repository**: https://huggingface.co/ggerganov/whisper.cpp
- **GGML Library**: https://github.com/ggml-org/ggml
- **OpenAI Whisper**: https://github.com/openai/whisper
- **Issues**: https://github.com/ggml-org/whisper.cpp/issues
- **Discussions**: https://github.com/ggml-org/whisper.cpp/discussions
- **CI/CD**: https://github.com/ggml-org/whisper.cpp/actions

---

**Document Version**: 1.0  
**Last Updated**: 2026-06-16  
**License**: MIT (same as project)
