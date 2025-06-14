import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.list import list_append
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/list_append_2-data.n3').data

def query(final_ctu):
    data.find(Iri('http://example.org/result'), Iri('http://example.org/is'), Iri('http://example.org/correct'), lambda s, p, o: final_ctu())
    rule_0(lambda: final_ctu())

def rule_0(final_ctu):
    list_append(Collection([Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int'])]), Collection([Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])])]), Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int']), Literal(3, NS.xsd['int']), Literal(4, NS.xsd['int'])]), lambda s, o: final_ctu())
query(lambda: print(Triple(Iri('http://example.org/result'), Iri('http://example.org/is'), Iri('http://example.org/correct')).instantiate({})))