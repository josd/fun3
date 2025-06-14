import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/simple/person_ca.ttl').data

def query(x, t, final_ctu):
    data.find(x, Iri('http://example.org/label'), t, lambda s, p, o: final_ctu(s, o))
    rule_0(x, t, lambda p_0, t_1: final_ctu(p_0, t_1))

def rule_0(p_0, t_1, final_ctu):
    data.find(p_0, NS.rdf['type'], t_1, lambda s, p, o: rule_0_1(s, o, final_ctu))
    if t_1 == Iri('http://example.org/Person'):
        rule_1(p_0, lambda pe_3: rule_0_1(pe_3, Iri('http://example.org/Person'), final_ctu))

def rule_0_1(p_0, t_1, final_ctu):
    data.find(p_0, Iri('http://example.org/address'), ANY, lambda s, p, o: rule_0_2(s, t_1, o, final_ctu))

def rule_0_2(p_0, t_1, a_2, final_ctu):
    data.find(a_2, Iri('http://example.org/country'), Literal('CA', NS.xsd['string']), lambda s, p, o: final_ctu(p_0, t_1))

def rule_1(pe_3, final_ctu):
    data.find(pe_3, Iri('http://example.org/ability'), Iri('http://example.org/drink'), lambda s, p, o: final_ctu(s))
query(ANY, ANY, lambda x, t: print(Triple(Var('x'), Iri('http://example.org/label'), Var('t')).instantiate({'x': x, 't': t})))