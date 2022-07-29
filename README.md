# Della, the "AI" improv coach

This is not an AI. This is a grammar-based generator, essentially an overglorified madlibs that spits out bad improv coaching.

It is designed to run on MacOS (it depends on the `say` command line utility), in Python. It's been tested in 3.11, but should work on pretty much any version of Python 3. It has no external dependencies.

## Running
`python coach.py` launches the application. Hit enter as prompted. Once it gets through the preamble bits, it will start giving you options- hit 1-4 to pick the phrase you want Della to say. 

## Customizing
Read through the code in `coach.py`. There are sections labeled PREAMBLE, MAIN LOOP, and EXIT. Anything within a `say()` call is what Della will say. Feel free to modify the PREAMBLE and EXIT. To alter the main loop, you need to…

### Customize the Grammar
`grammar.txt` contains a simple BNF-like grammar. The syntax is stupid, and the program does basically no validation, so if you fuck this up, it will stop working. It's easy to do, however, so let's review the basic syntax.

Each line of the grammar defines a rule. The structure of a line is:

```
RULE_NAME::=option|option|option
```

Each line starts with a `RULE_NAME`, which is how you want to reference this rule in the future. `RULE_NAME` is followed by `::=` which is just a separator. Then, we have a list of `option`s, separated by `|` characters. An option is any arbitrary text you want. An option may contain a reference to a rule, wrapped in `{}`.

So, a very simple grammar might be:

```
CAST::=Joebob|Sallybob|Suebob
INSULT::={CAST}, you suck|You're really bad at this, {CAST}
NOTE::={INSULT}|Can we do something else?
```

`NOTE` is the terminal rule in our grammar. When Della chooses phrases, she's going to choose `NOTE`s. The simple grammar above is capable of generating the following phrases:

```
Joebob, you suck
Sallybob, you suck
Suebob, you suck
You're really bad at this, Joebob
You're really bad at this, Sallybob
You're really bad at this, Suebob
Can we do something else?
```

# Final Notes
Look, this is software I wrote for myself to do a dumb bit. Feel free to use it, but you're on your own.