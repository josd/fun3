import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.math import math_sum
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/math_sum_2-data.n3').data

def query(r, final_ctu):
    data.find(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), Iri('http://example.org/result'), r, lambda s, p, o: final_ctu(o))
    rule_0(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), r, lambda a_0, r_1: final_ctu(r_1))

def rule_0(a_0, r_1, final_ctu):
    math_sum(a_0, r_1, lambda s, o: final_ctu(s, o))
query(ANY, lambda r: print(Triple(Collection([Literal(1, NS.xsd['int']), Literal(4, NS.xsd['int'])]), Iri('http://example.org/result'), Var('r')).instantiate({'r': r})))