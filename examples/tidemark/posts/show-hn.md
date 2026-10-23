I built Tidemark because my photo backups were 14 folders of IMG_4412.JPG and DSC00981.ARW from four cameras and three phones, and every tool I tried either wanted to import everything into a library or renamed files with no way back.

It is a small command-line tool. It reads the capture date and shows a dry-run table of old and new names before it touches anything [R2]. When you confirm, it renames and writes an undo file that puts every name back [R4]. If six shots share the same second, they get -1, -2 and so on instead of overwriting each other [R5]. It has no network code; nothing leaves your machine [R6].

On my 2022 laptop it renamed a 2,000-file test set in about 4 seconds [R1].

Try it: `pipx install tidemark`, then `tidemark --dry-run ./sample-photos` (a sample folder is in the repo). It needs exiftool; the README has the install line.

Limits: I have not tested it on Windows at all. Format support is whatever exiftool can read, so odd RAW files may fail. The undo file is not a backup.

What would help most: run it on files from an unusual camera or phone and, if it fails, paste the error text in a reply or an issue.
