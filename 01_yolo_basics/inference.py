"""
YOLOv8 추론 스크립트.
모델 크기별(n/s/m/l/x) FPS·mAP 비교 벤치마크 포함.

사용법:
  python inference.py --model yolov8n.pt --source image.jpg
  python inference.py --benchmark --models yolov8n yolov8s yolov8m
"""

import argparse
import time
import csv
from pathlib import Path

import torch
from ultralytics import YOLO


def run_inference(model_path: str, source: str):
    model = YOLO(model_path)
    results = model(source, stream=True)
    for r in results:
        print(r.boxes)


def benchmark_models(model_names: list[str], source: str, n_runs: int = 100):
    """모델 크기별 FPS 측정 후 출력."""
    rows = []
    for name in model_names:
        model = YOLO(f"{name}.pt")
        # 워밍업
        model(source)

        start = time.perf_counter()
        for _ in range(n_runs):
            model(source, verbose=False)
        elapsed = time.perf_counter() - start

        fps = n_runs / elapsed
        params = sum(p.numel() for p in model.model.parameters()) / 1e6
        print(f"{name}: {fps:.1f} FPS | {params:.1f}M params")
        rows.append({"model": name, "fps": round(fps, 2), "params_M": round(params, 2)})

    # 결과 저장
    out = Path("../benchmarks/results.csv")
    write_header = not out.exists()
    with open(out, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "fps", "params_M"])
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="yolov8n.pt")
    parser.add_argument("--source", default="https://ultralytics.com/images/bus.jpg")
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--models", nargs="+", default=["yolov8n", "yolov8s", "yolov8m"])
    parser.add_argument("--n-runs", type=int, default=100)
    args = parser.parse_args()

    if args.benchmark:
        benchmark_models(args.models, args.source, args.n_runs)
    else:
        run_inference(args.model, args.source)
