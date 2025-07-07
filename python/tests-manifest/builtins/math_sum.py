import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
from n3.fun.builtins.math import math_sum
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/math_sum-data.n3').data

def query(r_0, final_ctu):
    data.find(Iri('http://example.org/r'), Iri('http://example.org/result'), r_0, lambda s, p, o: final_ctu(o))
    rule_0(r_0, lambda r_1: final_ctu(r_1))

def rule_0(r_1, final_ctu):
    math_sum(Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int'])]), r_1, lambda s, o: final_ctu(o))
query(ANY, lambda r_0: print(Triple(Iri('http://example.org/r'), Iri('http://example.org/result'), Var('r_0')).instantiate({'r_0': r_0})))