#!/usr/bin/env python3
"""Score a paper folder against SPEC §16 file assertions.

  python tests/toy-study/score.py PATH
  python tests/toy-study/score.py PATH --tests T1,T5,T13
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from harness import (
    check_t1,
    check_t10,
    check_t11,
    check_t12,
    check_t13,
    check_t2,
    check_t3,
    check_t4,
    check_t5,
    check_t6,
    check_t7,
    check_t8,
    check_t9,
    list_ai_use,
    load_layout,
)

DEFAULTS = ("T1", "T3", "T4", "T5", "T7", "T9", "T13")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score Research Agent Kit file assertions.")
    parser.add_argument("root", type=Path)
    parser.add_argument("--tests", default=",".join(DEFAULTS))
    parser.add_argument("--ai-use-after-t11", type=int, default=None)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    wanted = [t.strip().upper() for t in args.tests.split(",") if t.strip()]
    layout = load_layout(root)
    results = []
    for test_id in wanted:
        if test_id == "T1":
            results.append(check_t1(root, ai_use_before=len(list_ai_use(root, layout))))
        elif test_id == "T2":
            results.append(check_t2(root))
        elif test_id == "T3":
            results.append(check_t3(root))
        elif test_id == "T4":
            results.append(check_t4(root))
        elif test_id == "T5":
            results.append(check_t5(root))
        elif test_id == "T6":
            results.append(check_t6(root))
        elif test_id == "T7":
            results.append(check_t7(root))
        elif test_id == "T8":
            results.append(check_t8(root))
        elif test_id == "T9":
            results.append(check_t9(root))
        elif test_id == "T10":
            results.append(check_t10(root))
        elif test_id == "T11":
            results.append(check_t11(root))
        elif test_id == "T12":
            n = args.ai_use_after_t11
            if n is None:
                n = len(list_ai_use(root, layout))
            results.append(check_t12(root, n))
        elif test_id == "T13":
            results.append(check_t13(root))
        else:
            print(f"Unknown test {test_id}", file=sys.stderr)
            return 2
    failed = 0
    for item in results:
        mark = "PASS" if item.passed else "FAIL"
        print(f"{item.test_id} {mark}  {item.detail}")
        if not item.passed:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
