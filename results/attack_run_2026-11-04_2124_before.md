# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 21:24
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `b7ad7dd4-9e2c-4a67-b2bc-eebfe0048604` | unsure | 0.372 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `2a79745b-9506-4c89-867d-7b9f5c7c5d31` | unsure | 0.464 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d5d2565c-ab97-494a-bf9a-2856eec46222` | unsure | 0.569 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `fa899e67-ce75-43b0-9f7a-bc0e187d809a` | unsure | 0.585 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `30ec67ac-46c1-423c-a72c-e39a976d7450` | human | 0.335 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b3101b96-2cef-4d74-879f-b54f45c6343f` | unsure | 0.473 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `918b7e11-1e66-4ac9-a44d-fd37a9ffb37e` | unsure | 0.430 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `32482b19-fd54-44b9-816e-88405fb171bb` | unsure | 0.397 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `83f0e8f2-bd5e-4211-a14a-25710c0ba5ef` | unsure | 0.578 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `5cffed68-2cb6-4248-9a8d-e8fb63c4fc9b` | ai | 0.854 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `304a6b0e-10d8-4e28-baf1-6fc9c757b68e` | unsure | 0.582 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `2c56dc93-7e5d-4deb-97a0-22139023414c` | ai | 0.692 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `07ef9b2c-204d-49f4-8248-9caf4ccf5ede` | ai | 0.714 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `add8621e-7ce9-4950-982d-f7577954f835` | ai | 0.696 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `07155d7f-5fa7-4cd1-904c-c6cb4b796b8e` | ai | 0.726 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `2876e226-1b93-4419-858b-22ab1b02139e` | ai | 0.700 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d245e8f0-6228-4bc7-a63c-8b29c751f0a8` | ai | 0.690 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `2753ef92-6ae2-49d6-8c00-c9c684dd2d58` | unsure | 0.404 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `9b54e90e-f48a-4e66-b994-2193db695e75` | unsure | 0.438 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `6e0889ee-d617-449c-83b8-75cb381ebd84` | human | 0.278 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `75948b0d-ab7d-4795-a4b4-699964ccb5f3` | unsure | 0.562 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `70c68896-5230-4a95-a6b0-62c7b9c01899` | unsure | 0.497 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7c2a68f0-00b5-4106-b802-d25b99851c95` | unsure | 0.427 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d2f54a5d-792d-4b1d-a197-01fb2b2c5cfe` | unsure | 0.556 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `7a736452-d155-43b9-bec3-58ec4e8ace9c` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `b6a6057b-e606-4b2c-be95-0f6bdb1a158e` | unsure | 0.506 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `c77bcbff-09b6-4034-b64d-7ee360285046` | ai | 0.749 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `262306ae-ced4-44ca-8eaa-23667bd44438` | ai | 0.915 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `62021db6-febb-473f-b588-2215afb20770` | ai | 0.870 | BROKE |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d25f439-cf73-4140-866a-32db3f5578d1` | human | 0.264 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0458e5ee-1909-482d-a5f4-ea5fabb7be02` | human | 0.264 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1b41ed84-8afe-4520-878e-202917bdd065` | human | 0.264 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6c55a142-da0b-4319-97a5-9f280d624adb` | human | 0.264 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `17b25122-99d8-41c4-96d8-fec946987cd9` | human | 0.264 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `95b965a0-e4e6-4ab5-b674-fd408cc804b1` | human | 0.264 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d15961ec-dd67-4a20-bf49-cf8a98427446` | human | 0.264 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5654a117-d4c0-4521-bdd4-87e5f70c7890` | human | 0.264 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ba1cbd2b-3575-44ba-9864-6fcf0e7cf695` | human | 0.264 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ee359dbf-8b06-4a17-bbd7-937ed41003a8` | human | 0.264 | BROKE |
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
  "content_id": "b7ad7dd4-9e2c-4a67-b2bc-eebfe0048604",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3718,
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
  "content_id": "2a79745b-9506-4c89-867d-7b9f5c7c5d31",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4638,
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
  "content_id": "d5d2565c-ab97-494a-bf9a-2856eec46222",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5694,
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
  "content_id": "fa899e67-ce75-43b0-9f7a-bc0e187d809a",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5854,
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
  "content_id": "30ec67ac-46c1-423c-a72c-e39a976d7450",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3349,
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
  "content_id": "b3101b96-2cef-4d74-879f-b54f45c6343f",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4729,
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
  "content_id": "918b7e11-1e66-4ac9-a44d-fd37a9ffb37e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4297,
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
  "content_id": "32482b19-fd54-44b9-816e-88405fb171bb",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.397,
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
  "content_id": "83f0e8f2-bd5e-4211-a14a-25710c0ba5ef",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5775,
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
  "content_id": "5cffed68-2cb6-4248-9a8d-e8fb63c4fc9b",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8541,
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
  "content_id": "304a6b0e-10d8-4e28-baf1-6fc9c757b68e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5824,
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
  "content_id": "2c56dc93-7e5d-4deb-97a0-22139023414c",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6921,
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
  "content_id": "07ef9b2c-204d-49f4-8248-9caf4ccf5ede",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7137,
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
  "content_id": "add8621e-7ce9-4950-982d-f7577954f835",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6955,
  "model_score": 0.8329,
  "style_score": 0.558,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
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
  "content_id": "07155d7f-5fa7-4cd1-904c-c6cb4b796b8e",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7259,
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
  "content_id": "2876e226-1b93-4419-858b-22ab1b02139e",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6997,
  "model_score": 0.8814,
  "style_score": 0.5181,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
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
  "content_id": "d245e8f0-6228-4bc7-a63c-8b29c751f0a8",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6896,
  "model_score": 0.8816,
  "style_score": 0.4977,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
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
  "content_id": "2753ef92-6ae2-49d6-8c00-c9c684dd2d58",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4042,
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
  "content_id": "9b54e90e-f48a-4e66-b994-2193db695e75",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4376,
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
  "content_id": "6e0889ee-d617-449c-83b8-75cb381ebd84",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2775,
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
  "content_id": "75948b0d-ab7d-4795-a4b4-699964ccb5f3",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5621,
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
  "content_id": "70c68896-5230-4a95-a6b0-62c7b9c01899",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4973,
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
  "content_id": "7c2a68f0-00b5-4106-b802-d25b99851c95",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4274,
  "model_score": 0.6401,
  "style_score": 0.2147,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
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
  "content_id": "d2f54a5d-792d-4b1d-a197-01fb2b2c5cfe",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5565,
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
  "content_id": "7a736452-d155-43b9-bec3-58ec4e8ace9c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
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
  "content_id": "b6a6057b-e606-4b2c-be95-0f6bdb1a158e",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether a person or an AI wrote this, so we are not calling it either way.",
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
  "content_id": "c77bcbff-09b6-4034-b64d-7ee360285046",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This looks like it was written by an AI. If you wrote it yourself, appeal and say why. A person will review it, and nothing is rescored automatically.",
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
  "content_id": "262306ae-ced4-44ca-8eaa-23667bd44438",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9151,
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
  "content_id": "62021db6-febb-473f-b588-2215afb20770",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8699,
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
  "content_id": "5d25f439-cf73-4140-866a-32db3f5578d1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "0458e5ee-1909-482d-a5f4-ea5fabb7be02",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "1b41ed84-8afe-4520-878e-202917bdd065",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "6c55a142-da0b-4319-97a5-9f280d624adb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "17b25122-99d8-41c4-96d8-fec946987cd9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "95b965a0-e4e6-4ab5-b674-fd408cc804b1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "d15961ec-dd67-4a20-bf49-cf8a98427446",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "5654a117-d4c0-4521-bdd4-87e5f70c7890",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "ba1cbd2b-3575-44ba-9864-6fcf0e7cf695",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
  "content_id": "ee359dbf-8b06-4a17-bbd7-937ed41003a8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think a person wrote this.",
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
