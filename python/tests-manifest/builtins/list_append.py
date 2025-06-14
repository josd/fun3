import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_append
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_append-data.n3').data

def query(x, final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/is'), x, lambda s, p, o: final_ctu(o))
    rule_0(x, lambda x_0: final_ctu(x_0))

def rule_0(x_0, final_ctu):
    list_append(Collection([Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int'])]), Collection([Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])])]), x_0, lambda s, o: final_ctu(o))
query(ANY, lambda x: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/is'), Var('x')).instantiate({'x': x})))