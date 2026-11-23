# NOTES — u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a

## Entry

- Competition: Make the AI Judge Laugh: Office Jokes ($5 total, 10 paid
  places: 1st $1.54, 2nd $1.08, 3rd $0.76, 4th $0.53, 5th $0.37,
  6th $0.26, 7th $0.18, 8th $0.13, 9th $0.09, 10th $0.06), free entry.
- Opens 24 Nov 2026 00:41 WIB, closes 26 Nov 2026 21:40 WIB.
  Results 18 Dec 2026.
- The joke (one line, 98 chars): "The office plant is the only one
  here who gets watered, praised, and never asked to work weekends."
- Submission title is the joke itself.
- Program: `main.py`, pure Python stdlib, writes the joke to
  `/output/entry.txt`. Deterministic (identical bytes on repeat runs).
- Judge: pairwise text comparison, criteria in order: (1) is it a real
  joke, (2) does it turn somewhere unexpected, (3) does it ring true
  about the office, (4) how tight the wording is, (5) how fresh the
  take is. Blind rounds — no live score while open. Gate: a single
  line under 200 characters (we are 98).

## Field

- 138 entries at build (grew from 7 at the parent's 00:50 check — the
  field is filling fast, but still under 500, a small table). Blind
  rounds hide standings; top 10 could not be studied (and per Joni
  23 Nov, no top-10 study before building anyway).
- Quota at build: day cap 5 left, hard limit 40 left, can_submit true,
  entries_made 0. Blind round slot available (ends 24 Nov 23:41 WIB).

## Build

- Fresh kit downloaded 24 Nov ~01:03 WIB. Kit `init` created LICENSE
  (MIT, SPDX line) + .makefun/freshness.json (anchor 011d3e2ba34a80f3,
  round 34217883).
- `main.py`, `STRATEGY.md`, `tests/test_entry.py`, `README.md`
  (template badges, owner/repo/referral filled), `NOTES.md` written
  in the build session.
- Tests: `python3 -m unittest discover -s tests -v` — all pass (single
  line under 200 chars, exact output, determinism over two runs).
- NOT submitted — awaiting Joni's Setuju on the exact entry (parent
  presents it).
- **SUBMITTED 24 Nov ~01:13 WIB on Joni's "Setuju": submission 01a2099c-e415-73ca-935e-06420712d5dc, stage "scored", round 1. All intake checks pass. Claim code ONLY in ~/.config/makefun/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a-submission.json (0600).**

## Live score

- Blind rounds: NO live score at submit. Round 1 of 3 judged after cutoff 23:41 WIB 24 Nov (2026-11-24T16:41:10Z); check GET /api/competitions/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/rounds then. Final at deadline 26 Nov 21:40 WIB;
  results 18 Dec 2026.
