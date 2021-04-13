class Grammar:
    def __init__(self, terminals, nonterminals, initial, rules):
        """
        :param terminals: token valued iterable of terminals (i.e. must be iterable, elements must have value() method )
        :param nonterminals: iterable with terminal objects
        :param initial element of nonterminals (i.e. must holds initial in nonterminals)
        :param rules: list of pairs (nonterminal, list of nonterminals and terminals )
        example of rule: [(S, [S, S]),
                          (S, ['(', S, ')'])
                          (S, )]
        """
        self.termimals = terminals
        self.nonterminals = nonterminals
        self.initial = initial
        self.rules = rules

