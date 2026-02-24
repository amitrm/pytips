import random
import streamlit as st

st.set_page_config(page_title="Tips for Today", page_icon="🐍")

st.title("Tips for Today 🐍")
st.write("Funny advice that accidentally teaches you Python.")

TIPS = [
    {
        "title": "F-strings: stop concatenating like it is 2009",
        "advice": "If your string formatting looks like a ransom note, use f-strings.",
        "snippet": """name = "Billu"
bugs = 3
msg = f"Hello, {name}. You have {bugs} bugs. Good luck."
print(msg)""",
    },
    {
        "title": "Enumerate: give your loops a name tag",
        "advice": "Counting manually is how off-by-one errors reproduce.",
        "snippet": """items = ["alpha", "beta", "gamma"]
for i, item in enumerate(items, start=1):
    print(i, item)""",
    },
    {
        "title": "Zip: pair things without awkward indexing",
        "advice": "If you are looping over range(len(...)), a zip is quietly judging you.",
        "snippet": """names = ["Ada", "Linus", "Grace"]
scores = [99, 87, 95]
for name, score in zip(names, scores):
    print(name, score)""",
    },
    {
        "title": "Unpacking: let Python carry the groceries",
        "advice": "Stop walking back to the car for each variable.",
        "snippet": """point = (10, 20)
x, y = point
print(x, y)""",
    },
    {
        "title": "Slicing: take a bite, not the whole sandwich",
        "advice": "You do not need a loop to grab the last 3 items. You need boundaries.",
        "snippet": """nums = [1, 2, 3, 4, 5, 6]
last_three = nums[-3:]
every_other = nums[::2]
print(last_three, every_other)""",
    },
    {
        "title": "Dict.get: avoid KeyError drama",
        "advice": "Arguing with missing keys is a hobby. Use .get().",
        "snippet": """config = {"timeout": 30}
timeout = config.get("timeout", 10)
retries = config.get("retries", 3)
print(timeout, retries)""",
    },
    {
        "title": "Defaultdict: stop writing if-key-not-exists rituals",
        "advice": "If you are summoning keys into existence, use defaultdict like an adult wizard.",
        "snippet": """from collections import defaultdict

counts = defaultdict(int)
words = ["spam", "ham", "spam"]
for w in words:
    counts[w] += 1
print(dict(counts))""",
    },
    {
        "title": "Counter: counting is not a personality trait",
        "advice": "If you wrote a counting loop, Counter already did it and did not brag.",
        "snippet": """from collections import Counter

words = ["spam", "ham", "spam"]
c = Counter(words)
print(c["spam"])
print(c.most_common(1))""",
    },
    {
        "title": "List comprehensions: one-liners with benefits",
        "advice": "If your loop is just appending, compress the sadness into a comprehension.",
        "snippet": """nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums if n % 2 == 1]
print(squares)""",
    },
    {
        "title": "Generator expressions: same idea, less RAM",
        "advice": "Your laptop fan is not a feature. Stream values with generators.",
        "snippet": """nums = range(1_000_000)
total = sum(n * n for n in nums if n % 2 == 0)
print(total)""",
    },
    {
        "title": "Any/All: stop writing boolean novels",
        "advice": "If your condition reads like a contract, use any()/all().",
        "snippet": """values = [0, "", None, 5]
print(any(values))
print(all(values))""",
    },
    {
        "title": "Sorted with key: let the key do the thinking",
        "advice": "Do not sort by vibes. Sort by key functions.",
        "snippet": """items = ["aaa", "b", "cc"]
by_length = sorted(items, key=len)
print(by_length)""",
    },
    {
        "title": "Dataclasses: less boilerplate, more sanity",
        "advice": "If your class is 90% __init__, you are building furniture without screws.",
        "snippet": """from dataclasses import dataclass

@dataclass
class User:
    name: str
    active: bool = True

u = User("Billu")
print(u)""",
    },
    {
        "title": "Context managers: open files like you mean it",
        "advice": "If you forget to close files, your OS will remember. Forever.",
        "snippet": """path = "example.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("Hello from a responsible adult.")""",
    },
    {
        "title": "Pathlib: stop handcrafting file paths",
        "advice": "Building paths with string + '/' is how bugs migrate cross-platform.",
        "snippet": """from pathlib import Path

p = Path("data") / "input.csv"
print(p)
print(p.suffix)""",
    },
    {
        "title": "Logging: print() is not observability",
        "advice": "Print statements are like sticky notes in a hurricane. Use logging.",
        "snippet": """import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting job")
logging.warning("This might be spicy")""",
    },
    {
        "title": "Try/Except: catch exceptions, not feelings",
        "advice": "Assuming inputs behave is optimism. Handle failure like a professional pessimist.",
        "snippet": """def safe_int(x: str) -> int | None:
    try:
        return int(x)
    except ValueError:
        return None

print(safe_int("42"))
print(safe_int("nope"))""",
    },
    {
        "title": "Type hints: future you deserves subtitles",
        "advice": "If your function signature is a mystery, you are writing thriller code.",
        "snippet": """def greet(name: str, times: int = 1) -> str:
    return " ".join([f"Hi, {name}!" for _ in range(times)])

print(greet("Billu", 2))""",
    },
    {
        "title": "Walrus operator: assign and judge at the same time",
        "advice": "Sometimes you want a value and a decision. Python said: fine.",
        "snippet": """data = "hello"
if (n := len(data)) > 3:
    print(f"Length is {n}")""",
    },
    {
        "title": "Join: concatenation in loops is a slow hobby",
        "advice": "If you build strings with += in a loop, your CPU starts writing resignation drafts.",
        "snippet": """parts = ["ship", "it", "now"]
sentence = " ".join(parts)
print(sentence)""",
    },
    {
        "title": "Set operations: dedupe like you mean it",
        "advice": "Duplicates are like gremlins. Sets are the bright light.",
        "snippet": """a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)""",
    },
    {
        "title": "Ternary expression: small decisions, fewer lines",
        "advice": "One-line ifs are fine. Two-page ifs are not.",
        "snippet": """temp = 21
label = "warm" if temp >= 20 else "cold"
print(label)""",
    },
    {
        "title": "Named tuples: readable lightweight records",
        "advice": "If you keep forgetting what index 1 means, name it.",
        "snippet": """from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)""",
    },
    {
        "title": "Map/Filter: use responsibly (or not at all)",
        "advice": "map/filter are fine, but comprehensions are usually clearer. Choose clarity over cleverness.",
        "snippet": """nums = [1, 2, 3, 4]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubled = list(map(lambda n: n * 2, evens))
print(doubled)""",
    },
    {
        "title": "timeit: measure, do not guess",
        "advice": "Performance opinions without measurements are just astrology for engineers.",
        "snippet": """import timeit

t = timeit.timeit(stmt="sum(range(1000))", number=10_000)
print(t)""",
    },
]

st.caption("Pick a tip at random. Laugh a little. Learn a lot.")

if "tip_idx" not in st.session_state:
    st.session_state.tip_idx = random.randrange(len(TIPS))

if st.button("Give me a tip"):
    st.session_state.tip_idx = random.randrange(len(TIPS))

tip = TIPS[st.session_state.tip_idx]

st.subheader(tip["title"])
st.success(tip["advice"])
st.code(tip["snippet"], language="python")

st.divider()
st.caption("⚠️ Disclaimer: Tips are funny. The Python is real.")
st.caption("🧩 Put together by [amitrm](https://github.com/amitrm). ⚙️ Built with [Streamlit](https://streamlit.io).")
