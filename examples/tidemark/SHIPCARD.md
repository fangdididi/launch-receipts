# Ship card: Tidemark (fictional example)

Frozen: 2026-10-19, before any post was written.

- **What**: a command-line tool that renames photos and videos to their capture date, shows a dry-run table first, and writes an undo file.
- **For**: someone with years of camera and phone exports named `IMG_4412.JPG`, `DSC00981.ARW`, `PXL_20230611_...`, who wants one sortable folder without uploading anything.
- **Try path**: `pipx install tidemark` then `tidemark --dry-run ./sample-photos` (sample folder ships in the repo). Success = a preview table with old and new names.
- **Cost to try**: free, MIT, offline. Needs Python 3.9+ and `exiftool`.
- **Status**: usable on macOS and Linux. Windows untested. RAW support only for files exiftool can read.
- **The one ask**: tries on unusual cameras, and bug reports with the exact error text.
- **Will not claim**: "fastest", "works with every camera", "never loses a file" (the undo file is good, but it is not a backup).
- **Launch-day owner**: Mei (the maker), free 08:00-13:00 PT on the main day.
