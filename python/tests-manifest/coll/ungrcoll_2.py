import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/coll/ungrcoll_2-data.n3').data

def query(a, xl, yl, final_ctu):
    data.find(a, Iri('http://example.org/partLabels'), Collection([xl, yl]), lambda s, p, o: final_ctu(s, o[0], o[1]))
    rule_0(a, xl, yl, lambda a_0, xl_1, yl_2: final_ctu(a_0, xl_1, yl_2))

def rule_0(a_0, xl_1, yl_2, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), Collection([Var('x_3'), Var('y_4')]), lambda s, p, o: rule_0_1(s, xl_1, yl_2, o[0], o[1], final_ctu))
    rule_1(a_0, ANY, ANY, lambda q_5, a_6, b_7: rule_0_1(q_5, xl_1, yl_2, a_6, b_7, final_ctu))

def rule_0_1(a_0, xl_1, yl_2, x_3, y_4, final_ctu):
    data.find(x_3, Iri('http://example.org/label'), xl_1, lambda s, p, o: rule_0_2(a_0, o, yl_2, s, y_4, final_ctu))

def rule_0_2(a_0, xl_1, yl_2, x_3, y_4, final_ctu):
    data.find(y_4, Iri('http://example.org/label'), yl_2, lambda s, p, o: final_ctu(a_0, xl_1, o))

def rule_1(q_5, a_6, b_7, final_ctu):
    data.find(q_5, Iri('http://example.org/part'), a_6, lambda s, p, o: rule_1_1(s, o, b_7, final_ctu))

def rule_1_1(q_5, a_6, b_7, final_ctu):
    data.find(q_5, Iri('http://example.org/part'), b_7, lambda s, p, o: final_ctu(s, a_6, o))
query(ANY, ANY, ANY, lambda a, xl, yl: print(Triple(Var('a'), Iri('http://example.org/partLabels'), Collection([Var('xl'), Var('yl')])).instantiate({'a': a, 'xl': xl, 'yl': yl})))