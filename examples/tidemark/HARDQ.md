# Hard questions, answered before launch

1. **How is this different from doing it in a photo app?** Photo apps import into a library; Tidemark only renames files where they are, previews first [R2] and can undo [R4].
2. **Why not a ten-line exiftool one-liner?** That works, and Tidemark uses exiftool underneath. What it adds is the preview, clash handling [R5] and the undo file [R4]. If the one-liner works for you, use it.
3. **What data does it touch or send?** It reads metadata and renames files in the folder you give it. No network code [R6].
4. **What if the capture date is wrong or missing?** Files without a date are listed and left alone. Wrong camera clocks: there is a `--shift` flag; no receipt for edge cases yet, so I would say "tell me what you hit".
5. **Windows?** Not tested [R3]. If you try, please report.
6. **Will it be maintained?** It's a side project I use every month. I can't promise more than that.
7. **What does it cost?** Free and MIT. No paid version planned.
8. **Why trust it with my photos?** Run `--dry-run` first, keep a backup, and read `tests/test_undo.py` [R4]. Don't trust any renamer without a backup, including this one.
