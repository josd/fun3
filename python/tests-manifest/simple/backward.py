import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
from n3.parse import parse_n3_file
from n3.objects import Iri, Var, Literal, Collection, ANY, Terms, Triple
from n3.ns import NS
from n3.fun.builtins.math import math_greaterThan
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-manifest/simple/empty.ttl').data

def query(final_ctu):
    data.find(Literal(5, NS.xsd['int']), Iri('http://example.org/#moreInterestingThan'), Literal(3, NS.xsd['int']), lambda s, p, o: final_ctu())
    rule_0(Literal(5, NS.xsd['int']), Literal(3, NS.xsd['int']), lambda X_0, Y_1: final_ctu())

def rule_0(X_0, Y_1, final_ctu):
    math_greaterThan(X_0, Y_1, lambda s, o: final_ctu(s, o))
query(lambda: print(Triple(Literal(5, NS.xsd['int']), Iri('http://example.org/#moreInterestingThan'), Literal(3, NS.xsd['int'])).instantiate({})))