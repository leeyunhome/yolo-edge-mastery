# GEMINI.md

이 파일은 Gemini / Antigravity AI 코딩 어시스턴트가 이 저장소에서 작업할 때 참고하는 안내 문서입니다. 개발 과정과 중요한 설계 결정을 누적 기록하여 일관성 있는 코딩 지원을 제공합니다.

---

## 1. 프로젝트 목적 및 파이프라인 개요
본 프로젝트(`yolo-edge-mastery`)는 YOLO 모델을 기반으로 한 End-to-End Edge 디바이스 배포 및 MLOps 파이프라인 구축 포트폴리오입니다.

### 전체 파이프라인 구조
```
YOLOv8~v11 학습  →  Custom Backbone  →  Pruning / Quantization  →  Edge 배포  →  MLOps
   Phase 1~2           Phase 2              Phase 3~4              Phase 5       Phase 6
```

---

## 2. 개발 환경 정보
- **OS:** Windows (테스트 기기: Android SM-G991N)
- **Conda 환경:** `yolo-edge`
- **언어 및 프레임워크:** Python 3.10.20 / PyTorch 2.5.1+cu121 (CUDA 활성화)
- **하드웨어:** NVIDIA GeForce RTX 4060 Laptop GPU
- **사용 패키지:** `ultralytics` 8.4.75

---

## 3. 핵심 규칙 및 개발 가이드라인

### ⚠️ Windows Jupyter 환경 멀티프로세싱 버그 방지 (필수)
Windows 환경의 주피터 노트북에서 PyTorch/Ultralytics 데이터 로더가 멀티프로세싱을 시도하면 무한 대기(락) 상태에 빠지거나 극도로 느려집니다.
- **규칙:** `model.val()` 호출 시 반드시 **`workers=0`** 옵션을 명시해야 합니다.
  - *예시 코드:* `r = model.val(data="coco128.yaml", workers=0)`

### 🎨 웹 개발 스타일 가이드 (해당 시)
- **CSS:** TailwindCSS 대신 Vanilla CSS 사용을 우선하되, HSL 테일러드 컬러 및 sleek dark mode 등의 현대적인 테마 적용.
- **Flutter 개발 시 참고:** Android 테스트 기기(`SM-G991N`)의 ML Kit 호환성 이슈 해결을 위해 카메라 이미지 포맷은 **`bgra8888`**로 고정하여 사용합니다.

---

## 4. 모델 벤치마크 및 설계 결정 사항

### Phase 1 벤치마크 완료 (coco128 검증 세트 기준)
- **yolov8n:** 3.2M params / 12.6MB / 63.1 FPS / mAP@0.5: 0.605 / mAP@0.5:0.95: 0.445
- **yolov8s:** 11.2M params / 44.6MB / 65.0 FPS / mAP@0.5: 0.759 / mAP@0.5:0.95: 0.585
- **yolov8m:** 25.9M params / 103.5MB / 54.4 FPS / mAP@0.5: 0.781 / mAP@0.5:0.95: 0.608
- **yolov9s:** 7.2M params / 28.8MB / 29.0 FPS / mAP@0.5: 0.729 / mAP@0.5:0.95: 0.574
- **yolo11n:** 2.6M params / 10.5MB / 47.9 FPS / mAP@0.5: 0.670 / mAP@0.5:0.95: 0.502
- **yolo11s:** 9.4M params / 37.0MB / 48.4 FPS / mAP@0.5: 0.750 / mAP@0.5:0.95: 0.574

### 📌 경량화 베이스라인 결정: `yolov8n`
- **결정 이유:**
  1. **구현 편의성:** Structured Pruning 및 QAT 구현 시 최신 버전(v11)보다 v8이 전 세계 오픈소스 레퍼런스가 훨씬 풍부하여 디버깅 비용을 최소화할 수 있습니다.
  2. **경량화 임팩트:** 이미 극도로 설계 최적화가 된 `yolo11n`(2.6M)보다 `yolov8n`(3.2M)을 직접 프루닝하고 양자화하여 성능 하락을 방지하는 스토리가 포트폴리오 면접관 관점에서 더 강력한 임팩트를 줍니다.
  3. **초기 FPS 속도 우위:** 초기 속도가 63.1 FPS로 YOLO11n(47.9 FPS)보다 빠르게 측정되어 경량화 시작점으로 적합합니다.

---

## 5. 현재 진행 상황
- **Phase 1 (YOLO 기초 및 벤치마크):** ✅ 완료 및 Git Push 완료
- **Phase 2 (Custom Backbone 실험):** 🔲 예정
