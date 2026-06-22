# Phase 3 — 경량화: Pruning ⭐ 면접 핵심

## 목표
Structured / Unstructured Pruning을 적용하고, 수치 벤치마크를 도출한다.

## 체크리스트
- [ ] torch-pruning으로 Structured Pruning (채널 단위)
- [ ] torch.nn.utils.prune으로 Unstructured Pruning (가중치 단위)
- [ ] Sparsity별 (20% / 40% / 60%) 벤치마크 측정
- [ ] 결과를 benchmarks/results.csv에 기록

## 핵심 수치 (면접 답변 형식)
> "원본 대비 모델 크기 **X% 감소**, FPS **B배 향상**, mAP **C% 하락**"

## 결과
| 기법 | Sparsity | 모델 크기 | FPS | mAP@0.5 | 비고 |
|------|---------|---------|-----|---------|------|
| 원본 | 0% | - | - | - | 기준선 |
| Structured | 40% | - | - | - | |
| Unstructured | 40% | - | - | - | |

## 의사결정 근거
<!-- Structured vs Unstructured 선택 이유 -->
<!-- torch-pruning 선택 이유 -->
