# Phase 6 — MLOps 파이프라인

## 목표
폐쇄망 환경을 가정한 Docker + Local MLflow 기반 재현 가능한 학습·배포 파이프라인 구축.

## 체크리스트
- [ ] Docker로 학습 환경 컨테이너화 (docker-compose.yml)
- [ ] Local MLflow 서버 설정 및 실험 추적
- [ ] 파라미터·메트릭·아티팩트 자동 로깅
- [ ] 간단한 Active Learning 루프 구현 (불확실성 기반 샘플 선별)

## 파이프라인 구조
```
데이터 수집 → 전처리 → 학습 (MLflow 추적) → 평가 → 배포
       ↑                                              |
       └────────── Active Learning 피드백 루프 ────────┘
```

## 의사결정 근거
<!-- Active Learning 데이터 선별 기준 (불확실성? Diversity?) -->
<!-- 폐쇄망 제약 조건과 해결 방법 -->
