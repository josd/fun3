import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.math import math_sum
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/builtins/math_sum-data.n3').data

def query(r, final_ctu):
    data.find(Iri('http://example.org/r'), Iri('http://example.org/result'), r, lambda s, p, o: final_ctu(o))
    rule_0(r, lambda r_0: final_ctu(r_0))

def rule_0(r_0, final_ctu):
    math_sum(Collection([Literal(1, NS.xsd['int']), Literal(2, NS.xsd['int'])]), r_0, lambda s, o: final_ctu(o))
query(ANY, lambda r: print(Triple(Iri('http://example.org/r'), Iri('http://example.org/result'), Var('r')).instantiate({'r': r})))