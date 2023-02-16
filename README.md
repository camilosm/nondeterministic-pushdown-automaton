# Non deterministic pushdown automaton

This program receives a non deterministic pushdown automaton especified in a JSON file and a word, and checks if the word is recognized by the automaton.

## Format of the automaton file

{ "pda": [
 [states],
 [input alphabet],
 [stack alphabet],
 [transitions],
 [initial states],
 [final states]
]}

where each element in [transitions] is:

[origin state, input symbol read, symbol to remove from stack, target state, symbol to insert in stack]

## Example of an automaton that recognizes [palindromes](palindrome.js "palindrome.js")

```javascript
{"pda":[
    ["A", "B"],
    ["0", "1"],
    ["X", "Y"],
    [
        ["A", "0", "#", "A", "X"],
        ["A", "1", "#", "A", "Y"],
        ["A", "#", "#", "B", "#"],
        ["A", "0", "#", "B", "#"],
        ["A", "1", "#", "B", "#"],
        ["B", "0", "X", "B", "#"],
        ["B", "1", "Y", "B", "#"]
    ],
    ["A"],
    ["B"]
    ]}
```
## Usage

```shell
$ python pda.py palindrome.js 0110
Yes
$ python pda.py palindrome.js 1110
No
```

## Motivation

This program was written for an assignment of my bachelor's degree in Computer Engineering at CEFET-MG.

## Thanks

@thiagorss: best duo :beers:
@rimsa: professor and inspiration :man_teacher: