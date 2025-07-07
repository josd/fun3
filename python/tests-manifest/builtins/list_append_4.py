import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_append
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_append_4-data.n3').data

def query(x_0, y_1, final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([x_0, y_1]), lambda s, p, o: final_ctu(o[0], o[1]))
    rule_0(x_0, y_1, lambda x_2, y_3: final_ctu(x_2, y_3))

def rule_0(x_2, y_3, final_ctu):
    list_append(Collection([x_2, y_3]), Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int']), Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])]), lambda s, o: final_ctu(s[0], s[1]))
query(ANY, ANY, lambda x_0, y_1: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([Var('x_0'), Var('y_1')])).instantiate({'x_0': x_0, 'y_1': y_1})))