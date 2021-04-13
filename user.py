# from lexer import Lexer
#
# s = '''  (1 + 2  -) /4
# +5 -
# 10'''
# print(Lexer.preparator(s))
# prints '(1+2-)/4+5-10'

from tokens import Token
from lexer import Lexer
import re

s1 = '1+2+3+()sin'

print (Lexer.tokenize(s1, Token))
#
# for tkn in Token:
#     print(str(tkn.value))

# print(re.findall(r'^1', '1'))