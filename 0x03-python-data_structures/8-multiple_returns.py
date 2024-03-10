#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence = tuple(sentence) + (None,)
    char1 = sentence[0]
    return (len(sentence), char1)
