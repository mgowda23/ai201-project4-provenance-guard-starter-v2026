"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "The thing is my order has been picked up and i also have the proof which i have attached with this mail - soo plz check and replace my order soon. Thank you.",
            "Usually for a 2-pointer approach we need the my understanding is that we array to be sorted right? but here we dont apply that concept , if we can decide which pointer to move without the array being sorted it can still act like a 2-pointer problem.",
            "TODAY - Solved 2 Neetcode easy questions and hopefully will remember atleast the logics applied to one SDE role.",
            "TOMORROW - Focus on checking on more SDE roles and working on upskilling that, - start with DA or DS related coursework or portfolio project from youtube. Oh! also solve more Neetcode problems hehe",
            "5-Jan: Tried the first plan but came to conclusion that its not so easy to target them when what I need the most is consistency, i wont be giving up easily on that and will keep an optimistic mindset and tackle through this.",
            "Apart from that when we are extending thread class, we usually extends class to increase capabilities / behaviour, but thread helps decides where/who the code has to run so separating this makes sense.",
            "Metaclass is the class of a class, it controls how class are created by default. Python use \"type\" as the metaclass but we can create our own metaclass to customize or validate the class creation.",
            "A race condition occurs when multiple threads or processes access and modify a shared data at the same time and the final result depends on which one executes first.",
            "I want to send a thank you for connecting message to this person and also wanted to let him know I connected with him since we both worked as software engineers at ITC INFOTECH until june 2024 and right now Im trying to transition into AI software field in the US after i completed my masters, so wanted your help with framing my resume points properly structured and would be helpful if you could share your updated resume for reference.",
            "I want to join the kaggle Competition Launch: NFL Big Data Bowl 2027 hackathon, but I have never done anything like this before, what kind of dedication and knowledge do I need If i would be working on this? I would require your guidance and help in doing this. If you had to prepare a plan with step by step procedure or process to complete this how would you do it.",
        ],
    },
    {
        "name": "score spread between clear cases",
        "criterion": 2,
        "texts": [
            "The importance of effective time management cannot be overstated in today's fast-paced work environment. Professionals who develop strong organizational habits are better positioned to meet deadlines and reduce stress. There are several key strategies that can help individuals improve their productivity. First, prioritization is essential. By identifying the most important tasks and addressing them first, workers can ensure that critical objectives are met. Second, minimizing distractions plays a significant role. Setting aside dedicated blocks of time for concentrated work is widely considered beneficial. Finally, regular breaks are important for maintaining performance.",
            "I didn't sleep. Not properly, anyway — I lay there listening to the boiler tick and thinking about the thing I'd said to Marcus at the pub, which was stupid, and which he will absolutely bring up again. Twice now. So: coffee, and the long way round to work, and a plan. The plan lasted until about ten past nine, when Priya asked how the weekend was and I said \"fine\" in the voice that means it wasn't, and she put her mug down and looked at me. That's the trouble with Priya. She notices.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "The scenarios below are drafts built around your metrics. I don’t know your real context, so anything in [brackets] is a placeholder, and the situations are plausible framings. Replace them with what actually happened. Interviewers probe deeply, and a story that isn’t true falls apart on the second follow-up. Also make sure the tech stack and employer on each story match your actual resume.",
            "Nope. Priya — mug down, that look — caught me before I'd even sat. I told Marcus the boiler's tick was driving me spare, and that I'd rather walk past the shut bakery, twice, than sit through another standup where nobody says the thing they actually mean.",
            "Time management matters more than people admit, especially now that work moves as fast as it does. If you're organised you hit deadlines, and you're less frazzled doing it. A few things actually help. Prioritise — work out what genuinely matters and do that first. Cut the interruptions; notifications wreck focus and the damage is worse than it feels at the time. And take breaks, short ones, often.",
        ],
    },
    {
        "name": "appeal submission",
        "criterion": 4,
        "texts": [
            "I wrote this sentence myself and want to verify that the appeal process records my explanation.",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 5,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {
                "creator_id": "eval_missing_text",
            },
            {
                "text": "",
                "creator_id": "eval_empty_text",
            },
            {
                "text": "x" * 4001,
                "creator_id": "eval_huge_text",
            },
        ],
    },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
