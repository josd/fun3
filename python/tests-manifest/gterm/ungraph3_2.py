import sys  # noqa
import pathlib  # noqa
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.resolve()))  # noqa
from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file(
    '/Users/wvw/git/n3/fun3/python/tests-manifest/gterm/ungraph3-data.n3').data


def query(a_0, final_ctu):
    data.find(a_0, Iri('http://example.org/partType'),
              Iri('http://example.org/machine'), lambda s, p, o: final_ctu(s))
    rule_0(a_0, Iri('http://example.org/machine'),
           lambda a_1, t_2: final_ctu(a_1))


def rule_0(a_1, t_2, final_ctu):
    data.find(a_1, Iri('http://example.org/parts'), GraphTerm(triples=[Triple(
        Var('part_3'), NS.rdf['type'], t_2)]), lambda s, p, o: final_ctu(s, o[0][2]))
    rule_1(a_1, GraphTerm(triples=[Triple(Var(
        'part_3'), NS.rdf['type'], t_2)]), lambda q_4, data_5: final_ctu(q_4, data_5[0][2]))


def rule_1(q_4, data_5, final_ctu):
    data.find(q_4, Iri('http://example.org/hasParts'),
              data_5, lambda s, p, o: final_ctu(s, o))


query(ANY, lambda a_0: print(Triple(Var('a_0'), Iri('http://example.org/partType'),
      Iri('http://example.org/machine')).instantiate({'a_0': a_0})))
