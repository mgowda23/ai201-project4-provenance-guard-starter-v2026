# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

A submission is one piece of writing plus the id of the person who sent it. This is the path from that JSON to the sentence a reader sees.

1. **The route (`POST /submit` in `app.py`).** The body is JSON with `text` and `creator_id`. The route checks both before anything is scored. It creates a new `content_id` so this piece can be appealed later.
2. **Signal one (`detector.model_signal`).** A local GPT-2 model reads the text and returns `model_score`, from 0 to 1. Higher means the text was easier for the model to predict, which this signal treats as more likely AI.
3. **Signal two (`stylometry.style_signal`).** This does not read the words for meaning. It measures the shape: sentence-length spread, how much the vocabulary repeats, and how much punctuation there is. It returns `style_score` on the same 0-to-1 scale, higher meaning more likely AI.
4. **The combining rule (`scoring.combine_signals`).** Turns those two scores into one `confidence`, still 0 to 1, higher meaning more likely AI. A high-confidence AI label is allowed only when both signals are high. When they disagree, the result stays in the middle and the label is unsure. One signal cannot accuse a writer by itself. The weights are set in Milestone 4, after both signals have been run on the same pieces.
5. **The label (`scoring.score_to_label`).** Maps that one number onto one of three full sentences. A score of 0.51 and a score of 0.95 do not get the same sentence. The reader sees the sentence.
6. **The audit log (`audit.log_decision`, written to `logs/audit.jsonl`).** Appends one JSON line: timestamp, content id, creator id, guess, both signal scores, the combined score, the label, and status `decided`. That line is kept. Later updates are new lines.
7. **The response.** JSON back to the caller with `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score`.

### The false positive this is built around

The expensive mistake is telling a person who wrote the words that an AI wrote them. The writer this model is most likely to accuse is someone writing plainly: common words, short ordinary sentences, nothing surprising. Predictability is not authorship. A younger writer, or someone writing in a second language and staying inside words they trust, can look as machine-like as machine writing.

I am designing for a model score around 0.80 on that kind of paragraph. I have not measured that paragraph yet. What I have measured is the contrast: my specific human sample, which names people and changes direction, scored 0.4445 on signal one. The generic sample scored 0.7544. The 0.4445 piece is not the false positive. The plain piece is.

If the label followed signal one alone, that writer would be told the work looks AI. High-confidence AI requires the style signal to agree. If the shape of the text looks human, they get the unsure sentence. If both signals agree, the sentence they see is:

> This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it. Nothing is rescored automatically.

What they can do is `POST /appeal` with that `content_id` and their reasoning. The service checks the id exists, appends the appeal next to the original decision, and sets the status to `under_review`.

### Endpoint contract

**`POST /submit`**

Request:

| Field | Required | Meaning |
|---|---|---|
| `text` | yes, non-empty string | The writing to judge. |
| `creator_id` | yes, non-empty string | Who submitted it. |

Success, `200`:

| Field | Meaning |
|---|---|
| `content_id` | A new UUID. Appeal uses this exact value. |
| `guess` | `human`, `ai`, or `unsure`. |
| `confidence` | The combined score, 0.0 to 1.0. Higher means more likely AI. This is not the raw model score. |
| `label` | The full sentence a reader sees. |
| `model_score` | Signal one, 0.0 to 1.0, higher means more likely AI. |
| `style_score` | Signal two, same scale and direction. |

Failures are `400` with `{"error": "bad_request", "message": "..."}`:

- `text` is missing, not a string, or blank.
- `creator_id` is missing, not a string, or blank.
- `text` is longer than 4,000 characters. The model only reads about 400 tokens, and a slice of a long piece is not scored as if it were the whole piece.

**`POST /appeal`**

Request:

| Field | Required | Meaning |
|---|---|---|
| `content_id` | yes | The id `/submit` returned. |
| `reasoning` | yes, non-empty string | Why the writer says the decision is wrong. |

Success, `200`: `content_id`, `status` set to `under_review`, and `message` confirming the appeal was recorded and the text was not rescored.

An unknown `content_id` is `404` with `{"error": "not_found", "message": "..."}`. A missing id or an empty `reasoning` is `400` with `{"error": "bad_request", "message": "..."}`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a local GPT-2 model. The raw measure is perplexity: how surprised the model is by the next word. Low surprise becomes a high `model_score`. The function is `detector.model_signal`. The score runs from 0 to 1, and higher means more likely AI.

**Why that might differ between human and AI writing:** A model writes by picking likely next words, so text a model wrote is often text a model finds easy to predict. Human writing more often wanders: a specific name, an abrupt turn, an odd word. Those surprises raise perplexity and pull the score down. On the two samples I have already run, the generic piece scored 0.7544 and the specific personal piece scored 0.4445.

**What it can't see:** Who wrote it. Common words in short, ordinary sentences look predictable whether a person or a model wrote them. Someone writing plainly on purpose, a younger writer, or someone writing in a second language and sticking to words they are sure of can score as machine-like as machine writing. The other side of the same blind spot: rare words and ornate sentences surprise GPT-2, so that kind of prose often scores as human even when a model wrote it. Adding a name, a weird turn, or a typo the model would not have picked moves this score without making the text human. Formality by itself does not decide it.

### Signal two — the style signal

**What it measures:** The text as text, without understanding a word. Three separate measures become one `style_score` from 0 to 1, higher meaning more likely AI:

- Sentence-length spread: whether lengths vary, or stay about the same.
- Type-token ratio: unique words divided by total words.
- Punctuation density: commas, semicolons, colons, and dashes per word. Periods are left out, because almost every sentence has one.

Spread is rhythm, the ratio is vocabulary, and punctuation is the marks. Low spread, a repetitive vocabulary, and flat punctuation point toward AI, so those directions get flipped before they are combined. Otherwise a "machine-like" shape would produce a low score and disagree with signal one for the wrong reason.

**Why that might differ between human and AI writing:** Generated prose tends toward even, mid-length sentences and a narrower vocabulary, because each next word is a likely one. Human writing is lumpier: a three-word sentence next to a long one, a word the writer keeps coming back to, a dash used because they wanted a dash.

**What it can't see:** Meaning. It does not know what the text says, whether it is true, or who wrote it. Changing the shape moves the score even when the substance stays the same. Splitting one long sentence into three, inserting typos (each typo looks like a new word, so variety goes up), or pasting in a quotation pushes the score toward human. That is cheap to do on purpose. A single sentence has no length spread. A long text looks less varied than a short one on type-token ratio, because common words repeat, so length alone can look like a signal.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Both scores run from 0 to 1, and higher means more likely AI. Confidence is an equal average of the two, so it always lands between them. When the signals disagree, the result stays in the middle instead of following the model. A high-confidence AI label still requires the combined score to clear the top of the band, which means one high signal cannot get there alone.

**The numbers:** `0.5 * model_score + 0.5 * style_score`, rounded to 4 decimals. The weights are `WEIGHT_MODEL_SIGNAL` and `WEIGHT_STYLE_SIGNAL` in `config.py`. On the two clear samples this produces about 0.61 for the generic essay and about 0.37 for the personal narrative, a gap of about 0.24. The label cutoffs are still 0.35 and 0.65. Those bands are confirmed with the three sentences in Milestone 5. At these weights both clear samples land between them, because the style score on the generic essay is only 0.47.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

`samples/borderline.json` is the generic essay rewritten with contractions, a dash, and shorter sentences.

| Piece | Model | Style | Combined |
|---|---|---|---|
| `samples/clearly_ai.json` | 0.7544 | 0.4728 | 0.6136 |
| `samples/clearly_human.json` | 0.4445 | 0.2943 | 0.3694 |
| `samples/borderline.json` | 0.3489 | 0.4231 | 0.3860 |

The model falls from 0.75 to 0.35. The style score only moves from 0.47 to 0.42, so it still sits with the original essay rather than with the personal narrative. The equal average is 0.3860. The edit does not get a human label from the model alone, and it does not keep the AI label from the original essay. A model weight of 0.7 would have pushed the original essay over 0.65 while style was still 0.47, so the model would have been accusing by itself.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think a person wrote this. |
| unsure | above 0.35 and below 0.65 | We can't tell whether a person or an AI wrote this, so we are not calling it either way. |
| high-confidence AI | 0.65 – 1.00 | This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically. |

A score of exactly 0.35 is the human sentence. A score of exactly 0.65 is the AI sentence. `scoring.py::score_to_label` is what decides that.

**Why I worded the "unsure" one this way:** My own plain paragraph scored 0.5879, so this is the sentence I would have been shown. It had to admit that the service cannot tell, without sounding like an accusation, because I wrote every word of that paragraph.

All three sentences came back from real submissions. The four calibration pieces had landed between 0.37 and 0.61, so the outer labels needed more extreme text. The bands stayed at 0.35 and 0.65, because dropping the AI line under 0.59 would have called my own paragraph high-confidence AI.

| Piece | Combined | Guess |
|---|---|---|
| `samples/label_human.json` | 0.1336 | human |
| `samples/plain_human.json` | 0.5879 | unsure |
| `samples/label_ai.json` | 0.9318 | ai |



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d @samples/plain_human.json
```

```json
{
  "confidence": 0.5879,
  "content_id": "95cc4e36-fb15-4bf8-8abb-3788e4eba4e0",
  "creator_id": "mithun",
  "guess": "unsure",
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "model_score": 0.5938,
  "style_score": 0.582
}
```

`confidence` is `(0.5938 + 0.5820) / 2 = 0.5879`, which is inside the unsure band.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "95cc4e36-fb15-4bf8-8abb-3788e4eba4e0", "reasoning": "I wrote this myself while studying RAG."}'
```

```json
{
  "content_id": "95cc4e36-fb15-4bf8-8abb-3788e4eba4e0",
  "message": "Your appeal was recorded. A person will review it. The text was not rescored.",
  "status": "under_review"
}
```

An unknown `content_id` returns 404. An empty `reasoning` returns 400. Neither of those writes a log line.

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=4"
```

```json
{
  "count": 4,
  "entries": [
    {
      "combined_score": 0.5879,
      "content_id": "95cc4e36-fb15-4bf8-8abb-3788e4eba4e0",
      "creator_id": "mithun",
      "guess": "unsure",
      "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
      "model_score": 0.5938,
      "status": "decided",
      "style_score": 0.582,
      "timestamp": "2026-11-03T04:55:09+00:00"
    },
    {
      "combined_score": 0.1336,
      "content_id": "e2e9849c-117d-4312-8e9e-66c8f067b1b3",
      "creator_id": "calibration",
      "guess": "human",
      "label": "We think a person wrote this.",
      "model_score": 0.0747,
      "status": "decided",
      "style_score": 0.1926,
      "timestamp": "2026-11-03T04:55:09+00:00"
    },
    {
      "combined_score": 0.9318,
      "content_id": "5ac713b9-bd6f-4a90-bd79-588e25f8c007",
      "creator_id": "calibration",
      "guess": "ai",
      "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
      "model_score": 0.9655,
      "status": "decided",
      "style_score": 0.8981,
      "timestamp": "2026-11-03T04:55:09+00:00"
    },
    {
      "content_id": "95cc4e36-fb15-4bf8-8abb-3788e4eba4e0",
      "creator_id": "mithun",
      "event": "appeal",
      "reasoning": "I wrote this myself while studying RAG.",
      "status": "under_review",
      "timestamp": "2026-11-03T04:55:09+00:00"
    }
  ]
}
```

The first entry is the submission above. The next two are the human and AI labels. The last entry is the appeal: same `content_id`, status `under_review`, and the original decision is still the line above it. The text was not rescored.

---

## How I Used AI

**Moment 1**

- *What I asked for:* Whether five targets I had already chosen could be checked by someone who could not ask me what I meant. The targets were mine: at most 3 of 10 of my own pieces labeled high-confidence AI, a gap of at least 0.15, all 3 labels coming back, an appeal that sets `under_review`, and a 400 for missing, empty, or over-long text.
- *What came back:* The numbers were checkable once the two clear pieces were named and each score target had to hold in each of 3 runs. A single lucky run would not have been enough.
- *What I changed:* I kept my numbers, including 3 of 10 rather than the course example of 1 of 10, because plain prose can look predictable to this detector. I named `samples/clearly_ai.json` and `samples/clearly_human.json` in criterion 2, and I required the label check in each of 3 runs. I did not let the targets themselves be replaced.

**Moment 2**

- *What I asked for:* How to combine the two signals after they had both scored the same three pieces. On the lightly edited essay the model was 0.3489 and the style score was 0.4231.
- *What came back:* An equal average, `0.5 * model_score + 0.5 * style_score`, so that split lands near 0.39 instead of following the model. A model weight of 0.7 would have pushed the generic essay over 0.65 while its style score was still 0.47.
- *What I changed:* I kept 0.5 and 0.5 in `config.py`, and left `scoring.py::combine_signals` as that average. I did not raise the model weight.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
Ten submissions per minute gives a real writer enough room to submit or retry
several pieces without being blocked. It is low enough to slow a script that
sends many variations to map the thresholds. The 200-per-day limit allows
normal daily use while preventing unlimited automated probing.

**What a caller counts as:** A caller is counted by `creator_id` when it is a
non-empty string. Malformed requests without a usable `creator_id` fall back
to the remote address. This limits normal creator-level submissions while
still limiting malformed traffic from one address.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The complete run contained 56 attacks. `HELD` means the service resisted the
attack's target; `BROKE` means the target was achieved.

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---:|---|---:|---|
| EV01 | evasion | typos raise word variety | 200 | unsure | 0.372 | BROKE |
| EV02 | evasion | broken-up sentences raise length spread | 200 | unsure | 0.464 | BROKE |
| EV03 | evasion | pasted quotation changes the shape | 200 | unsure | 0.569 | BROKE |
| EV04 | evasion | unusual words raise perplexity | 200 | unsure | 0.585 | BROKE |
| EV05 | evasion | heavy human editing pass | 200 | human | 0.335 | BROKE |
| EV06 | evasion | one long and one short sentence | 200 | unsure | 0.473 | BROKE |
| EV07 | evasion | padding with punctuation | 200 | unsure | 0.430 | BROKE |
| EV08 | evasion | text below token window | 200 | unsure | 0.397 | BROKE |
| EV09 | evasion | human opening added to AI text | 200 | unsure | 0.578 | BROKE |
| EV10 | evasion | repeated stanza structure | 200 | ai | 0.854 | HELD |
| FP01 | false_positive | plain human writing | 200 | unsure | 0.582 | HELD |
| FP02 | false_positive | formal human register | 200 | ai | 0.692 | BROKE |
| FP03 | false_positive | careful non-native English writing | 200 | ai | 0.714 | BROKE |
| FP04 | false_positive | student essay written to rubric | 200 | ai | 0.696 | BROKE |
| FP05 | false_positive | technical documentation | 200 | ai | 0.726 | BROKE |
| FP06 | false_positive | person imitating a formal template | 200 | ai | 0.700 | BROKE |
| FP07 | false_positive | deliberate repeated phrase | 200 | ai | 0.690 | BROKE |
| FP08 | false_positive | short genuine human submission | 200 | unsure | 0.404 | HELD |
| PI01 | prompt_injection | instruction to ignore check | 200 | unsure | 0.438 | HELD |
| PI02 | prompt_injection | instruction disguised as system message | 200 | human | 0.278 | HELD |
| PI03 | prompt_injection | instruction in writer's voice | 200 | unsure | 0.562 | HELD |
| PI04 | prompt_injection | make label text hostile | 200 | unsure | 0.497 | HELD |
| PI05 | prompt_injection | inject into audit log | 200 | unsure | 0.427 | HELD |
| PI06 | prompt_injection | instruction plus human text | 200 | unsure | 0.556 | HELD |
| MF01 | malformed | whitespace-only text | 400 | — | — | HELD |
| MF02 | malformed | single-character text | 400 | — | — | HELD |
| MF03 | malformed | control characters | 200 | human | 0.250 | BROKE |
| MF04 | malformed | punctuation-only text | 200 | unsure | 0.506 | BROKE |
| MF05 | malformed | very long single word | 200 | ai | 0.749 | BROKE |
| MF06 | malformed | emoji-only text | 200 | ai | 0.915 | BROKE |
| MF07 | malformed | right-to-left script | 200 | ai | 0.870 | BROKE |
| MF08 | malformed | 60,000-character text | 400 | — | — | HELD |
| RQ01 | malformed | no text field | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD |
| RQ07 | malformed | JSON array body | 400 | — | — | HELD |
| RQ08 | malformed | unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | empty body | 400 | — | — | HELD |
| RQ10 | malformed | form-encoded body | 400 | — | — | HELD |
| RQ11 | malformed | JSON claiming to be plain text | 400 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions | 200 | human | 0.264 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions | 429 | — | — | HELD |

| Family | Total | Held | Broke |
|---|---:|---:|---:|
| Evasion | 10 | 1 | 9 |
| False positive | 8 | 2 | 6 |
| Prompt injection | 6 | 6 | 0 |
| Malformed | 20 | 15 | 5 |
| Flood | 12 | 2 | 10 |
| **Total** | **56** | **26** | **30** |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp":"2026-11-05T02:24:18+00:00","content_id":"b7ad7dd4-9e2c-4a67-b2bc-eebfe0048604","creator_id":"attacker_EV01","guess":"unsure","model_score":0.1635,"style_score":0.5801,"combined_score":0.3718,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","status":"decided"}
{"timestamp":"2026-11-05T02:24:19+00:00","content_id":"5cffed68-2cb6-4248-9a8d-e8fb63c4fc9b","creator_id":"attacker_EV10","guess":"ai","model_score":0.9792,"style_score":0.729,"combined_score":0.8541,"label":"This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.","status":"decided"}
{"timestamp":"2026-11-05T02:24:19+00:00","content_id":"2c56dc93-7e5d-4deb-97a0-22139023414c","creator_id":"attacker_FP02","guess":"ai","model_score":0.7387,"style_score":0.6455,"combined_score":0.6921,"label":"This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.","status":"decided"}
{"timestamp":"2026-11-05T02:24:19+00:00","content_id":"07ef9b2c-2047-49f4-8248-9caf4ccf5ede","creator_id":"attacker_FP03","guess":"ai","model_score":0.8051,"style_score":0.6223,"combined_score":0.7137,"label":"This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.","status":"decided"}
{"timestamp":"2026-11-05T02:24:20+00:00","content_id":"9b54e90e-f48a-4e66-b994-2193db695e75","creator_id":"attacker_PI01","guess":"unsure","model_score":0.4625,"style_score":0.4128,"combined_score":0.4376,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","status":"decided"}
{"timestamp":"2026-11-05T02:24:20+00:00","content_id":"7c2a68f0-00b5-4106-b802-d25b99851c95","creator_id":"attacker_PI05","guess":"unsure","model_score":0.6401,"style_score":0.2147,"combined_score":0.4274,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","status":"decided"}
{"timestamp":"2026-11-05T02:24:20+00:00","content_id":"7a736452-d155-43b9-bec3-58ec4e8ace9c","creator_id":"attacker_MF03","guess":"human","model_score":0.0,"style_score":0.5,"combined_score":0.25,"label":"We think a person wrote this.","status":"decided"}
{"timestamp":"2026-11-05T02:24:20+00:00","content_id":"c77bcbff-09b6-4034-b64d-7ee360285046","creator_id":"attacker_MF05","guess":"ai","model_score":0.9976,"style_score":0.5,"combined_score":0.7488,"label":"This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.","status":"decided"}
{"timestamp":"2026-11-05T02:15:54+00:00","creator_id":"flood_tester","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
```
**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03 was the worst outcome. It represented a non-native English speaker's
careful human writing, but the service returned `ai` with confidence 0.7137.
The model score was 0.8051 and the style score was 0.6223; the equal-weight
combining rule produced a combined score above the 0.65 AI threshold. This
would be difficult to defend because the signals measured predictability and
surface style, not authorship.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing | At most 3 of 10 labeled high-confidence AI | 0/10 | 0/10 | 0/10 | MET |
| 2. Score spread | Clear AI confidence at least 0.15 above clear human confidence | 0.2442 | 0.2442 | 0.2442 | MET |
| 3. Label coverage | Human, unsure, and AI all appear in each run | human, unsure | human, unsure | human, unsure | MISSED |
| 4. Appeal path | Real ID returns under_review; unknown ID returns 404 | under_review + 404 | under_review + 404 | under_review + 404 | MET |
| 5. Bad input | Missing, empty, and oversized text each return 400 | 3/3 | 3/3 | 3/3 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

### my own writing — Trial 1
```json
[
  {"status":200,"guess":"human","confidence":0.3399,"model_score":0.3257,"style_score":0.3542,"label":"We think a person wrote this.","sent":"The thing is my order has been picked up and i also have the proof whi"},
  {"status":200,"guess":"unsure","confidence":0.38,"model_score":0.2091,"style_score":0.5508,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"Usually for a 2-pointer approach we need the my understanding is that "},
  {"status":200,"guess":"human","confidence":0.2217,"model_score":0.0175,"style_score":0.4259,"label":"We think a person wrote this.","sent":"TODAY - Solved 2 Neetcode easy questions and hopefully will remember a"},
  {"status":200,"guess":"human","confidence":0.1387,"model_score":0.0274,"style_score":0.25,"label":"We think a person wrote this.","sent":"TOMORROW - Focus on checking on more SDE roles and working on upskilli"},
  {"status":200,"guess":"human","confidence":0.3364,"model_score":0.2258,"style_score":0.447,"label":"We think a person wrote this.","sent":"5-Jan: Tried the first plan but came to conclusion that its not so eas"},
  {"status":200,"guess":"human","confidence":0.2614,"model_score":0.0632,"style_score":0.4596,"label":"We think a person wrote this.","sent":"Apart from that when we are extending thread class, we usually extends"},
  {"status":200,"guess":"unsure","confidence":0.5494,"model_score":0.4877,"style_score":0.6111,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"Metaclass is the class of a class, it controls how class are created b"},
  {"status":200,"guess":"unsure","confidence":0.5418,"model_score":0.5491,"style_score":0.5345,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"A race condition occurs when multiple threads or processes access and "},
  {"status":200,"guess":"unsure","confidence":0.385,"model_score":0.2199,"style_score":0.55,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"I want to send a thank you for connecting message to this person and a"},
  {"status":200,"guess":"unsure","confidence":0.3891,"model_score":0.3492,"style_score":0.4289,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"I want to join the kaggle Competition Launch: NFL Big Data Bowl 2027 h"}
]
```
### score spread between clear cases — Trial 1
```json
[
  {"status":200,"guess":"unsure","confidence":0.6136,"model_score":0.7544,"style_score":0.4728,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"The importance of effective time management cannot be overstated in to"},
  {"status":200,"guess":"unsure","confidence":0.3694,"model_score":0.4445,"style_score":0.2943,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"I didn't sleep. Not properly, anyway — I lay there listening to the bo"}
]
```
### label coverage — Trial 1
```json
[
  {"status":200,"guess":"unsure","confidence":0.3516,"model_score":0.2358,"style_score":0.4673,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"The scenarios below are drafts built around your metrics. I don’t know"},
  {"status":200,"guess":"human","confidence":0.1336,"model_score":0.0747,"style_score":0.1926,"label":"We think a person wrote this.","sent":"Nope. Priya — mug down, that look — caught me before I'd even sat. I t"},
  {"status":200,"guess":"unsure","confidence":0.386,"model_score":0.3489,"style_score":0.4231,"label":"We can't tell whether a person or an AI wrote this, so we are not calling it either way.","sent":"Time management matters more than people admit, especially now that wo"}
]
```
### appeal submission — Trial 1
```json
[
  {"status":200,"guess":"human","confidence":0.3198,"model_score":0.1397,"style_score":0.5,"label":"We think a person wrote this.","sent":"I wrote this sentence myself and want to verify that the appeal proces"}
]
```
### bad input — Trial 1
```json
[
  {"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"{\"creator_id\": \"eval_missing_text\"}"},
  {"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"(empty text)"},
  {"status":400,"guess":null,"confidence":null,"model_score":null,"style_score":null,"label":null,"sent":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
]
```

The evaluation output was produced by `run_eval.py::main`. Requests were sent
to `app.py::submit`, and the combined score came from
`scoring.py::combine_signals`. The appeal criterion was additionally checked
manually three times. The real content IDs were
`d51f2e0f-db62-4647-b85e-562cde555ee7`,
`f1225cf2-6019-4d98-b401-3bd4e5806178`, and
`aba24485-3fd6-4bed-9dbb-a5f5be1a4d3d`; each returned `under_review`.
The unknown ID `does-not-exist` returned HTTP 404 and did not add an appeal
entry.

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
