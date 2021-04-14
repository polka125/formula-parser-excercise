from tokens import Token
from lexer import Lexer
import re
from grammar import Grammar


def testLexer():
    s1 = 'sIn(x + 10.2*y)'

    print (Lexer.tokenize(s1, Token))

def testGrammar():
    gr = Grammar(['(', ')'], ['S', 'L', 'BL', 'BR'], 'S', [('S', ['BL', 'L']), ('S', ['BL', 'BR']), ('L', ['S', 'BR']), ('BL', ['(']), ('BR', [')'])])
    print(gr.parse(['(', '(', ')', ')', ')']))


if __name__ == '__main__':

    test_function_list = [testGrammar]

    for test in test_function_list:
        test.__call__()
    