import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/dupl_vars/dupl_vars_3-data.n3').data

def query(a, x, xl, final_ctu):
    data.find(a, Iri('http://example.org/partLabels'), Collection([x, xl]), lambda s, p, o: final_ctu(s, o[0], o[1]))
    rule_0(a, x, xl, lambda a_0, x_1, xl_2: final_ctu(a_0, x_1, xl_2))

def rule_0(a_0, x_1, xl_2, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), Collection([x_1, x_1]), lambda s, p, o: rule_0_1(s, o[1], xl_2, final_ctu) if o[0] == o[1] else False)
    rule_1(a_0, x_1, x_1, lambda q_3, k_4, l_5: rule_0_1(q_3, l_5, xl_2, final_ctu) if k_4 == l_5 else False)

def rule_0_1(a_0, x_1, xl_2, final_ctu):
    data.find(x_1, Iri('http://example.org/label'), xl_2, lambda s, p, o: final_ctu(a_0, s, o))

def rule_1(q_3, k_4, l_5, final_ctu):
    data.find(q_3, Iri('http://example.org/hasParts'), Collection([k_4, l_5]), lambda s, p, o: final_ctu(s, o[0], o[1]))
query(ANY, ANY, ANY, lambda a, x, xl: print(Triple(Var('a'), Iri('http://example.org/partLabels'), Collection([Var('x'), Var('xl')])).instantiate({'a': a, 'x': x, 'xl': xl})))