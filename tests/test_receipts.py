import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import receipts as r  # noqa: E402

RECEIPTS = """
| id | kind | claim | evidence |
|----|------|-------|----------|
| R1 | RUN | renames 2,000 photos in 4.1 s | `time tidemark ./dcim` on M2 laptop |
| R2 | SHOWN | dry-run preview table | docs/shots/preview.png |
| R3 | WISH | works on Windows | not tested yet |
"""


def codes(issues):
    return [i[2] for i in issues]


class LoadTests(unittest.TestCase):
    def test_reads_ids_and_kinds(self):
        got = r.load_receipts(RECEIPTS)
        self.assertEqual(got, {1: "RUN", 2: "SHOWN", 3: "WISH"})


class LintTests(unittest.TestCase):
    def test_backed_claim_is_clean(self):
        draft = "I built Tidemark. It renamed 2,000 photos in 4.1 s on my laptop [R1]."
        self.assertEqual(r.lint(draft, RECEIPTS, "x"), [])

    def test_missing_receipt_is_error(self):
        self.assertIn("NO-RECEIPT", codes(r.lint("Fast import [R9].", RECEIPTS)))

    def test_wish_cannot_back_a_claim(self):
        self.assertIn("WEAK-RECEIPT", codes(r.lint("Runs on Windows [R3].", RECEIPTS)))

    def test_bare_number_warns(self):
        self.assertIn("BARE-NUMBER", codes(r.lint("Saves 80% of your time.", RECEIPTS)))

    def test_versions_and_urls_are_not_claims(self):
        draft = "Version 1.2.0 is at https://example.com/a1b2 now."
        self.assertNotIn("BARE-NUMBER", codes(r.lint(draft, RECEIPTS)))

    def test_identifiers_are_not_numbers(self):
        draft = "Folders full of IMG_4412.JPG and DSC00981.ARW."
        self.assertNotIn("BARE-NUMBER", codes(r.lint(draft, RECEIPTS)))
        self.assertIn("BARE-NUMBER", codes(r.lint("大约4秒改完。", RECEIPTS)))

    def test_hype_warns_in_both_languages(self):
        self.assertIn("HYPE", codes(r.lint("The fastest renamer ever.", RECEIPTS)))
        self.assertIn("HYPE", codes(r.lint("史上最强的改名工具。", RECEIPTS)))

    def test_hype_word_inside_other_word_is_fine(self):
        self.assertNotIn("HYPE", codes(r.lint("First-run setup is one command [R2].", RECEIPTS)))
        self.assertNotIn("HYPE", codes(r.lint("It works on the bestiary folder too.", RECEIPTS)))

    def test_vote_ask_is_error(self):
        self.assertIn("VOTE-ASK", codes(r.lint("Please upvote us today!", RECEIPTS)))
        self.assertIn("VOTE-ASK", codes(r.lint("求大家点赞支持。", RECEIPTS)))

    def test_disclosure_needed_for_posts(self):
        self.assertIn("NO-DISCLOSURE", codes(r.lint("Tidemark renames photos [R2].", RECEIPTS, "x")))
        self.assertNotIn("NO-DISCLOSURE", codes(r.lint("我做了一个改名工具 [R2]。", RECEIPTS, "x")))

    def test_title_venues_skip_disclosure_but_check_prefix(self):
        issues = r.lint("Tidemark - rename photos by date", RECEIPTS, "hn-title")
        self.assertNotIn("NO-DISCLOSURE", codes(issues))
        self.assertIn("HN-PREFIX", codes(issues))

    def test_too_long(self):
        self.assertIn("TOO-LONG", codes(r.lint("x" * 61, RECEIPTS, "ph-tagline")))


class LengthTests(unittest.TestCase):
    def test_x_weighting(self):
        self.assertEqual(r.length("abc", "x-weighted"), 3)
        self.assertEqual(r.length("改名", "x-weighted"), 4)
        self.assertEqual(r.length("see https://example.com/very/long/path", "x-weighted"), 4 + 23)

    def test_strip_removes_tags(self):
        self.assertEqual(r.strip_tags("Fast [R1] and safe [R2]."), "Fast and safe.")


if __name__ == "__main__":
    unittest.main()
