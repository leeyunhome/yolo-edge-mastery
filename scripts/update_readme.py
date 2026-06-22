"""
benchmarks/results.csv → README.md 벤치마크 표 자동 업데이트.
GitHub Actions 또는 로컬에서 실행.
"""

import csv
from pathlib import Path

README = Path("README.md")
CSV = Path("benchmarks/results.csv")

START = "<!-- BENCHMARK_START -->"
END = "<!-- BENCHMARK_END -->"


def build_table(csv_path: Path) -> str:
    rows = []
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)

    lines = ["| model | variant | phase | metric | value |",
             "|-------|---------|-------|--------|-------|"]
    for r in rows:
        val = r.get("optimized_value", "-")
        lines.append(f"| {r['model_name']} | {r['variant']} | {r['phase']} | {r['metric_type']} | {val} |")

    return "\n".join(lines)


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
