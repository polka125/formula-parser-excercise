import re


class Lexer:
    @staticmethod
    def preparator(s: str):
        """prepare string to lexing"""
        pattern = re.compile('\s+')
        return re.sub(pattern, '', s)

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




    def __init__(self, string: str, token_enum):
        """
        :param string: string to parse
        :param token_enum: any instance of Enum class with string valued items
        """
        self.__row_string = string
        self.__token_emun - token_enum