# Phase 5 — 엣지 배포

## 목표
ONNX → TensorRT / OpenVINO 변환 및 타겟별 추론 속도를 측정한다.

## 체크리스트
- [ ] PyTorch → ONNX 변환 및 검증 (onnxruntime)
- [ ] ONNX → TensorRT FP16/INT8 엔진 변환
- [ ] ONNX → OpenVINO IR 변환
- [ ] 동일 입력 기준 추론 속도·정확도 비교
- [ ] 결과를 benchmarks/results.csv에 기록

## 결과
| 포맷 | 디바이스 | Latency (ms) | FPS | mAP@0.5 |
|------|---------|------------|-----|---------|
| PyTorch FP32 | CPU | - | - | - |
| ONNX | CPU | - | - | - |
| TensorRT FP16 | GPU | - | - | - |
| OpenVINO | CPU | - | - | - |

## 의사결정 근거
<!-- TensorRT vs OpenVINO vs ONNX 선택 기준 -->
