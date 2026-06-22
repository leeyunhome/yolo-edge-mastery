# yolo-edge-mastery — Claude Code Reference

## 목적
(주)미스릴 AI Software Engineer (Vision & MLOps Specialist) 포지션 지원을 위한 학습 및 포트폴리오 레포지토리.
**핵심 목표**: YOLO 기반 모델 설계 → 경량화(Pruning/Quantization) → 엣지 배포까지의 End-to-End 파이프라인 구축.

---

## 채용 포지션 요약

| 항목 | 내용 |
|------|------|
| 회사 | (주)미스릴 |
| 포지션 | AI Software Engineer (Vision & MLOps Specialist) |
| 연봉 | 5,000만원 ~ 10,000만원 |
| 직급 | 협의 |
| 필요 경력 | 7년 이상 |

---

## 핵심 업무 내용

1. **Edge-Driven Vision 모델 설계**: YOLOv8~v11 기반 객체 탐지, 저조도·고속 이동 환경 최적화 및 경량화
2. **On-premise MLOps 체계 구축**: 폐쇄망 환경에서 Active Learning 기반 데이터 수집 → 학습 → 배포 파이프라인
3. **HW 가속 최적화**: 엣지 디바이스 특성에 맞춘 추론 엔진 개발
4. **데이터 신뢰성 파이프라인**: 수천 시간 영상 데이터에서 유의미한 데이터 선별 및 재학습 투입

---

## 자격 요건 (필수)

- 관련 경력 7년 이상
- **YOLO 전문가**: Custom Backbone 설계 및 가중치 최적화(Pruning, Quantization)를 통한 실시간 추론 성능 극대화
- **End-to-End MLOps**: Docker, Local MLflow 활용, 성능 모니터링 및 재학습 자동화
- **Python 숙련도**: 엣지 환경 리소스 관리, 고성능 비전 처리 알고리즘 구현
- **기술 의사결정 및 멘토링**: 주니어/미들급 코드 리뷰 및 기술 가이드

## 자격 요건 (우대)

- **영상 분석 파이프라인**: GStreamer, FFMPEG 기반 다중 채널 RTSP 스트리밍 및 실시간 분석
- **Edge AI 프레임워크**: NVIDIA DeepStream SDK, OpenVINO 활용 파이프라인 고도화
- **산업용 통신 프로토콜**: Modbus, TCP/IP, MQTT를 통한 PLC/현장 데이터 연동

---

## 레포지토리 구조 (목표)

```
yolo-edge-mastery/
├── 01_yolo_basics/          # YOLOv8~v11 학습·추론 기초 실습
│   ├── train.py
│   ├── inference.py
│   └── README.md
├── 02_custom_backbone/      # Custom Backbone 설계 및 교체 실험
│   ├── backbones/
│   └── README.md
├── 03_pruning/              # Structured / Unstructured Pruning 실습
│   ├── torch_pruning_demo.py
│   └── README.md
├── 04_quantization/         # PTQ / QAT 실습 및 성능 비교
│   ├── ptq_demo.py
│   ├── qat_demo.py
│   └── README.md
├── 05_edge_deployment/      # TensorRT, ONNX, OpenVINO 변환 및 배포
│   ├── export_onnx.py
│   ├── tensorrt_infer.py
│   └── README.md
├── 06_mlops_pipeline/       # Docker + MLflow 기반 로컬 MLOps
│   ├── docker-compose.yml
│   ├── mlflow_tracking.py
│   └── README.md
├── 07_video_pipeline/       # GStreamer / FFMPEG / RTSP 실습 (우대사항)
│   └── README.md
├── benchmarks/              # 실험 결과 수치 정리 (속도/정확도/모델 크기)
│   └── results.csv
├── requirements.txt
└── README.md
```

---

## 학습 단계별 우선순위

### Phase 1 — YOLO 기본기 (1~2주)
- [ ] YOLOv8 학습·검증·추론 전 과정 직접 실행
- [ ] v8 → v9 → v11 아키텍처 변화 정리
- [ ] Ultralytics CLI 및 Python API 숙달

### Phase 2 — Backbone 이해 (2~3주)
- [ ] CSPNet, C2f 구조 분석
- [ ] Custom Backbone 교체 실험 (ResNet50 → YOLO head)
- [ ] 성능 비교: mAP, FPS, 파라미터 수

### Phase 3 — 경량화 (2~3주) ← 면접 핵심
- [ ] Structured Pruning (torch-pruning 라이브러리)
- [ ] PTQ: torch.quantization 활용
- [ ] QAT: 학습 중 양자화 적용
- [ ] **벤치마크 수치 도출**: 원본 대비 크기·속도·정확도 변화표 작성

### Phase 4 — 엣지 배포 (2~3주)
- [ ] ONNX 변환 및 검증
- [ ] TensorRT 엔진 변환 및 추론 속도 측정
- [ ] OpenVINO 변환 실습

### Phase 5 — MLOps 파이프라인 (2~3주)
- [ ] Docker로 학습 환경 컨테이너화
- [ ] Local MLflow 실험 추적 설정
- [ ] 간단한 Active Learning 루프 구현

---

## 면접 대비 핵심 질문

1. YOLO Custom Backbone을 직접 설계한 경험과 그 이유는?
2. Quantization 적용 시 정확도 손실을 어떻게 최소화했나?
3. 폐쇄망 MLOps에서 가장 어려운 점과 해결 방법은?
4. Active Learning 데이터 선별 기준을 어떻게 설계했나?
5. DeepStream vs OpenVINO 선택 기준은?

---

## 참고 자료

- [Ultralytics 공식 문서](https://docs.ultralytics.com)
- [torch-pruning GitHub](https://github.com/VainF/Torch-Pruning)
- [PyTorch Quantization 튜토리얼](https://pytorch.org/docs/stable/quantization.html)
- [NVIDIA DeepStream SDK](https://developer.nvidia.com/deepstream-sdk)
- [OpenVINO 공식 문서](https://docs.openvino.ai)
- 데이터셋: COCO, VisDrone (저조도·소형 객체 환경 유사)

---

## 메모
- 모든 실험은 **수치 결과(벤치마크)** 중심으로 정리할 것
- 각 모듈 README에 "왜 이 기법을 선택했는가" 의사결정 근거 기록
- 면접 시 "원본 대비 크기 X% 감소, 속도 X배 향상, mAP X% 하락" 형태로 말할 수 있도록 준비