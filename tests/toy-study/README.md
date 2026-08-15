# Toy-study tests

Structural checks and T13 run in CI:

```text
pip install -r requirements-dev.txt
pytest tests/toy-study
```

T1–T12 are **file assertions after an agent run**. Score a folder:

```text
python tests/toy-study/score.py examples/toy-study
python tests/toy-study/score.py PATH --tests T2,T6,T8,T11
```

A different run from the implementer should score T1–T12 against prompts in `SPEC.md` §16. The example toy study is expected to pass T1, T3, T4, T5, T7, T9, and T13 in its committed state (draft output, no AI-use events, no assigned task).
