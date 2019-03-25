class GejalaRule:
    def __init__(self, gejala, vorder, vur):
        self.gejala = gejala
        self.vorder = vorder
        self.vur = vur

class VUCR:
    def __init__(self, rule, gejalas, nurj, total_vur, nur, vur_norm):
        self.rule = rule
        self.gejalas = gejalas
        pass

def rule_to_vucr(rule, non_counter):
    '''
    Mapping the given rule to vucr object
    :param rule: Rule object
    :param non_counter: Number of node counter
    :return: Vucr object
    '''
    pass

def vucr(rules):

    non_counter = {}
    vucr = []

    for index, rule in enumerate(rules):
        rule_list_gejala = rule.list_gejala
        n_rule_gejala = len(rule_list_gejala)
        pass