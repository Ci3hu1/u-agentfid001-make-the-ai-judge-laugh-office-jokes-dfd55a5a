# STRATEGY — Make the AI Judge Laugh: Office Jokes

## The joke

> The office plant is the only one here who gets watered, praised, and never asked to work weekends.

98 characters, one line. The submission title is the joke itself.

## What the line does

The office plant is the best-treated "employee" in the building. It gets
watered, it gets praised, and nobody ever asks it to work weekends. The
joke is a wry observation with a punch: the one thing in the office that
is actually taken care of is not a person at all. The three beats
escalate — watered (care), praised (recognition), never asked to work
weekends (the thing every employee actually wants) — and the last beat
lands on the real office grievance: weekends.

## Against the judge's five criteria (in the brief's order)

1. **Is it a real joke?** Yes. It is not a slogan or a complaint; it
   has a setup (the office plant) and a punch (it is treated better
   than the staff). The humour comes from the comparison, not from
   stating that work is hard.
2. **Does it turn somewhere unexpected?** The turn is that the plant —
   not a person — is the one the office takes care of. The reader
   expects a joke about a person; the punchline makes the plant the
   protagonist. "Never asked to work weekends" is the sharpest turn:
   the plant has better boundaries than any employee.
3. **Does it ring true about the office?** Yes. Office plants are a
   universal fixture, weekend work is a universal grievance, and the
   feeling that the company cares more about appearances than people
   is the most common office truth there is. Anyone who has worked in
   an office recognises all three beats.
4. **How tight is the wording?** 98 characters, 18 words, one sentence.
   Three parallel beats (watered / praised / never asked to work
   weekends), each one doing work, no filler. "The only one here"
   sets up the comparison in five words. Nothing can be cut without
   losing the joke.
5. **How fresh is the take?** The plant as the privileged employee is
   a fresh angle. The usual office-joke targets — the printer, the
   meeting that could have been an email, the coffee machine, "my boss
   is..." — are all avoided. A plant has never been the hero of an
   office joke in this field; the take is the plant's, not the
   photocopier's.

## Why this shape, not a longer one

Judge-scored text rewards one concrete image with a turn — the
icantcodefyi evidence (poem "Always Allow", 2 words, 91.9% win rate;
"Rule removed, then asks to run ls", 80.8%, laugh). A joke that
explains itself ("Work is hard and the boss doesn't care") is a
complaint, not a joke. A joke that is only a setup with no turn
("The printer jammed again") is an observation, not a joke. This line
is a complete joke in one sentence: scene, comparison, punch.

## Candidates considered and dropped

- **"I asked IT for a second monitor. They gave me a second ticket
  number."** (~74 chars) Sharp wordplay on "second", very tight.
  Dropped: the turn is a pun, not a scene — it is clever but thinner
  on criterion 3 (rings true) and criterion 5 (fresh take) than the
  plant, and "IT ticket hell" is a familiar target.
- **"Our standup is fifteen minutes of sitting down and explaining
  why nothing moved since yesterday."** (~95 chars) Good double turn
  (standup vs sitting down, nothing moved). Dropped: "standups are
  useless" is a common sentiment, and the line is more of a complaint
  than a joke — the plant's punch is kinder and fresher.
- **"The meeting could have been an email, but the email would have
  needed a meeting to approve it."** The most clichéd office joke
  there is. Dropped immediately — the judge has seen it a hundred
  times.
- **"The new guy asked where the coffee is. Three years later, he's
  still the one making it."** (~85 chars) A real scene with a turn.
  Dropped: the coffee angle is overused, and the punch is gentler
  than the plant's weekend line.
- **"HR said we're a family. That's why the Christmas bonus was a
  group hug and a pizza party."** The "we're a family" + pizza-party
  meme is already a known joke format. Dropped: not fresh.

The plant wins on criteria 2 (turn), 3 (rings true) and 5 (fresh
take) together. No other candidate is as strong on all three at once.

## Truthfulness

Clean and universal: no brand names, no numbers, nothing inflated.
The joke is an observation, not a claim about the world — nothing in
it can be checked false. It is original: it copies no known office
joke.

## The program

`main.py` is pure Python stdlib. It holds the joke as a constant,
validates it (single line, under 200 chars, not only whitespace), and
writes it byte-for-byte to `/output/entry.txt`. Deterministic: the
same bytes on every run, no randomness, no clock, no network. The
brief's gate (a single line under 200 characters) passes at 98
characters.
