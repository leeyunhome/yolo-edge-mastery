# yolo-edge-mastery

End-to-end YOLO pipeline: custom backbone → pruning/quantization → TensorRT/OpenVINO edge deployment + MLOps

> Portfolio — AI Software Engineer (Vision & MLOps Specialist)

---

## Pipeline Overview

```
YOLOv8~v11 학습  →  Custom Backbone  →  Pruning / Quantization  →  Edge 배포  →  MLOps
   Phase 1~2           Phase 2              Phase 3~4              Phase 5       Phase 6
```

---

## Benchmark Results

<!-- BENCHMARK_START -->
### phase1
| 모델 | 크기(MB) | params(M) | FPS | mAP@0.5 | mAP@0.5:0.95 |
|------|---|---|---|---|---|
| yolo11n | 10.5 | 2.6 | 47.9 | 0.670 | 0.502 |
| yolo11s | 37.8 | 9.4 | 48.4 | 0.750 | 0.574 |
| yolov8m | 103.5 | 25.9 | 54.4 | 0.781 | 0.608 |
| yolov8n | 12.6 | 3.2 | 63.1 | 0.605 | 0.445 |
| yolov8s | 44.6 | 11.2 | 65.0 | 0.759 | 0.585 |
| yolov9s | 28.8 | 7.2 | 29.0 | 0.729 | 0.574 |
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
