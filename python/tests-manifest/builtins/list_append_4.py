import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_append
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_append_4-data.n3').data

def query(x, y, final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([x, y]), lambda s, p, o: final_ctu(o[0], o[1]))
    rule_0(x, y, lambda x_0, y_1: final_ctu(x_0, y_1))

def rule_0(x_0, y_1, final_ctu):
    list_append(Collection([x_0, y_1]), Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int']), Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])]), lambda s, o: final_ctu(s[0], s[1]))
query(ANY, ANY, lambda x, y: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([Var('x'), Var('y')])).instantiate({'x': x, 'y': y})))