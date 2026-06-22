"""
YOLOv8 학습 스크립트.
커스텀 데이터셋 또는 COCO 사전학습 모델 기준으로 학습 실행.

사용법:
  python train.py --model yolov8n --epochs 100 --data coco128.yaml
  python train.py --model yolov8s --data custom.yaml --imgsz 640
"""

import argparse
from pathlib import Path
from ultralytics import YOLO


def train(model_name: str, data: str, epochs: int, imgsz: int, project: str):
    model = YOLO(f"{model_name}.pt")

    results = model.train(
        data=data,
        epochs=epochs,
        imgsz=imgsz,
        project=project,
        name=model_name,
        exist_ok=True,
    )
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="yolov8n", help="모델 이름 (yolov8n/s/m/l/x)")
    parser.add_argument("--data", default="coco128.yaml", help="데이터셋 YAML 경로")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--project", default="runs/train")
    args = parser.parse_args()

    train(args.model, args.data, args.epochs, args.imgsz, args.project)
