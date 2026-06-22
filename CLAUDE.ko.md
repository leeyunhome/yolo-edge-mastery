# CLAUDE.ko.md

이 파일은 이 레포지토리에서 작업하는 Claude Code(claude.ai/code)에게 제공되는 가이드입니다.

## 프로젝트 목적

YOLO 모델 설계 → 경량화(Pruning/Quantization) → 엣지 배포 → MLOps 파이프라인까지 End-to-End 전문성을 실증하는 포트폴리오 레포지토리.

목표 수준: 경력 7년 이상. 모든 작업은 면접에서 구체적으로 설명 가능한 수치 벤치마크를 도출해야 합니다:  
"원본 대비 크기 X% 감소 / 속도 B배 향상 / mAP C% 하락"

## 레포지토리 구조 (목표)

```
yolo-edge-mastery/
├── 01_yolo_basics/          # YOLOv8~v11 학습·검증·추론 기초
├── 02_custom_backbone/      # CSPNet/C2f 분석; 커스텀 백본 교체 실험
├── 03_pruning/              # Structured pruning (torch-pruning), Unstructured (torch.nn.utils.prune)
├── 04_quantization/         # PTQ (torch.quantization) 및 QAT 비교
├── 05_edge_deployment/      # ONNX, TensorRT, OpenVINO 변환 및 추론
├── 06_mlops_pipeline/       # Docker + Local MLflow; Active Learning 루프
├── 07_video_pipeline/       # GStreamer, FFMPEG, 다중 채널 RTSP (우대 자격)
├── benchmarks/results.csv   # 전 단계 성능 지표 통합 관리
├── references/              # 기획 문서
└── requirements.txt
```

## 환경 설정

conda 사용 권장 — CUDA/cuDNN 버전 매칭과 GStreamer 등 비Python 패키지 관리 때문.  
conda는 `~/.conda/pkgs/` 공유 캐시 + hard link 방식이라 여러 환경을 만들어도 storage가 중복 소비되지 않음.

```bash
# environment.yml로 한 번에 생성 (권장)
conda env create -f environment.yml
conda activate yolo-edge

# 환경 업데이트 시
conda env update -f environment.yml --prune
```

TensorRT는 NVIDIA 공식 가이드로 별도 설치 (conda/pip 미지원).


## 단계별 핵심 라이브러리

| 단계 | 라이브러리 |
|------|-----------|
| 1–2 YOLO 및 백본 | `ultralytics` |
| 3 프루닝 | `torch-pruning`, `torch.nn.utils.prune` |
| 4 양자화 | `torch.quantization` (PTQ/QAT) |
| 5 엣지 배포 | `onnx`, `onnxruntime`, `tensorrt`, `openvino` |
| 6 MLOps | `mlflow`, Docker, docker-compose |
| 7 영상 처리 | `gst-python`, `ffmpeg-python` |

## benchmarks/results.csv 스키마

모든 실험 결과는 여기에 기록합니다:

```
model_name, variant, phase, metric_type, baseline_value, optimized_value, improvement_pct
```

## 기술 의사결정 기준

- **프루닝**: 하드웨어 효율을 위한 Structured → torch-pruning; 비구조적 → `torch.nn.utils.prune`
- **양자화**: 재학습 없이 속도 개선 → PTQ; 정확도 손실 최소화 필요 → QAT (파인튜닝 포함)
- **배포 타겟**:
  - TensorRT → NVIDIA GPU / Jetson (최고 성능)
  - OpenVINO → Intel CPU 엣지 (광범위 호환)
  - ONNX → 포맷 중립적 중간 형식
- **MLOps**: 폐쇄망 환경 → Local MLflow; 재현 가능한 환경 → Docker

## 개발 원칙

각 모듈의 README에는 반드시 다음을 포함합니다:
1. 구현 내용
2. 다른 기법 대신 이 기법을 선택한 이유
3. 벤치마크 결과표 (적용 전 vs. 적용 후)
