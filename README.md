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
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



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
  -d @samples/clearly_human.json
```

```json
{
  "confidence": 0.3694,
  "content_id": "a8fcab94-4485-44a3-8c85-0430b485153c",
  "creator_id": "demo_instructor",
  "guess": "unsure",
  "label": "not built yet",
  "model_score": 0.4445,
  "style_score": 0.2943
}
```

`confidence` is the equal average of `model_score` and `style_score`: `(0.4445 + 0.2943) / 2 = 0.3694`. `guess` and `label` are still placeholders.

**An appeal**

Milestone 5. `POST /appeal` still returns 501.

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": null,
      "content_id": "d318774e-5a8a-4bfb-8944-cd44e9e517ed",
      "creator_id": "demo_instructor",
      "guess": "unsure",
      "label": null,
      "model_score": 0.4445,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-03T03:59:02+00:00"
    },
    {
      "combined_score": null,
      "content_id": "42e60d13-d840-4c51-85d7-6a9469b2a589",
      "creator_id": "demo_instructor",
      "guess": "unsure",
      "label": null,
      "model_score": 0.4445,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-11-03T04:11:10+00:00"
    },
    {
      "combined_score": 0.3694,
      "content_id": "a8fcab94-4485-44a3-8c85-0430b485153c",
      "creator_id": "demo_instructor",
      "guess": "unsure",
      "label": null,
      "model_score": 0.4445,
      "status": "decided",
      "style_score": 0.2943,
      "timestamp": "2026-11-03T04:29:36+00:00"
    }
  ]
}
```

The last entry is the submission above. `model_score`, `style_score`, and `combined_score` are all filled in. The earlier lines are from before the style signal was wired, so those two scores are null there.

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

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
