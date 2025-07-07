import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/misc/french.n3').data

def query(x_0, final_ctu):
    data.find(x_0, NS.rdf['type'], Iri('http://example.org/French'), lambda s, p, o: final_ctu(s))
    rule_0(x_0, lambda p_1: final_ctu(p_1))

def rule_0(p_1, final_ctu):
    data.find(p_1, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_1(s, final_ctu))

def rule_0_1(p_1, final_ctu):
    data.find(p_1, Iri('http://example.org/loves'), p_1, lambda s, p, o: final_ctu(o) if s == o else False)
    if p_1 == p_1:
        rule_1(p_1, lambda p_2: final_ctu(p_2) if p_2 == p_2 else False)

def rule_1(p_2, final_ctu):
    final_ctu(p_2)
query(ANY, lambda x_0: print(Triple(Var('x_0'), NS.rdf['type'], Iri('http://example.org/French')).instantiate({'x_0': x_0})))