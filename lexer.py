import re


class Lexer:

    @staticmethod
    def preparator(s: str):
        """prepare string to lexing"""
        pattern = re.compile('\s+')
        return re.sub(pattern, '', s).lower()

    @staticmethod
    def greed_tokenizer(s: str, token_enum):
        """get string and token list, returns list of pairs (tocken instanceof tocken_enum, substring)
        """
        answer = []
        s1 = s
        while s1 != '':

            for tkn in token_enum:
                pattern = r'^' + str(tkn.value)
                subtokens = re.findall(pattern, s1)
                if len(subtokens) > 0:
                    match = subtokens[0]
                    answer.append((tkn, match))
                    s1 = s1[len(match):]

                    break
            else:
                # case no token found
                raise Exception("incomplete token enum, couldn't parse")
        return answer

    @staticmethod
    def tokenize(s: str, token_enum):
        s = Lexer.preparator(s)
        return Lexer.greed_tokenizer(s, token_enum)

    def __init__(self):
        pass
