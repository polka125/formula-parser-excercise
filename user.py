from tokens import Token
from lexer import Lexer
import re


def testLexer():
    s1 = 'sIn(x + 10.2*y)'

    print (Lexer.tokenize(s1, Token))


if __name__ == '__main__':

    test_function_list = [testLexer]

    for test in test_function_list:
        test.__call__()
    