import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/dupl_vars/dupl_vars_2-data.n3').data

def query(a, x, y, xl, final_ctu):
    data.find(a, Iri('http://example.org/partLabels'), Collection([x, y, xl]), lambda s, p, o: final_ctu(s, o[0], o[1], o[2]))
    rule_0(a, x, y, xl, lambda a_0, x_1, y_2, xl_3: final_ctu(a_0, x_1, y_2, xl_3))

def rule_0(a_0, x_1, y_2, xl_3, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), Collection([x_1, y_2]), lambda s, p, o: rule_0_1(s, o[0], o[1], xl_3, final_ctu))
    if x_1 == y_2:
        rule_1(a_0, y_2, lambda q_4, x_5: rule_0_1(q_4, x_5, x_5, xl_3, final_ctu))

def rule_0_1(a_0, x_1, y_2, xl_3, final_ctu):
    data.find(x_1, Iri('http://example.org/label'), xl_3, lambda s, p, o: final_ctu(a_0, s, y_2, o))

def rule_1(q_4, x_5, final_ctu):
    data.find(q_4, Iri('http://example.org/hasParts'), Collection([x_5, x_5]), lambda s, p, o: final_ctu(s, o[1]) if o[0] == o[1] else False)
query(ANY, ANY, ANY, ANY, lambda a, x, y, xl: print(Triple(Var('a'), Iri('http://example.org/partLabels'), Collection([Var('x'), Var('y'), Var('xl')])).instantiate({'a': a, 'x': x, 'y': y, 'xl': xl})))