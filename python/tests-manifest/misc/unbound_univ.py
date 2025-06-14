import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/misc/unbound_univ-data.n3').data

def query(x, t, final_ctu):
    data.find(x, Iri('http://example.org/label'), Collection([t]), lambda s, p, o: final_ctu(s, o[0]))
    rule_0(x, t, lambda p_0, t_1: final_ctu(p_0, t_1))

def rule_0(p_0, t_1, final_ctu):
    data.find(p_0, NS.rdf['type'], t_1, lambda s, p, o: final_ctu(s, o))
    rule_1(p_0, t_1, lambda p_2, t_3: final_ctu(p_2, t_3))

def rule_1(p_2, t_3, final_ctu):
    data.find(p_2, Iri('http://example.org/name'), Literal('Socrates', NS.xsd['string']), lambda s, p, o: final_ctu(s, t_3))
query(ANY, ANY, lambda x, t: print(Triple(Var('x'), Iri('http://example.org/label'), Collection([Var('t')])).instantiate({'x': x, 't': t})))