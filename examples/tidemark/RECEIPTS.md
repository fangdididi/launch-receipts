# Receipts: Tidemark

| id | kind | claim | evidence |
|---|---|---|---|
| R1 | RUN | renamed the 2,000-file sample set in about 4 seconds | `time tidemark ./bench-2000` on a 2022 laptop (8 cores, SSD), 3 runs: 4.3 s, 4.1 s, 4.0 s; 2026-10-18 |
| R2 | SHOWN | shows a dry-run table before touching any file | `docs/preview.png`, real UI, fictional file names |
| R3 | WISH | works on Windows | never tested |
| R4 | FILE | every run writes an undo file that restores the old names | `tests/test_undo.py::test_round_trip`, `docs/undo.md` |
| R5 | RUN | handles name clashes by adding -1, -2 instead of overwriting | `tidemark --dry-run ./sample-photos/burst` output, 6 shots in the same second |
| R6 | FILE | nothing leaves the machine; no network code | `grep -rn "socket\|requests\|urllib" src/` returns nothing; no network deps in `pyproject.toml` |
| R7 | STATED | reads most camera formats | true as far as Mei knows; depends on exiftool; rephrased as "anything exiftool can read" |
| R8 | QUOTE | "finally sorted my dad's 2009 Canon folder" | Ana, beta tester, agreed to be quoted by first name, message of 2026-10-12 |
