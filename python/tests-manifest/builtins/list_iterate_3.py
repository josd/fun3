import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_iterate
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_iterate_3-data.n3').data

def query(x, final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/value'), x, lambda s, p, o: final_ctu(o))
    rule_0(x, lambda x_0: final_ctu(x_0))

def rule_0(x_0, final_ctu):
    list_iterate(Collection([Literal('c', NS.xsd['string']), Literal('b', NS.xsd['string']), Literal('c', NS.xsd['string'])]), Collection([Literal(2, NS.xsd['int']), x_0]), lambda s, o: final_ctu(o[1]))
query(ANY, lambda x: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/value'), Var('x')).instantiate({'x': x})))