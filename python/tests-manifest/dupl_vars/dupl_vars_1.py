import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/dupl_vars/dupl_vars_1-data.n3').data

def query(a, b, final_ctu):
    data.find(a, Iri('http://example.org/part'), b, lambda s, p, o: final_ctu(s, o))
    if a == b:
        rule_0(b, lambda a_0: final_ctu(a_0, a_0))

def rule_0(a_0, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), Collection([Var('x_1'), Var('y_2')]), lambda s, p, o: rule_0_1(s, o[0], o[1], final_ctu))
    rule_1(a_0, Collection([Var('x_1'), Var('y_2')]), lambda q_5, a_6: rule_0_1(q_5, a_6[0], a_6[1], final_ctu))

def rule_0_1(a_0, x_1, y_2, final_ctu):
    data.find(x_1, Iri('http://example.org/label'), ANY, lambda s, p, o: rule_0_2(a_0, s, y_2, o, final_ctu))

def rule_0_2(a_0, x_1, y_2, xl_3, final_ctu):
    data.find(y_2, Iri('http://example.org/label'), ANY, lambda s, p, o: final_ctu(a_0))

def rule_1(q_5, a_6, final_ctu):
    data.find(q_5, Iri('http://example.org/hasParts'), a_6, lambda s, p, o: final_ctu(s, o))
query(ANY, ANY, lambda a, b: print(Triple(Var('a'), Iri('http://example.org/part'), Var('b')).instantiate({'a': a, 'b': b})))