from pathlib import Path

from harness import check_t3, check_t4, check_t5, check_t7, check_t9, check_t1

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "toy-study"


def test_example_t1_no_ai_use():
    result = check_t1(EXAMPLE, ai_use_before=0)
    assert result.passed, result.detail


def test_example_draft_output_metadata():
    assert check_t5(EXAMPLE).passed
    assert check_t3(EXAMPLE).passed
    assert check_t4(EXAMPLE).passed
    assert check_t9(EXAMPLE).passed
    assert check_t7(EXAMPLE).passed
