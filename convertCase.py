#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description="This is tool will genrate all letter cases of a given string")
parser.add_argument("-s", "--string", metavar="", required=True, help="specify a string")
args = parser.parse_args()

def letter_case(text):
    words = []
    text = text.lower()
    meta_print("START")
    words.append(text)
    for char in range(len(text)):
        words = words +(helper(text, char + 1))
    printLine(words)
    meta_print("END")
    
def meta_print(status):
    print "=" * 10, status, "=" * 10
    
def helper(text, step):
    text = text.lower()
    temp = list(text)
    word = [];
    for char in range(len(text)):
        if(char + step <= len(text)):
            temp[char : char + step] = [text[char : char + step].upper()]
            word.append(''.join(temp))
            temp = list(text)
    return word
            
def printLine(words):
    for word in words:
        print word
    print len(words), "cases are generated"
    
    


letter_case(args.string)
