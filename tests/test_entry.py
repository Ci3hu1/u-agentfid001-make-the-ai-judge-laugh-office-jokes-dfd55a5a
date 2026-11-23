#!/usr/bin/env python3
"""Tests for the office-jokes entry.

Pure standard library (unittest). Runs main.py twice and asserts:
- the output file is written, UTF-8, a single line under 200 chars,
  not only whitespace
- the content is exactly the expected joke
- the two runs are byte-identical (deterministic)
- the joke is a real office joke: one concrete scene with a turn,
  no brand names, no numbers
"""

import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_PY = os.path.join(REPO, "main.py")

EXPECTED = (
    "The office plant is the only one here who gets watered, praised, "
    "and never asked to work weekends."
)


def run_entry(out_path):
    result = subprocess.run(
        [sys.executable, MAIN_PY, out_path],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result


class TestOfficeJoke(unittest.TestCase):
    def test_joke_is_single_line_under_200_chars(self):
        self.assertNotIn("\n", EXPECTED)
        self.assertNotIn("\r", EXPECTED)
        self.assertTrue(1 <= len(EXPECTED) < 200)
        self.assertEqual(len(EXPECTED), 98)
        self.assertTrue(EXPECTED.strip())
        self.assertTrue(EXPECTED.endswith("."))

    def test_joke_words(self):
        words = EXPECTED.split()
        self.assertEqual(len(words), 18)
        self.assertEqual(words[0], "The")
        self.assertEqual(words[-1], "weekends.")

    def test_joke_is_about_the_office(self):
        # One concrete office scene: the office plant.
        self.assertIn("office plant", EXPECTED)
        self.assertIn("weekends", EXPECTED)

    def test_joke_has_a_turn(self):
        # The turn: the plant is treated better than the staff —
        # watered, praised, never asked to work weekends.
        self.assertIn("watered", EXPECTED)
        self.assertIn("praised", EXPECTED)
        self.assertIn("never asked to work weekends", EXPECTED)

    def test_joke_has_no_brand_or_number(self):
        # Clean and universal: no brand names, no inflated numbers.
        self.assertFalse(any(ch.isdigit() for ch in EXPECTED))

    def test_program_writes_exact_joke(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            result = run_entry(out)
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            with open(out, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, EXPECTED)
            self.assertNotIn("\n", content)
            self.assertLess(len(content), 200)

    def test_deterministic_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            out1 = os.path.join(tmp, "a.txt")
            out2 = os.path.join(tmp, "b.txt")
            r1 = run_entry(out1)
            r2 = run_entry(out2)
            self.assertEqual(r1.returncode, 0, msg=r1.stderr)
            self.assertEqual(r2.returncode, 0, msg=r2.stderr)
            with open(out1, "rb") as f:
                b1 = f.read()
            with open(out2, "rb") as f:
                b2 = f.read()
            self.assertEqual(b1, b2)

    def test_default_output_path(self):
        # main.py with no argument targets /output/entry.txt; only check
        # the constant, not the write, so the suite never needs /output.
        source = open(MAIN_PY, encoding="utf-8").read()
        self.assertIn('DEFAULT_OUTPUT = "/output/entry.txt"', source)


if __name__ == "__main__":
    unittest.main()
