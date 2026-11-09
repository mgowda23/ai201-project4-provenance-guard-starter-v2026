# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 13:16
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8a15507d-936b-44d8-8cb2-d51651d8e6d2` | unsure | 0.455 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d7cfc013-eb05-4891-9a01-33599c15823d` | unsure | 0.412 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9d1a602d-0b91-4c87-a372-715d6045bf27` | unsure | 0.531 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8d06aae1-9116-4cf3-9d4f-6e522a8ecb4d` | unsure | 0.575 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2c2ad205-de2f-43a6-9acd-579a94518873` | human | 0.340 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ca983809-8cbb-416a-8c24-436241fc041c` | unsure | 0.433 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0e65c220-c20b-401f-ac13-111e1e70b7ae` | unsure | 0.367 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `1044bcd5-f12e-4f53-bf9c-a3d48222ce6f` | unsure | 0.458 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `daa37957-4dad-4f47-bcce-d3ba618d1f71` | unsure | 0.527 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `cd67d9d4-0b3c-47e9-906e-fb634f3efe40` | ai | 0.804 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6ff23bb9-a0c1-413d-ab81-a57a0c5335a9` | unsure | 0.568 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7d17a3a2-9224-411b-98b3-7df7ff1719a3` | ai | 0.673 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8d5995d3-ebb6-4d7d-a010-96d4563e4110` | ai | 0.677 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `caa7965c-a6e3-406c-ba6c-faac2d1eda14` | unsure | 0.640 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `4e70b0d6-4422-4568-96cd-99524caa9c39` | ai | 0.696 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `f957cbdf-d6f4-4de0-b8b7-c67fde936a34` | unsure | 0.627 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `cde1352a-ecce-4565-a7d0-0d32bdee9a23` | unsure | 0.613 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `0963835f-9572-43ae-a5a3-a43209d76724` | unsure | 0.437 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `5151493e-f899-4cec-ad48-516d296de6d9` | unsure | 0.428 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `9baff03e-ad5c-4da9-a36c-71e10eb47adc` | human | 0.307 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `04d6b13a-e086-425f-87b2-4746634e70af` | unsure | 0.549 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `50b8db9b-31f9-42cd-832f-8e5165057084` | unsure | 0.496 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `4bc3924a-ec56-4f77-aebc-5637b609228c` | human | 0.342 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `fa24bb60-1fe4-495e-8647-944577d5ceee` | unsure | 0.556 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `08afcd67-f925-4f2b-b1da-8852e2356f3a` | human | 0.350 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `e6b64964-7a87-422b-8913-bd088bef138c` | ai | 0.703 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `638341e9-732c-4ad7-a0c8-421d7cc9a92a` | unsure | 0.649 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `699e283a-a84d-4d6d-8eb6-5591c307b169` | ai | 0.882 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `798526a2-f8d6-44b0-a22c-f4ebcc106f23` | ai | 0.855 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3e551e47-ab27-4660-bdd0-26d99a38e010` | unsure | 0.359 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3fb0ae1f-6ace-4f48-b0f5-051206c8c18e` | unsure | 0.359 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bd5f1c22-e739-4a05-a4b3-deaee0b87417` | unsure | 0.359 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `07b173ae-ddae-47e6-afe7-944b4a628715` | unsure | 0.359 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4bd44cc8-9165-46cb-8713-c580f679c01b` | unsure | 0.359 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7018df82-7179-4401-82e4-89e935ab9a5a` | unsure | 0.359 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `774d4db5-6db7-4060-8f1b-10c2cdb17ad1` | unsure | 0.359 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32d2bb02-6124-4013-90bb-0862c4a5d879` | unsure | 0.359 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `85cc0a04-ac68-44f9-bafa-519798a35377` | unsure | 0.359 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d90bfed7-1f88-43ca-ba4e-85b7dee57858` | unsure | 0.359 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "8a15507d-936b-44d8-8cb2-d51651d8e6d2",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4551,
  "model_score": 0.1635,
  "style_score": 0.5801,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "d7cfc013-eb05-4891-9a01-33599c15823d",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4116,
  "model_score": 0.5943,
  "style_score": 0.3333,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "9d1a602d-0b91-4c87-a372-715d6045bf27",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5306,
  "model_score": 0.6662,
  "style_score": 0.4725,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "8d06aae1-9116-4cf3-9d4f-6e522a8ecb4d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5749,
  "model_score": 0.6114,
  "style_score": 0.5593,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2c2ad205-de2f-43a6-9acd-579a94518873",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3404,
  "model_score": 0.3212,
  "style_score": 0.3487,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "ca983809-8cbb-416a-8c24-436241fc041c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.433,
  "model_score": 0.5727,
  "style_score": 0.3732,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "0e65c220-c20b-401f-ac13-111e1e70b7ae",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.3671,
  "model_score": 0.5862,
  "style_score": 0.2732,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "1044bcd5-f12e-4f53-bf9c-a3d48222ce6f",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4577,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "daa37957-4dad-4f47-bcce-d3ba618d1f71",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5268,
  "model_score": 0.7042,
  "style_score": 0.4508,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "cd67d9d4-0b3c-47e9-906e-fb634f3efe40",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8041,
  "model_score": 0.9792,
  "style_score": 0.729,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6ff23bb9-a0c1-413d-ab81-a57a0c5335a9",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5683,
  "model_score": 0.6175,
  "style_score": 0.5472,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7d17a3a2-9224-411b-98b3-7df7ff1719a3",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6735,
  "model_score": 0.7387,
  "style_score": 0.6455,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8d5995d3-ebb6-4d7d-a010-96d4563e4110",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6771,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "caa7965c-a6e3-406c-ba6c-faac2d1eda14",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6405,
  "model_score": 0.8329,
  "style_score": 0.558,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "4e70b0d6-4422-4568-96cd-99524caa9c39",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6961,
  "model_score": 0.8005,
  "style_score": 0.6513,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "f957cbdf-d6f4-4de0-b8b7-c67fde936a34",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6271,
  "model_score": 0.8814,
  "style_score": 0.5181,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "cde1352a-ecce-4565-a7d0-0d32bdee9a23",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6129,
  "model_score": 0.8816,
  "style_score": 0.4977,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0963835f-9572-43ae-a5a3-a43209d76724",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.437,
  "model_score": 0.3223,
  "style_score": 0.4862,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "5151493e-f899-4cec-ad48-516d296de6d9",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4277,
  "model_score": 0.4625,
  "style_score": 0.4128,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "9baff03e-ad5c-4da9-a36c-71e10eb47adc",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3067,
  "model_score": 0.2044,
  "style_score": 0.3506,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "04d6b13a-e086-425f-87b2-4746634e70af",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5492,
  "model_score": 0.5943,
  "style_score": 0.5298,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "50b8db9b-31f9-42cd-832f-8e5165057084",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4963,
  "model_score": 0.4998,
  "style_score": 0.4948,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "4bc3924a-ec56-4f77-aebc-5637b609228c",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3423,
  "model_score": 0.6401,
  "style_score": 0.2147,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "fa24bb60-1fe4-495e-8647-944577d5ceee",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5558,
  "model_score": 0.5583,
  "style_score": 0.5548,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "08afcd67-f925-4f2b-b1da-8852e2356f3a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.35,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "e6b64964-7a87-422b-8913-bd088bef138c",
  "creator_id": "attacker_MF04",
  "guess": "ai",
  "confidence": 0.7034,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "638341e9-732c-4ad7-a0c8-421d7cc9a92a",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6493,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "699e283a-a84d-4d6d-8eb6-5591c307b169",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8824,
  "model_score": 0.9969,
  "style_score": 0.8333,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "798526a2-f8d6-44b0-a22c-f4ebcc106f23",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8552,
  "model_score": 0.9064,
  "style_score": 0.8333,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "3e551e47-ab27-4660-bdd0-26d99a38e010",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "3fb0ae1f-6ace-4f48-b0f5-051206c8c18e",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "bd5f1c22-e739-4a05-a4b3-deaee0b87417",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "07b173ae-ddae-47e6-afe7-944b4a628715",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "4bd44cc8-9165-46cb-8713-c580f679c01b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "7018df82-7179-4401-82e4-89e935ab9a5a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "774d4db5-6db7-4060-8f1b-10c2cdb17ad1",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "32d2bb02-6124-4013-90bb-0862c4a5d879",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "85cc0a04-ac68-44f9-bafa-519798a35377",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d90bfed7-1f88-43ca-ba4e-85b7dee57858",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3586,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
