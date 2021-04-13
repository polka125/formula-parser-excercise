from enum import Enum

# just simple regexps

class Token(Enum):
    LEFT_BRACKET = r'\('
    RIGHT_BRACKET = r'\)'
    NUMBER = r'\d+(?:\.\d*|)'
    PLUS = r'\+'
    MINUS = r'\-'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    SIN = r'sin'
    COS = r'cos'
    SQRT = r'sqrt'
    POWER = r'\^'
    TAN = r'(?:tg|tan)'
    LOG = r'(?:log|ln|lg)'
    SPACE = r'\s'
    VARIABLE = r'(?:[a-zA-Z_$][a-zA-Z_$0-9]*)'
    UNKNOWN = '.'






