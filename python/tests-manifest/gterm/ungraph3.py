import sys  # noqa
import pathlib  # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))  # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file(
    '/Users/wvw/git/n3/fun3/python/tests-manifest/gterm/ungraph3-data.n3').data


def query(a_0, t_1, final_ctu):
    data.find(a_0, Iri('http://example.org/partType'),
              t_1, lambda s, p, o: final_ctu(s, o))
    rule_0(a_0, t_1, lambda a_2, t_3: final_ctu(a_2, t_3))


def rule_0(a_2, t_3, final_ctu):
    data.find(a_2, Iri('http://example.org/parts'), GraphTerm(triples=[Triple(
        Var('part_4'), NS.rdf['type'], t_3)]), lambda s, p, o: final_ctu(s, o[0][2]))
    rule_1(a_2, GraphTerm(triples=[Triple(Var(
        'part_4'), NS.rdf['type'], t_3)]), lambda q_5, data_6: final_ctu(q_5, data_6[0][2]))


def rule_1(q_5, data_6, final_ctu):
    data.find(q_5, Iri('http://example.org/hasParts'),
              data_6, lambda s, p, o: final_ctu(s, o))


query(ANY, ANY, lambda a_0, t_1: print(Triple(Var('a_0'), Iri(
    'http://example.org/partType'), Var('t_1')).instantiate({'a_0': a_0, 't_1': t_1})))
