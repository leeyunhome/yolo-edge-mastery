# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Portfolio repository demonstrating end-to-end expertise from YOLO model design → pruning/quantization → edge deployment → MLOps pipeline.

Target: 7-year+ experience level. All work should produce quantitative benchmarks suitable for interview discussion: "Original: X size/Y FPS/Z mAP → Optimized: A% smaller / B× faster / C% mAP loss."

## Planned Repository Structure

```
yolo-edge-mastery/
├── 01_yolo_basics/          # YOLOv8~v11 training, validation, inference
├── 02_custom_backbone/      # CSPNet/C2f analysis; custom backbone replacement experiments
├── 03_pruning/              # Structured pruning (torch-pruning), unstructured (torch.nn.utils.prune)
├── 04_quantization/         # PTQ (torch.quantization) and QAT comparison
├── 05_edge_deployment/      # ONNX, TensorRT, OpenVINO export and inference
├── 06_mlops_pipeline/       # Docker + local MLflow; Active Learning loop
├── 07_video_pipeline/       # GStreamer, FFMPEG, multi-channel RTSP (preferred qualification)
├── benchmarks/results.csv   # Canonical performance metrics (all phases)
├── references/              # Planning documents
└── requirements.txt
```

## Environment Setup

conda recommended — handles CUDA/cuDNN version matching and non-Python packages (GStreamer).

```bash
conda create -n yolo-edge python=3.10 -y
conda activate yolo-edge

# PyTorch + CUDA (includes cuDNN automatically)
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia

pip install -r requirements.txt
```

TensorRT: install separately via NVIDIA official guide (not on conda/pip).  
GStreamer (Phase 7): `conda install -c conda-forge gstreamer gst-plugins-base python-gst`

## Key Libraries by Phase

| Phase | Libraries |
|-------|-----------|
| 1–2 YOLO & Backbone | `ultralytics` |
| 3 Pruning | `torch-pruning`, `torch.nn.utils.prune` |
| 4 Quantization | `torch.quantization` (PTQ/QAT) |
| 5 Edge Deployment | `onnx`, `onnxruntime`, `tensorrt`, `openvino` |
| 6 MLOps | `mlflow`, Docker, docker-compose |
| 7 Video | `gst-python`, `ffmpeg-python` |

## benchmarks/results.csv Schema

All experiments must record results here:

```
model_name, variant, phase, metric_type, baseline_value, optimized_value, improvement_pct
```

## Technology Decision Reference

- **Pruning**: torch-pruning for structured (hardware-efficient); `torch.nn.utils.prune` for unstructured
- **Quantization**: PTQ for no-retraining speed; QAT for accuracy-sensitive cases (requires fine-tuning)
- **Deployment target**:
  - TensorRT → NVIDIA GPU / Jetson (maximum performance)
  - OpenVINO → Intel CPU edge (broad compatibility)
  - ONNX → format-agnostic interchange
- **MLOps**: Local MLflow for closed-network (on-premise) requirement; Docker for environment reproducibility

## Development Principle

Each module's README must document:
1. What was implemented
2. Why this technique was chosen over alternatives
3. Benchmark results table (before vs. after)
