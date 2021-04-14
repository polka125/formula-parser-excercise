from enum import Enum

class ExprTerminals(Enum):
    NUMBER = 'numer'
    VARIABLE = 'variable'
    FUN = 'function'
    ADDOP = '+ or -'
    MULOP = '* or /'
    OPEN = '('
    CLOSE = ')'
    POWOP = '^'

class ExprNonTerminals(Enum):
    S0 = 'init'
    EXPR = 'expr'
    TERM = 'term'
    FACTOR = 'factor'
    PRIMARY = 'primary'
    TOADDOP_TERM = 'addop term'
    TOMULOP_FACTOR = 'tomulop factor'
    TOPOWOP_PRIMARY = 'topowerop primary'
    EXPR_TOCLOSE = 'expr toclose'
    TONUMBER = 'tonumber'
    TOVARIABLE = 'tovariable'
    TOFUN = 'tofunction'
    TOADDOP = 'to + or to -'
    TOMULOP = 'to * or to /'
    TOOPEN = 'to ('
    TOCLOSE = 'to )'
    TOPOWOP = 'to ^'
    TOOPEN_EXPR_TOCLOSE = 'toopen expr toclose'

rules = [
    (ExprNonTerminals.S0, [ExprTerminals.NUMBER]),
    (ExprNonTerminals.S0, [ExprTerminals.VARIABLE]),
    (ExprNonTerminals.S0, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
    (ExprNonTerminals.S0, [ExprNonTerminals.FACTOR, ExprNonTerminals.TOPOWOP_PRIMARY]),
    (ExprNonTerminals.S0, [ExprNonTerminals.TERM, ExprNonTerminals.TOMULOP_FACTOR]),
    (ExprNonTerminals.S0, [ExprNonTerminals.EXPR, ExprNonTerminals.TOADDOP_TERM]),
    (ExprNonTerminals.S0, [ExprNonTerminals.TOADDOP, ExprNonTerminals.TERM]),
    (ExprNonTerminals.S0, [ExprNonTerminals.TOFUN, ExprNonTerminals.TOOPEN_EXPR_TOCLOSE]),

    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
    (ExprNonTerminals., []),
]

