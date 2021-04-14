from tokens import Token
from lexer import Lexer
import re
from grammar import Grammar


def testLexer():
    s1 = 'sIn(x + 10.2*y)'
    print (Lexer.tokenize(s1, Token))

def testGrammar():
    gr = Grammar(['(', ')'], ['S', 'S1', 'BL', 'BR'], 'S', [('S', ['S', 'S']), ('S', ['BL', 'S1']), ('S1', ['S', 'BR']), ('BL', ['(']), ('BR', [')']), ('S', ['BL', 'BR'])])
    s1 = '()'
    s2 = ')('
    s3 = '(((()))()())'
    s4 = '((()())((())'
    s5 = '('
    slist = [s1, s2, s3, s4, s5]
    for s in slist:
        print(gr.parse(s)[0])

def test_parser():
    from parser import ExprNonTerminals, ExprTerminals, rules, test_sequence
    gr = Grammar(ExprTerminals, ExprNonTerminals, ExprNonTerminals.S0, rules)
    print(gr.parse(test_sequence)[0])
    print(gr.parse(test_sequence[:-1])[0])

if __name__ == '__main__':

    test_function_list = [test_parser]

    for test in test_function_list:
        test.__call__()
    