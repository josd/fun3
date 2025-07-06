from n3.ns import NS
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.parse import parse_n3_file
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))
data = parse_n3_file(
    '/Users/wvw/git/n3/fun3/python/tests-manifest/gterm/ungraph1-data.n3').data


def query(a, xl, final_ctu):
    data.find(a, Iri('http://example.org/partLabel'),
              xl, lambda s, p, o: final_ctu(s, o))
    rule_0(a, xl, lambda a_0, xl_1: final_ctu(a_0, xl_1))


def rule_0(a_0, xl_1, final_ctu):
    data.find(a_0, Iri('http://example.org/parts'), GraphTerm(triples=[Triple(Iri(
        'http://example.org/robotorso'), NS.rdf['type'], Var('x_2'))]), lambda s, p, o: rule_0_1(s, xl_1, x_2, final_ctu))
    rule_1(a_0, Iri('http://example.org/robotorso'), ANY, lambda q_3,
           part_4, t_5: rule_0_1(q_3, xl_1, t_5, final_ctu))


def rule_0_1(a_0, xl_1, x_2, final_ctu):
    data.find(x_2, Iri('http://example.org/label'),
              xl_1, lambda s, p, o: final_ctu(a_0, o))


def rule_1(q_3, part_4, t_5, final_ctu):
    data.find(q_3, Iri('http://example.org/has'), part_4,
              lambda s, p, o: rule_1_1(s, o, t_5, final_ctu))


def rule_1_1(q_3, part_4, t_5, final_ctu):
    data.find(part_4, NS.rdf['type'], t_5,
              lambda s, p, o: final_ctu(q_3, s, o))


query(ANY, ANY, lambda a, xl: print(Triple(Var('a'), Iri(
    'http://example.org/partLabel'), Var('xl')).instantiate({'a': a, 'xl': xl})))
