import sys # noqa
import pathlib # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve())) # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
from n3.fun.builtins.math import math_sum
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/math_sum_2-data.n3').data

def query(r_0, final_ctu):
    data.find(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), Iri('http://example.org/result'), r_0, lambda s, p, o: final_ctu(o))
    rule_0(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), r_0, lambda a_1, r_2: final_ctu(r_2))

def rule_0(a_1, r_2, final_ctu):
    math_sum(a_1, r_2, lambda s, o: final_ctu(s, o))
query(ANY, lambda r_0: print(Triple(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), Iri('http://example.org/result'), Var('r_0')).instantiate({'r_0': r_0})))