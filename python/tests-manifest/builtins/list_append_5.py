import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_append
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_append_5-data.n3').data

def query(x, y, z, final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([x, y, z]), lambda s, p, o: final_ctu(o[0], o[1], o[2]))
    rule_0(x, y, z, lambda x_0, y_1, z_2: final_ctu(x_0, y_1, z_2))

def rule_0(x_0, y_1, z_2, final_ctu):
    list_append(Collection([Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int']), Literal(3, NS.xsd['int'])]), x_0, y_1, z_2]), Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int']), Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])]), lambda s, o: final_ctu(s[1], s[2], s[3]))
query(ANY, ANY, ANY, lambda x, y, z: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/is'), Collection([Var('x'), Var('y'), Var('z')])).instantiate({'x': x, 'y': y, 'z': z})))