import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/bnodes/person_ca_eur.n3').data

def query(x, final_ctu):
    data.find(x, NS.rdf['type'], Iri('http://example.org/Canadian'), lambda s, p, o: final_ctu(s))
    rule_0(x, lambda p_0: final_ctu(p_0))

def rule_0(p_0, final_ctu):
    data.find(p_0, NS.rdf['type'], Iri('http://example.org/Person'), lambda s, p, o: rule_0_1(s, final_ctu))
    rule_1(p_0, lambda p_1: rule_0_1(p_1, final_ctu))

def rule_0_1(p_0, final_ctu):
    data.find(p_0, Iri('http://example.org/address'), ANY, lambda s, p, o: rule_0_2(s, o, final_ctu))

def rule_0_2(p_0, a_bn, final_ctu):
    data.find(a_bn, Iri('http://example.org/country'), Literal('CA', NS.xsd['string']), lambda s, p, o: final_ctu(p_0))

def rule_1(p_1, final_ctu):
    data.find(p_1, Iri('http://example.org/ability'), Iri('http://example.org/think'), lambda s, p, o: final_ctu(s))
query(ANY, lambda x: print(Triple(Var('x'), NS.rdf['type'], Iri('http://example.org/Canadian')).instantiate({'x': x})))