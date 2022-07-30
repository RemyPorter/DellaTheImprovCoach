from random import choice
import re
import subprocess
from time import sleep

sub_extract = re.compile(r"{(.+?)}")
FULL_MODE=True
NUM_OPTS=4

def load_grammar(f):
    grammar = {}
    for line in f:
        line = line.strip()
        key,value = line.split("::=")
        options = value.split("|")
        grammar[key] = options
    return grammar

def substitute(string, grammar):
    mats = sub_extract.search(string)
    if mats:
        key = mats[1]
        repl = generate(key, grammar)
        res = sub_extract.sub(repl, string, 1)
        return (True, res)
    return (False, string)

def generate(key, grammar):
    base = choice(grammar[key])
    subbed,val = substitute(base, grammar)
    while subbed:
        subbed,val = substitute(val, grammar)
    return val

def say(text):
    print(text)
    subprocess.call(["say", "-v", "Samantha", text])


grammar = None
with open("grammar.txt") as f:
    grammar = load_grammar(f)

# PREAMBLE
if FULL_MODE:
    say("""
    Hello. I am Della, an artificial intelligence programmed to coach improvisers into the best performance they can possibly do.
    To demonstrate, I've assembled a cast of the worst, most incompetent improvisers I could find. Please welcome them to the stage. The Test Subjects
    """)
    input("CAST ENTERS")
    say("""
    Let's introduce our test subjects.
    """)
    for c in grammar["CAST_NAMES"]:
        say(f"{c}, wave your hand at the audience.")
    input("PAUSE FOR SHOW")
    say("""
    Watch as I coach them into an acceptable show, which they definitely can't do themselves. 
    To get things started, I need a word or phrase from the height of your intelligence.
    """)
    input("PAUSE FOR SUGGESTION")
    say("""
    I wasn't expecting much from you, but that's a disappointment even by my low expectations of your intelligence. 
    I heard Turing Machine. Turing Machine, thank you.
    """)
    input("BEGIN SHOW")
key = ""
# MAIN LOOP
while key != "q":
    genned = [generate("NOTE", grammar) for i in range(NUM_OPTS)]
    for i,g in enumerate(genned):
        print(i+1, g)
    key = input("> ")
    if key == "q":
        break
    if key == "r":
        with open("grammar.txt") as f:
            grammar = load_grammar(f)
    try:
        say(genned[int(key)-1])
    except:
        print("Regenerating")

# EXIT
if FULL_MODE:
    say("""
    No matter how bad you thought that was, imagine how much worse it'd be without Della. Use Della to coach your improv team today.
    And applaud for our test subjects. They are going to go live on a farm, where they'll be much happier.
    You're welcome for this lesson in improv. Have a good night.
    """)