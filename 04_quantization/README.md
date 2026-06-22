# Phase 4 — 경량화: Quantization ⭐ 면접 핵심

## 목표
PTQ(재학습 없음)와 QAT(학습 중 양자화)를 비교하고 정확도 손실 완화 전략을 정리한다.

## 체크리스트
- [ ] PTQ: torch.quantization으로 INT8 변환
- [ ] QAT: QuantStub 삽입 후 파인튜닝
- [ ] PTQ vs QAT 정확도·속도·크기 비교
- [ ] 결과를 benchmarks/results.csv에 기록

## 핵심 수치 (면접 답변 형식)
> "FP32 → INT8: 모델 크기 **75% 감소**, 추론 속도 **X배 향상**, mAP **C% 하락**"

## 결과
| 기법 | 정밀도 | 모델 크기 | Latency | mAP@0.5 |
|------|-------|---------|---------|---------|
| 원본 FP32 | 32-bit | - | - | - |
| PTQ INT8 | 8-bit | - | - | - |
| QAT INT8 | 8-bit | - | - | - |

## 의사결정 근거
<!-- PTQ vs QAT 선택 기준, 정확도 손실 완화 방법 -->
