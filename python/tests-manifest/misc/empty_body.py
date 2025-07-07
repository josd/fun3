import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/misc/french.n3').data

def query(x_0, final_ctu):
    data.find(x_0, NS.rdf['type'], Iri('http://example.org/French'), lambda s, p, o: final_ctu(s))
    if x_0 == Collection([Var('p_1'), Var('p2_2')]):
        rule_0(x_0[0], x_0[1], lambda p_1, p2_2: final_ctu(Collection([p_1, p2_2])))

def rule_0(p_1, p2_2, final_ctu):
    data.find(p_1, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_1(s, p2_2, final_ctu))

def rule_0_1(p_1, p2_2, final_ctu):
    data.find(p2_2, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_2(p_1, s, final_ctu))

def rule_0_2(p_1, p2_2, final_ctu):
    data.find(p_1, Iri('http://example.org/loves'), p2_2, lambda s, p, o: final_ctu(s, o))
    if p_1 == p2_2:
        rule_1(p2_2, lambda p_3: final_ctu(p_3, p_3))

def rule_1(p_3, final_ctu):
    final_ctu(p_3)
query(ANY, lambda x_0: print(Triple(Var('x_0'), NS.rdf['type'], Iri('http://example.org/French')).instantiate({'x_0': x_0})))