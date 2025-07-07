import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/misc/unbound_univ-data.n3').data

def query(x_0, t_1, final_ctu):
    data.find(x_0, Iri('http://example.org/label'), Collection([t_1]), lambda s, p, o: final_ctu(s, o[0]))
    rule_0(x_0, t_1, lambda p_2, t_3: final_ctu(p_2, t_3))

def rule_0(p_2, t_3, final_ctu):
    data.find(p_2, NS.rdf['type'], t_3, lambda s, p, o: final_ctu(s, o))
    rule_1(p_2, t_3, lambda p_4, t_5: final_ctu(p_4, t_5))

def rule_1(p_4, t_5, final_ctu):
    data.find(p_4, Iri('http://example.org/name'), Literal('Socrates', NS.xsd['string']), lambda s, p, o: final_ctu(s, t_5))
query(ANY, ANY, lambda x_0, t_1: print(Triple(Var('x_0'), Iri('http://example.org/label'), Collection([Var('t_1')])).instantiate({'x_0': x_0, 't_1': t_1})))