import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/misc/french.n3').data

def query(x, final_ctu):
    data.find(x, NS.rdf['type'], Iri('http://example.org/French'), lambda s, p, o: final_ctu(s))
    if x == Collection([Var('p_0'), Var('p2_1')]):
        rule_0(x[0], x[1], lambda p_0, p2_1: final_ctu(Collection([p_0, p2_1])))

def rule_0(p_0, p2_1, final_ctu):
    data.find(p_0, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_1(s, p2_1, final_ctu))

def rule_0_1(p_0, p2_1, final_ctu):
    data.find(p2_1, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_2(p_0, s, final_ctu))

def rule_0_2(p_0, p2_1, final_ctu):
    data.find(p_0, Iri('http://example.org/loves'), p2_1, lambda s, p, o: final_ctu(s, o))
    if p_0 == p2_1:
        rule_1(p2_1, lambda p_2: final_ctu(p_2, p_2))

def rule_1(p_2, final_ctu):
    final_ctu(p_2)
query(ANY, lambda x: print(Triple(Var('x'), NS.rdf['type'], Iri('http://example.org/French')).instantiate({'x': x})))