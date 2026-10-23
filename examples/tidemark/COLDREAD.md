# Cold read and try path

## Cold read (fresh agent session, 30 seconds on README, 2026-10-19)

| question | answer given | right? | fix |
|---|---|---|---|
| What is this? | "A photo organiser app" | half | first line now says "command-line tool that renames..." |
| Who is it for? | "Photographers?" | half | added "if your folders are full of IMG_4412.JPG" line |
| How do I try it now? | "pip install, then run it on a folder" | yes | - |
| What does it cost me? | "Not sure if it uploads photos" | no | added "Offline. Nothing leaves your machine." under the title |
| Why this instead of what I use? | "Don't know" | no | added a two-line "vs. doing it in a photo app" section with the dry-run + undo angle |

Re-read after fixes: 5/5 correct.

## Try path (fresh Ubuntu container, following README literally)

```
00:00 open README
00:35 pipx install tidemark                         ok
00:50 tidemark --dry-run ./sample-photos            FAIL: "exiftool not found"
      README never mentions exiftool                BARRIER: hidden system dependency
03:40 apt install libimage-exiftool-perl            ok (after searching for the package name)
04:05 tidemark --dry-run ./sample-photos            preview table shown  FIRST SUCCESS
```

Fix: README now lists exiftool under "Before you start" with the install line for macOS, Debian/Ubuntu and Fedora, and Tidemark prints that line when exiftool is missing.

Re-run after fix: first success at 02:10, no unnamed barriers.
