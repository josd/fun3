import sys # noqa
sys.path.insert(0, "../../../..") # noqa

from n3.parse import parse_n3_file
from n3.objects import ANY, Terms, Iri, Var, Literal, Collection, GraphTerm, Triple
from n3.ns import NS
data = parse_n3_file('/Users/wvw/git/n3/fun3/python/tests-bench/zika/red/data_red_0pt2_mini.n3').data

emitted = set()
def emit(t, inst_dict):
    global emitted
    t = t.instantiate(inst_dict)
    
    # t_str = str(t)
    # if t_str not in emitted:
    #     print(t_str)
    #     emitted.add(t_str)
        
    if t not in emitted:
        print(t)
        emitted.add(t)
    else:
        print("skipping duplicate")

def query(x_0, final_ctu):
    data.find(x_0, Iri('http://example.org/zika#testForZika'), Literal(True, NS.xsd['boolean']), lambda s, p, o: final_ctu(s))
    rule_0(x_0, lambda id_1_m: final_ctu(id_1_m))

def rule_0(id_1, final_ctu):
    data.find(ANY, Iri('http://example.org/zika#isPregnant'), Literal(True, NS.xsd['boolean']), lambda s, p, o: rule_0_1(id_1, s, final_ctu))
    rule_1(ANY, lambda p_3_m: rule_0_1(id_1, p_3_m, final_ctu))

def rule_0_1(id_1, p_2, final_ctu):
    data.find(p_2, Iri('http://hl7.org/fhir/id'), id_1, lambda s, p, o: final_ctu(o))

def rule_1(p_3, final_ctu):
    data.find(p_3, NS.rdf['type'], Iri('http://hl7.org/fhir/Patient'), lambda s, p, o: rule_1_1(s, final_ctu))

def rule_1_1(p_3, final_ctu):
    data.find(p_3, Iri('http://example.org/utils#hasCondition'), ANY, lambda s, p, o: final_ctu(s))
    rule_3(p_3, ANY, lambda p_8_m, c_9_m: final_ctu(p_8_m))

def rule_2(p_5, r_6, final_ctu):
    data.find(p_5, Iri('http://hl7.org/fhir/id'), ANY, lambda s, p, o: rule_2_1(s, r_6, o, final_ctu))

def rule_2_1(p_5, r_6, id_7, final_ctu):
    data.find(r_6, Iri('http://hl7.org/fhir/subject'), id_7, lambda s, p, o: final_ctu(p_5, s))

def rule_3(p_8, c_9, final_ctu):
    data.find(p_8, Iri('http://example.org/utils#has'), c_9, lambda s, p, o: rule_3_1(s, o, final_ctu))
    rule_2(p_8, c_9, lambda p_5_m, r_6_m: rule_3_1(p_5_m, r_6_m, final_ctu))

def rule_3_1(p_8, c_9, final_ctu):
    data.find(c_9, NS.rdf['type'], Iri('http://hl7.org/fhir/Condition'), lambda s, p, o: final_ctu(p_8, s))
query(ANY, lambda x_0: emit(Triple(Var('x_0'), Iri('http://example.org/zika#testForZika'), Literal(True, NS.xsd['boolean'])), {'x_0': x_0}))