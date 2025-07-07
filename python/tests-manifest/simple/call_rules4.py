import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/simple/person_ca.ttl').data

def query(x_0, t_1, final_ctu):
    data.find(x_0, Iri('http://example.org/label'), t_1, lambda s, p, o: final_ctu(s, o))
    rule_0(x_0, t_1, lambda p_2, t_3: final_ctu(p_2, t_3))

def rule_0(p_2, t_3, final_ctu):
    data.find(p_2, NS.rdf['type'], t_3, lambda s, p, o: rule_0_1(s, o, final_ctu))
    if t_3 == Iri('http://example.org/Person'):
        rule_1(p_2, lambda pe_5: rule_0_1(pe_5, Iri('http://example.org/Person'), final_ctu))

def rule_0_1(p_2, t_3, final_ctu):
    data.find(p_2, Iri('http://example.org/address'), ANY, lambda s, p, o: rule_0_2(s, t_3, o, final_ctu))

def rule_0_2(p_2, t_3, a_4, final_ctu):
    data.find(a_4, Iri('http://example.org/country'), Literal('CA', NS.xsd['string']), lambda s, p, o: final_ctu(p_2, t_3))

def rule_1(pe_5, final_ctu):
    data.find(pe_5, Iri('http://example.org/ability'), Iri('http://example.org/drink'), lambda s, p, o: final_ctu(s))
query(ANY, ANY, lambda x_0, t_1: print(Triple(Var('x_0'), Iri('http://example.org/label'), Var('t_1')).instantiate({'x_0': x_0, 't_1': t_1})))