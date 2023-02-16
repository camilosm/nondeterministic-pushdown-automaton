import json
import sys

def usage():
    print("Usage: python apn.py apn.json word")

if len(sys.argv) != 3:
    usage()
    if len(sys.argv) < 3:
        sys.exit("missing arguments")
    else:
        sys.exit("too many arguments")

try:
    with open(sys.argv[1]) as fp:
        apn = json.load(fp)["ap"]
except IOError:
    print("file "+sys.argv[1]+" not found")
    usage()
    sys.exit(1)

class Instant:
    def __init__(self, state, word, stack):
        self.state=state
        self.word=word
        self.stack=stack
    
    def __str__(self):
        return "state: "+self.state+" | word: "+self.word+" | stack: "+str(self.stack)
    
    def empty(self):
        if not self.word and not self.stack:
            return True

class Apn:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions, initial_states, final_states):
            self.states=states
            self.input_alphabet=input_alphabet
            self.stack_alphabet=stack_alphabet
            self.transitions=transitions
            self.initial_states=initial_states
            self.final_states=final_states
            self.instants=[]
    
    def initialize(self, word):
        word=word.replace('#','')
        if not all(c in self.input_alphabet for c in word):
            return False
        for state in self.initial_states:
            self.instants.append(Instant(state,word,[]))
        return True
        
    def process(self):
        while self.instants:
            next_instants=[]
            for instant in self.instants:
                if instant.empty() and instant.state in self.final_states:
                    return True
                else:
                    for transition in self.transitions:
                        if transition[0] == instant.state:
                            word = instant.word
                            if transition[1] == '#' or instant.word and transition[1] == instant.word[0]:
                                if transition[1] != '#':
                                    word = word[1:]
                                if transition[2] == '#' or instant.stack and transition[2] == instant.stack[-1]:
                                    stack = instant.stack[:]
                                    if transition[2] != '#':
                                        stack.pop()
                                    if transition[4] != '#':
                                        for char in transition[4][ : :-1]:
                                            stack.append(char)
                                    state = transition[3]
                                    next_instants.append(Instant(state, word, stack))
            self.instants=next_instants
        return False

states = apn[0]
input_alphabet = apn[1]
stack_alphabet = apn[2]
transitions = apn[3]
initial_states = apn[4]
final_states = apn[5]

apn = Apn(states, input_alphabet, stack_alphabet, transitions, initial_states, final_states)
word = sys.argv[2]

# to do: check if it's looping

if not apn.initialize(word):
    print("no")
else:
    if apn.process():
        print("yes")
    else:
        print("no")