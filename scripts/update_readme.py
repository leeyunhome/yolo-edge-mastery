"""
benchmarks/results.csv → README.md 벤치마크 표 자동 업데이트.
long 형식 CSV를 wide 형식 표로 피벗해서 출력.
GitHub Actions 또는 로컬에서 실행.
"""

import csv
from collections import defaultdict
from pathlib import Path

README = Path("README.md")
CSV = Path("benchmarks/results.csv")

START = "<!-- BENCHMARK_START -->"
END = "<!-- BENCHMARK_END -->"

# 표시할 컬럼 순서 및 헤더명
COLUMNS = [
    ("size_MB",    "크기(MB)"),
    ("params_M",   "params(M)"),
    ("FPS",        "FPS"),
    ("mAP50",      "mAP@0.5"),
    ("mAP50-95",   "mAP@0.5:0.95"),
]


def build_table(csv_path: Path) -> str:
    # (model, phase) → {metric: value} 로 피벗
    data = defaultdict(dict)
    phases = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row["model_name"], row["phase"])
            data[key][row["metric_type"]] = row["optimized_value"]
            if row["phase"] not in phases:
                phases.append(row["phase"])

    lines = []
    for phase in phases:
        models = [k for k in data if k[1] == phase]
        if not models:
            continue

        col_headers = " | ".join(h for _, h in COLUMNS)
        col_sep = "|".join("---" for _ in COLUMNS)
        lines.append(f"### {phase}")
        lines.append(f"| 모델 | {col_headers} |")
        lines.append(f"|------|{col_sep}|")

        for model, _ in sorted(models):
            metrics = data[(model, phase)]
            vals = " | ".join(metrics.get(k, "-") for k, _ in COLUMNS)
            lines.append(f"| {model} | {vals} |")

        lines.append("")

    return "\n".join(lines).rstrip()


def update_readme():
    content = README.read_text(encoding="utf-8")
    table = build_table(CSV)

    start_idx = content.index(START) + len(START)
    end_idx = content.index(END)

    new_content = content[:start_idx] + "\n" + table + "\n" + content[end_idx:]
    README.write_text(new_content, encoding="utf-8")
    print("README.md 업데이트 완료")


if __name__ == "__main__":
    update_readme()
