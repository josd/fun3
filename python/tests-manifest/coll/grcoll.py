import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/coll/grcoll-data.n3').data

def query(a, xl, yl, final_ctu):
    data.find(a, Iri('http://example.org/partLabels'), Collection([xl, yl]), lambda s, p, o: final_ctu(s, o[0], o[1]))
    rule_0(a, xl, yl, lambda a_0, xl_1, yl_2: final_ctu(a_0, xl_1, yl_2))

def rule_0(a_0, xl_1, yl_2, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), Collection([Iri('http://example.org/man'), Iri('http://example.org/machine')]), lambda s, p, o: rule_0_1(s, xl_1, yl_2, final_ctu))
    rule_1(a_0, lambda q_3: rule_0_1(q_3, xl_1, yl_2, final_ctu))

def rule_0_1(a_0, xl_1, yl_2, final_ctu):
    data.find(Iri('http://example.org/man'), Iri('http://example.org/label'), xl_1, lambda s, p, o: rule_0_2(a_0, o, yl_2, final_ctu))

def rule_0_2(a_0, xl_1, yl_2, final_ctu):
    data.find(Iri('http://example.org/machine'), Iri('http://example.org/label'), yl_2, lambda s, p, o: final_ctu(a_0, xl_1, o))

def rule_1(q_3, final_ctu):
    data.find(q_3, Iri('http://example.org/part'), Iri('http://example.org/man'), lambda s, p, o: rule_1_1(s, final_ctu))

def rule_1_1(q_3, final_ctu):
    data.find(q_3, Iri('http://example.org/part'), Iri('http://example.org/machine'), lambda s, p, o: final_ctu(s))
query(ANY, ANY, ANY, lambda a, xl, yl: print(Triple(Var('a'), Iri('http://example.org/partLabels'), Collection([Var('xl'), Var('yl')])).instantiate({'a': a, 'xl': xl, 'yl': yl})))