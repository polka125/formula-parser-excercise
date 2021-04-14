from copy import copy, deepcopy

class Empty:
    pass

class Grammar:
    def __init__(self, terminals, nonterminals, initial, rules, eps = Empty):
        """
        :param terminals: token valued iterable of terminals (i.e. must be iterable, elements must have value() method )
        :param nonterminals: iterable with terminal objects
        :param initial element of nonterminals (i.e. must holds initial in nonterminals)
        :param rules: list of pairs (nonterminal, list of nonterminals and terminals )
        example of rule: [(S, [S, S]),
                          (S, ['(', S, ')'])
                          (S, )]
        :param eps: empty token, Empty by default. If not default must be in terminals
        """
        self.termimals = copy(terminals)
        self.nonterminals = copy(nonterminals)
        self.initial = initial
        self.rules = deepcopy(rules)
        self.eps = eps


    def isChomsky(self):
        return True
    def toChomsky(self):
        pass

    def parse(self, token_list):
        """realisation CYK algorithm"""
        def find_in_nonterm(tkn):
            for i, t in enumerate(self.nonterminals):
                if t == tkn:
                    return i + 1
        def find_in_term(tkn):
            for i, t in enumerate(self.termimals):
                if t == tkn:
                    return i + 1

        if not self.isChomsky():
            self.toChomsky()
        dp = [[[{"possib":False, "parent": None, "lchild": None, "rchild": None, "lrule": 0, "rrule": 0, "type": None, "value": None}
                for k in range(len(self.nonterminals) + 1)]
               for j in range(len(token_list) + 1)]
              for i in range(len(token_list) + 1)]
        for s in range(1, len(token_list) + 1):
            for rule in range(1, len(self.rules) + 1):
                if len(self.rules[rule - 1][1]) == 1:
                    v = find_in_nonterm(self.rules[rule - 1][0])
                    dp[1][s][v]["possib"] = True
                    dp[1][s][v]["type"] = "term"
                    dp[1][s][v]["value"] = self.rules[rule - 1][1][0]
        for le in range(2, len(token_list) + 1):
            for s in range(1, len(token_list) - le + 2):
                for p in range(1, le):
                    for rule in range(1, len(self.rules) + 1):
                        if len(self.rules[rule - 1][1]) == 2:
                            a = find_in_nonterm(self.rules[rule - 1][0])
                            b = find_in_nonterm(self.rules[rule - 1][1][0])
                            c = find_in_nonterm(self.rules[rule - 1][1][1])

                            if dp[p][s][b]["possib"] and dp[le - p][s + p][c]["possib"]:
                                dp[le][s][a]["possib"] = True
                                dp[le][s][a]["type"] = "nonterm"
                                dp[le][s][a]["lchild"] = (p, s)
                                dp[le][s][a]["lrule"] = b
                                dp[le][s][a]["rchild"] = (le - p, s + p)
                                dp[le][s][a]["rrule"] = c
                                dp[le][s][a]["value"] = rule

        return dp[len(token_list)][1][1]["possib"], dp



