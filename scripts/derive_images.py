"""fastimage 两级派生图批量生成脚本。

从鬼刀原图（F:/photo/博客背景图/鬼刀/*.webp，超高清源）一次性降采样生成：
  - 2026/08/thumbs/<name>.webp  长边 800 / q72   → 相册列表缩略（40~120KB）
  - 2026/08/full/<name>.webp    长边 1600 / q74  → 灯箱查看（150~400KB）
母版 2026/08/<name>.webp（1920/q82）保留不动，继续作为 jsDelivr 回退源。

用法：
  python scripts/derive_images.py            # 增量（已存在的跳过）
  python scripts/derive_images.py --force    # 全部重算
依赖：Pillow（pip install pillow）
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(r"F:/photo/博客背景图/鬼刀")
OUT_DIR = REPO / "2026" / "08"

VARIANTS = [
    ("thumbs", 800, 72),
    ("full", 1600, 74),
]


def derive(src: Path, out_dir: Path, long_edge: int, quality: int) -> tuple[bool, int]:
    """返回 (是否新写入, 输出文件 KB)"""
    out = out_dir / src.name
    if out.exists():
        return False, out.stat().st_size // 1024

    with Image.open(src) as im:
        if getattr(im, "n_frames", 1) > 1:
            raise ValueError(f"animated webp not supported: {src.name}")
        im = im.convert("RGB")
        w, h = im.size
        scale = long_edge / max(w, h)
        if scale < 1:
            im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        out_dir.mkdir(parents=True, exist_ok=True)
        im.save(out, "WEBP", quality=quality, method=6)
    return True, out.stat().st_size // 1024


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="重算已存在的输出")
    parser.add_argument("--only", type=str, default="", help="只处理文件名包含该子串的图")
    args = parser.parse_args()

    sources = sorted(SOURCE_DIR.glob("*.webp"))
    if args.only:
        sources = [s for s in sources if args.only in s.name]
    if not sources:
        print(f"no sources in {SOURCE_DIR}")
        return 1
    print(f"{len(sources)} sources → {OUT_DIR}/(thumbs|full)")

    total_kb = 0
    for i, src in enumerate(sources, 1):
        line = f"[{i}/{len(sources)}] {src.name}"
        try:
            for sub, edge, q in VARIANTS:
                out_dir = OUT_DIR / sub
                if args.force and (out_dir / src.name).exists():
                    (out_dir / src.name).unlink()
                created, kb = derive(src, out_dir, edge, q)
                total_kb += kb
                line += f"  {sub}:{'new ' if created else 'keep '}{kb}KB"
            print(line)
        except Exception as e:  # noqa: BLE001
            print(f"{line}  ERROR: {e}")
    print(f"total output size: {total_kb / 1024:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
