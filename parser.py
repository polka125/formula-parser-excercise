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

    (ExprNonTerminals.EXPR, [ExprTerminals.NUMBER]),
    (ExprNonTerminals.EXPR, [ExprTerminals.VARIABLE]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.FACTOR, ExprNonTerminals.TOPOWOP_PRIMARY]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.TERM, ExprNonTerminals.TOMULOP_FACTOR]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.EXPR, ExprNonTerminals.TOADDOP_TERM]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.TOADDOP, ExprNonTerminals.TERM]),
    (ExprNonTerminals.EXPR, [ExprNonTerminals.TOFUN, ExprNonTerminals.TOOPEN_EXPR_TOCLOSE]),

    (ExprNonTerminals.TERM, [ExprTerminals.NUMBER]),
    (ExprNonTerminals.TERM, [ExprTerminals.VARIABLE]),
    (ExprNonTerminals.TERM, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
    (ExprNonTerminals.TERM, [ExprNonTerminals.FACTOR, ExprNonTerminals.TOPOWOP_PRIMARY]),
    (ExprNonTerminals.TERM, [ExprNonTerminals.TERM, ExprNonTerminals.TOMULOP_FACTOR]),
    (ExprNonTerminals.TERM, [ExprNonTerminals.TOFUN, ExprNonTerminals.TOOPEN_EXPR_TOCLOSE]),

    (ExprNonTerminals.FACTOR, [ExprTerminals.NUMBER]),
    (ExprNonTerminals.FACTOR, [ExprTerminals.VARIABLE]),
    (ExprNonTerminals.FACTOR, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
    (ExprNonTerminals.FACTOR, [ExprNonTerminals.FACTOR, ExprNonTerminals.TOPOWOP_PRIMARY]),
    (ExprNonTerminals.FACTOR, [ExprNonTerminals.TOFUN, ExprNonTerminals.TOOPEN_EXPR_TOCLOSE]),

    (ExprNonTerminals.PRIMARY, [ExprTerminals.NUMBER]),
    (ExprNonTerminals.PRIMARY, [ExprTerminals.VARIABLE]),
    (ExprNonTerminals.PRIMARY, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
    (ExprNonTerminals.PRIMARY, [ExprNonTerminals.TOFUN, ExprNonTerminals.TOOPEN_EXPR_TOCLOSE]),

    (ExprNonTerminals.TOADDOP, [ExprTerminals.ADDOP]),
    (ExprNonTerminals.TOMULOP, [ExprTerminals.MULOP]),
    (ExprNonTerminals.TOPOWOP, [ExprTerminals.POWOP]),
    (ExprNonTerminals.TOOPEN, [ExprTerminals.OPEN]),
    (ExprNonTerminals.TOCLOSE, [ExprTerminals.CLOSE]),
    (ExprNonTerminals.TOFUN, [ExprTerminals.FUN]),

    (ExprNonTerminals.TOADDOP_TERM, [ExprNonTerminals.TOADDOP, ExprNonTerminals.TERM]),
    (ExprNonTerminals.TOMULOP_FACTOR, [ExprNonTerminals.TOMULOP, ExprNonTerminals.FACTOR]),
    (ExprNonTerminals.TOPOWOP_PRIMARY, [ExprNonTerminals.TOPOWOP, ExprNonTerminals.PRIMARY]),
    (ExprNonTerminals.EXPR_TOCLOSE, [ExprNonTerminals.EXPR, ExprNonTerminals.TOCLOSE]),
    (ExprNonTerminals.TOOPEN_EXPR_TOCLOSE, [ExprNonTerminals.TOOPEN, ExprNonTerminals.EXPR_TOCLOSE]),
]

test_sequence = [ExprTerminals.NUMBER, ExprTerminals.ADDOP, ExprTerminals.NUMBER, ExprTerminals.MULOP, ExprTerminals.OPEN, ExprTerminals.FUN, ExprTerminals.OPEN, ExprTerminals.VARIABLE, ExprTerminals.CLOSE, ExprTerminals.CLOSE]

