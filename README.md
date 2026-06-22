# yolo-edge-mastery

End-to-end YOLO pipeline: custom backbone → pruning/quantization → TensorRT/OpenVINO edge deployment + MLOps

> Portfolio for AI Software Engineer (Vision & MLOps Specialist) — (주)미스릴

---

## Pipeline Overview

```
YOLOv8~v11 학습  →  Custom Backbone  →  Pruning / Quantization  →  Edge 배포  →  MLOps
   Phase 1~2           Phase 2              Phase 3~4              Phase 5       Phase 6
```

---

## Benchmark Results

<!-- BENCHMARK_START -->
| model | variant | phase | metric | value |
|-------|---------|-------|--------|-------|
| yolov8n | baseline | phase1 | FPS | 63.1 |
| yolov8n | baseline | phase1 | params_M | 3.2 |
| yolov8s | baseline | phase1 | FPS | 65.0 |
| yolov8s | baseline | phase1 | params_M | 11.2 |
| yolov8m | baseline | phase1 | FPS | 54.4 |
| yolov8m | baseline | phase1 | params_M | 25.9 |
<!-- BENCHMARK_END -->

---

## Phases

| Phase | 주제 | 상태 |
|-------|------|------|
| 1 | YOLO 기초 — YOLOv8~v11 학습·추론·벤치마크 | ✅ |
| 2 | Custom Backbone — CSPNet/C2f 분석 및 교체 실험 | 🔲 |
| 3 | Pruning — Structured / Unstructured 경량화 | 🔲 |
| 4 | Quantization — PTQ / QAT 비교 | 🔲 |
| 5 | Edge Deployment — ONNX / TensorRT / OpenVINO | 🔲 |
| 6 | MLOps — Docker + Local MLflow + Active Learning | 🔲 |
| 7 | Video Pipeline — GStreamer / FFMPEG / RTSP | 🔲 |

---

## Environment

- Python 3.10 / PyTorch 2.5.1+cu121
- GPU: NVIDIA GeForce RTX 4060 Laptop GPU
- conda 환경: `conda env create -f environment.yml`
